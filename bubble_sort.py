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

sorting_list=[]
number=int(input("Masukan jumlah maksimal angka dalam list : "))
print("Masukkan satu angka lalu tekan enter")
for i in range(number):
    x=int(input())
    sorting_list.append(x)

print(sorting_list)
bubble(sorting_list)