# 10 негативных тестов ниже

from api import PetFriends
from settings import *
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)


    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):


    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)


        assert status == 200
        assert result['name'] == name
    else:

        raise Exception("There is no my pets")

# 1.GET Негативный тест с некорректным вводом email и пароль
def test_invalid_email_password(email=invalid_email, password=invalid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 401

# 2.GET Негативный тест с пустыми полями email и пароль
def test_null_email_password(email='', password=''):

    status, result = pf.get_api_key(email, password)

    assert status == 400
    assert result['message'] == 'please fill in all fields'

# 3. POST Негативный тест – недопустимый тип данных поля name
def test_add_new_pet_with_invalid_name_type(name={'Кот': 'Марсик'}, animal_type='двортерьер', age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 500
    assert result["message"] == 'something bad happened'

# 4. POST Негативный тест – пустое поле name
def test_add_new_pet_with_null_name(name='', animal_type='двортерьер', age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result["message"] == 'please enter name'

# 5. POST Негативный тест – загрузка некорректного типа данных в фото
def test_add_invald_photo_type(name='', animal_type='двортерьер', age='4', pet_photo='images/cat.txt'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

# 6. DELETE Деструктивное тестирование – недопустимый HTTP метод
def test_delete_pet_from_create_option(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.try_delete_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 405

# 7. PUT Негативный тест с корректным вводом – некорректный id питомца (pet_id)
def test_update_pet_with_wrong_id(name='Мурзик', animal_type='Котэ', age=5):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][-10]['id'], name, animal_type, age)

        assert status == 400
        assert result['name'] != name
    else:

        raise Exception("There is no my pets")

# 8. POST Негативный тест – пустое поле animal_type
def test_add_new_pet_with_null_animal_type(name='Мурзик', animal_type='', age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result["message"] == 'please animal_type'

# 9. POST Негативный тест – неверный тип данных в age
def test_add_new_pet_with_invalid_age_data(name='Мурзик', animal_type='сибирский', age='привет', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result["message"] == 'wrong data type'

# 10. POST Негативный тест – отсутствующий файл загрузки
def test_set_null_photo(name='Мурзик', animal_type='сибирский', age='привет', pet_photo=''):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
