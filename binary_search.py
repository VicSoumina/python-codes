def binary_search(lst, search_number):
    low = 0
    high = len(lst) - 1
    search_result = False

    while low <= high and not search_result:
        middle = (low + high) // 2
        guess_number = lst[middle]
        if guess_number == search_number:
            search_result = True
            return search_result
        if guess_number > search_number:
            high = middle - 1
        else:
            low = middle + 1
    return search_result

def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst

def quick_sort_helper(lst, low, high):
    if low < high:
        split_point = separations(lst, low, high)
        quick_sort_helper(lst, low, split_point - 1)
        quick_sort_helper(lst, split_point + 1, high)

def separations(lst, low, high):
    pivot_value = lst[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while  right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[low], lst[right_mark] = lst[right_mark], lst[low]
    return right_mark



lst = list(map(int, input().split()))
print("Исходный массив: ", lst)
result_sort = quick_sort(lst)
print("Результат сортировки: ", result_sort)

value = int(input())
result = binary_search(lst, value)
if result:
    print("Искомое число есть в списке")
else:
    print("Искомого числа нет в списке")