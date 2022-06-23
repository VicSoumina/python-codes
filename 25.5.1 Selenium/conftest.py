import pytest
from selenium import webdriver



@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/viktoriasumina/PycharmProjects/tests/chromedriver')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('victroia@yamdex.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('123abc')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   yield

   pytest.driver.quit()