#input: list #output: list nguoc
#dao nguoc list vd: 2, 3, 5 --> 5, 3, 2 nguyen tac in tu ngoai vao trong
def dao_nguoc_list(lst):
    return lst[::-1]

input_lst = input("nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_lst.split(',')))
list_daonguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc: ",list_daonguoc)