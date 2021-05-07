def cari_sama(my_list,elemen):
    backup_list=[]
    mark = False
    for i in range(len(my_list)):
        if elemen == my_list[i]:
            mark = True
            backup_list.append(i)
            
    if mark == True:    
        print("list ini memiliki data yang sama dengan elemen yang anda ketik pada index")
        for i in backup_list:
            print(i)
    else:
        print("tidak ditemukan kesamaan data")

def main_function():
    i=1
    while i==1:
        elemen = (int(input("Ketik elemen yang ingin dicari : ")))
        cari_sama(my_list,elemen)

my_list = [56,20,12,45,100,34,35,13,17,90,110,500,1200,59,62,63,75,79]
print(my_list)
main_function()


    