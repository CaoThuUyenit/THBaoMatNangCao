from sinhvien import sinhvien

class quanlysinhvien:
    listsinhvien = []
    
    def generationID(self):
        maxID = 1
        if self.soluongsinhvien() > 0:
            maxID = self.listsinhvien[0]._id
            for sv in self.listsinhvien:
                if maxID < sv._id:
                    maxID = sv._id + 1
        return maxID
    
    def soluongsinhvien(self):
        return len(self.listsinhvien)  # trả về số lượng sinh viên
    
    def nhapsinhvien(self):
        svId = self.generationID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh: ") 
        diemTB = float(input("Nhap diem trung binh: "))
        sv = sinhvien(svId, name, sex, major, diemTB)
        self.xeploaisinhvien(sv)
        self.listsinhvien.append(sv)
        
    def updateSinhvien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh: ") 
            diemTB = float(input("Nhap diem trung binh: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xeploaisinhvien(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")
    
    def sortbyID(self):
        self.listsinhvien.sort(key=lambda x: x.id, reverse= False)
        
    def sortbydiemTB(self):
        self.listsinhvien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def sortbyName(self):
        self.listsinhvien.sort(key=lambda x:x._name, reverse=False)
        
    def findByID(self, ID):
        for sv in self.listsinhvien:
            if sv.id == ID:
                return sv
        return None
    
    def findbyname(self, name):
        result = []
        for sv in self.listsinhvien:
            if name.lower() in sv.name.lower():
                result.append(sv)
        return result
        
    def deletebyID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listsinhvien.remove(sv)
            print(f"Sinh vien co ID = {ID} da bi xoa.")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")
        
    def xeploaisinhvien(self, sv: sinhvien):
        if sv._diemtb >= 8:
            sv._hocluc = 'Gioi'
        elif sv._diemtb >= 6.5:
            sv._hocluc = 'Kha'
        elif sv._diemtb >= 5:
            sv._hocluc = 'Trung binh'
        else:
            sv._hocluc = 'Yeu'

    def showsinhvien(self, listsv=None):
        if listsv is None:
            listsv = self.listsinhvien
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        for sv in listsv:
            print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemtb, sv._hocluc))
        print("\n")

    def getlistSinhvien(self):
        return self.listsinhvien
