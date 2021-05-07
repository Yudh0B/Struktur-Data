def bubble(sorting_list):
    index_length = len(sorting_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if sorting_list[i] > sorting_list[i+1]:
                sorted = False
                sorting_list[i], sorting_list[i+1] = sorting_list[i+1], sorting_list[i]
    return sorting_list

def merge_sort(sorting_list):
    if len(sorting_list) <= 1:
        return sorting_list
    midpoint = int(len(sorting_list) / 2)
    left, right = merge_sort(sorting_list[:midpoint]), merge_sort(sorting_list[midpoint:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def main_merge():
    sorting_list = []
    number = int(input("Masukan jumlah maksimal angka dalam list : "))
    print("Masukkan satu angka lalu tekan enter")
    for i in range(number):
        x = int(input())
        sorting_list.append(x)
    print(sorting_list)
    result = merge_sort(sorting_list)
    print(result)


def main_bubble():
    sorting_list = []
    number = int(input("Masukan jumlah maksimal angka dalam list : "))
    print("Masukkan satu angka lalu tekan enter")
    for i in range(number):
        x = int(input())
        sorting_list.append(x)
    print(sorting_list)
    bubble(sorting_list)
    print(sorting_list)

z=1
while z==1:
    print("Pilih salah satu di bawah ini : ")
    print("1. Merge Sort")
    print("2. Bubble Sort")
    print("3. Sudahi Program")
    y=int(input("Pilihan : "))
    if y==1:
        main_merge()
    elif y==2:
        main_bubble()
    else:
        break

