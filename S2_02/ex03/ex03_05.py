#input: list
#output: dictionary luu gia tri phan tu va vi tri cua no
#dictionary: luu tru cac cap gia tri khong co thu tu, bieu dien bang dau {} va moi cap phan cach bang dau :
#key trong dictionary luon la duy nhat va khong the thay doi, value co the la bat ki gia tri nao
#khai bao: my_dict = {}
#person = {"name": "alice", "age": 25}

def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst: 
        if item in count_dict:
            count_dict[item] += 1
            
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhap danh sach cac tu, cach nhau bang dau cach : ")
word_list = input_string.split()

so_lan_xuat_hien_tu = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua mot tu la: ", so_lan_xuat_hien_tu)


