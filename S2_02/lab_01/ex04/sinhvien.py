class sinhvien:
    def __init__(self, id, name, sex, major, diemtb):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemtb = diemtb
        self._hocluc = ""

    def __str__(self):
        return f"ID: {self._id}, Ten: {self._name}, Gioi tinh: {self._sex}, Chuyen nganh: {self._major}, Điểm TB: {self._diemtb}, Học lực: {self._hocluc}"
