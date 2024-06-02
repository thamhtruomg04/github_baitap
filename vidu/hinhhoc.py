class HinhHoc():
    def __init__(self, ten):
        self.pi = 3.14
        self.ten = ten
        #self.chuVi = chuVi
        #self.dienTich = dienTich
        #self.theTich = theTich
    

class HinhChuNhat(HinhHoc):
    def __init__(self, ten, chieuDai, chieuRong):
        super().__init__(ten)
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
    def xuatTen(self):
        return self.ten
    def chuViHinhChuNhat(self):
        return (self.chieuDai + self.chieuRong) * 2
    def dienTichHinhChuNhat(self):
        return self.chieuDai * self.chieuRong
    
class HinhTron(HinhHoc):
    def __init__(self, ten, banKinh):
        super().__init__(ten)
        self.banKinh = banKinh
        
    def xuatTen(self):
        return self.ten
    def tinhChuViHinhTron(self):
        return (self.banKinh * 2) * self.pi
    def tinhDienTichHinhTron(self):
        return ((self.banKinh) * 2) * self.pi
    
class HinhTru(HinhTron):
    def __init__(self, ten, banKinh, chieuCao):
        super().__init__(ten, banKinh)
        self.chieuCao = chieuCao
    def xuatTen(self):
        return self.ten
    def tinhDienTichXungQuanh(self):
        return 2 * self.pi * self.banKinh * self.chieuCao
    def dienTichToanPhan(self):
        return 2 * self.pi *self.banKinh * (self.banKinh + self.chieuCao)
    
class HinhVuong(HinhChuNhat):
    def __init__(self, ten, chieuDai, chieuRong, canh):
        super().__init__(ten, chieuDai, chieuRong)
        self.canh = canh
    def xuatTen(self):
        return self.ten
    def tinhChuViHinhVuong(self):
        return self.canh * 4
    def tinhDienTichHinhVuong(self):
        return (self.canh) ** 2
    

def main():
    hinhchunhat = HinhChuNhat("Hinh Chu Nhat", 12 , 5)
    tenhinhchunhat = hinhchunhat.xuatTen()
    chuvihinhchunhat = hinhchunhat.chuViHinhChuNhat()
    dientichhinhchunhat = hinhchunhat.dienTichHinhChuNhat()
    print(tenhinhchunhat)
    print(chuvihinhchunhat)
    print(dientichhinhchunhat)

    print("\n")

    hinhtron = HinhTron("Hinh Tron", 4)
    tenhinhtron = hinhtron.xuatTen()
    chuvihinhtron = hinhtron.tinhChuViHinhTron()
    dientichhinhtron = hinhtron.tinhDienTichHinhTron()
    print(tenhinhtron)
    print(dientichhinhtron)
    print(chuvihinhtron)

    print("\n")

    hinhtru = HinhTru("Hinh Tru", 4, 8)
    tenhinhtru = hinhtru.xuatTen()
    dientichxungquanh = hinhtru.tinhDienTichXungQuanh()
    dientichtoanphan = hinhtru.dienTichToanPhan()
    print(tenhinhtru)
    print(dientichxungquanh)
    print(dientichtoanphan)

    print("\n")

    hinhvuong = HinhVuong("Hinh Vuong", 10, 4, 5)
    tenhinhvuong = hinhvuong.xuatTen()
    chuvihinhvuong = hinhvuong.tinhChuViHinhVuong()
    dientichhinhvuong = hinhvuong.tinhDienTichHinhVuong()
    print(tenhinhvuong)
    print(chuvihinhvuong)
    print(dientichhinhvuong)
    

if __name__ == "__main__":
    main()

    

    
        