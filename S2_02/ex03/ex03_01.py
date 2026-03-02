#tinh tong cac so chan trong list
#list la danh sach luu tru phan tu co thu tu va co the thay doi
#chi so danh sach bat dau tu 0 
#chua nhieu kieu du lieu trong 1 list
#append(), remove(), pop()(xoa phan tu chi dinh tra ve gia tri phan tu do)
#insert()them, #sort()sap xep, len()do dai danh sach
def tinhtong(lst):
    tong = 0
    #duyet qua tung phan tu trong danh sach
    for num in lst:
       if num % 2 == 0:
           tong += num
    return tong 
    

input_lst = input("danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_lst.split(",")))
numbers.append(6) #them so 6 vao cuoi danh sach
del numbers[3] # xoa phan tu thu 4 (list bat dau tu 0)
print(numbers)
numbers[1] = 23 # cap nhat phan tu so 2
print(numbers)
tongchan = tinhtong(numbers)
print("Tong cac so chan trong list: ", tongchan)