from QLSV import quanlysinhvien

# Khởi tạo đối tượng quản lý sinh viên
qlsv = quanlysinhvien()

while True:
    print("\nChuong trinh quan ly sinh vien")
    print("**********************************************")
    print("** 1. Them sinh vien")
    print("** 2. Cap nhat thông tin sinh vien")
    print("** 3. Xoa sinh viên bang ID")
    print("** 4. Hien thi danh sach sinh vien")
    print("** 5. Sap xep sinh viên theo diem trung binh")
    print("** 6. Sap xep sinh vien theo chuyen nganh")
    print("** 7. Thoat chuong trinh")
    print("**********************************************")

    choice = input("Chon chuc nang (1-7): ")

    if choice == '1':
        qlsv.nhapsinhvien()

    elif choice == '2':  
        try:
            ID = int(input("Nhap ID sinh viên can cap nhat: "))
            qlsv.updateSinhvien(ID)
        except ValueError:
            print("ID phai la mot so nguyen!")

    elif choice == '3':  
        try:
            ID = int(input("Nhap ID sinh viên can xoa: "))
            qlsv.deletebyID(ID)
        except ValueError:
            print("ID phai la mot so nguyen!")

    elif choice == '4':  
        print("\nDanh sach sinh vien:")
        qlsv.showsinhvien()

    elif choice == '5': 
        qlsv.sortbydiemTB()
        print("\nDanh sach sinh vien da duoc sap xep theo diem trung binh:")
        qlsv.showsinhvien()
        
    elif choice == '6':
        if(qlsv.soluongsinhvien() > 0):
            print("\n6.Sap xep sinh vien theo ten.")
            qlsv.findbyname()
            qlsv.showsinhvien(qlsv.getlistSinhvien())
        
        else:
            print("\nDanh sach sinh vien trong")
            
    elif choice == '7':  
        print("Thoat chuong trinh...")
        break

    else:
        print("Lua chon khong hop le! Vui long chon lai tu 1 đến 6.")
