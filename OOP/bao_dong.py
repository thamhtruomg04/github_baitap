class Bank():
    def __init__(self, hoTen, chungMinhThu):
        self.hoTen = hoTen
        self.chungMinhThu = chungMinhThu

class NhanVien(Bank):
    def __init__(self, hoTen, chungMinhThu):
        super().__init__(hoTen, chungMinhThu)
        self.__luongTra = 500000 # sử dụng 2 đấu gạch dưới gán private
                                 # Không cho phép truy cập từ bên ngoài
        # có thể can thiệp vào lương
    def get_luongTra(self):
        return self.__luongTra
    
    def set_luongTra(self, tangLuongTra):
        self.__luongTra = tangLuongTra


nhanVien1 = NhanVien("Thanh Truong", 1293483281)
nhanVien2 = NhanVien("Minh Khang", 13921891)

nhanVien2.set_luongTra(999999999999)
print("Luong moi cua nhan vien 2 la: ",nhanVien2.get_luongTra())











'''print(nhanVien1.chungMinhThu, nhanVien1.hoTen)
print(nhanVien1.luongTra)

nhanVien2.__luongTra = 10239129031293
print(nhanVien2.luongTra)
        '''