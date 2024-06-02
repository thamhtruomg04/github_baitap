# Đa hình thực hiện các phương thức khác nhau ở hai class khác nhau mà 2 class có thuộc tính giống nhau

class sinhVienNuocNgoai():
    def __init__(self, hoTen, maSinhVien, queQuan):
        self.hoTen = hoTen
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan

    def chao(self):
        print("Hello")



class sinhVienVietNam():
    def __init__(self, hoTen, maSinhVien, queQuan):
        self.hoTen = hoTen
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan

    def chao(self):
        print("Xin chao")

def hi(sinhVienNuocNgoai): # class có thuộc tính giống nhau gọi 1 trong 2 đều được
    sinhVienNuocNgoai.chao()

sinhVien1 = sinhVienNuocNgoai("Bob", 12328, "USA")
sinhVien2 = sinhVienVietNam("Thanh Truong", 218738, "Hung Yen")

sinhVien1.chao()
sinhVien2.chao()

hi(sinhVien1)
hi(sinhVien2)