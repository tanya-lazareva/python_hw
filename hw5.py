#СОРТРОВКА СПИСКА ЧИСЕЛ ВСТАВКОЙ

num_list = list(map(int, input('Введите значения элементов списка: ').split()))

def ins_sort(list):
    for i in range(1, len(list)):
        s_num = list[i]
        j = i - 1
        while j >= 0 and list[j] > s_num:
            list[j+1] = list[j]
            j = j - 1
        list[j + 1] = s_num
    print('Отсортированный список:', list)

ins_sort(num_list)