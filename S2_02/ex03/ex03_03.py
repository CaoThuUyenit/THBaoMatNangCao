#input: list
#output: tuple
#tuple luu dang thong tin khong the thay doi, theo thu tu, su dung dau ngoac don() va dau phay ','
#vd: khi khai bao: my_tuple = (1, 2, 3, 4, 5), mixed_tuple =(1, "alcie", 4)
#count(value), index(value), append(), sort(), remove()

def tao_tuple_tu_list(lst):
    return tuple(lst)


input_list = input("nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print("tuple tu list la: ", my_tuple)