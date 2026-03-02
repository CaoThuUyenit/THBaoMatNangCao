#input: mot tuple
#output: tra ve phan tu dau va cuoi cua tuple
#evla thuc thi chuoi nhap vao bieu thuc python 
#input(): Dùng để nhận dữ liệu từ người dùng dưới dạng chuỗi.
#eval(): Chạy chuỗi này như là mã Python, ví dụ nếu bạn nhập vào 1 + 2, eval() sẽ trả về kết quả 3
def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
    
input_tuple = eval(input("nhap mot tuple vi du(1, 3, 4, 5): "))
first, last = truy_cap_phan_tu(input_tuple)

print("phan tu dau tien: ", first)
print("phan tu cuoi cung: ", last)