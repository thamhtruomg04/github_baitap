'''
connguoi
    hoten
    namsinh
    
    an()
    uong()
    ngu()

hocsinh
    hoten
    namsih
    lop
    ten TRuong
    
    an()
    uong()
    ngu()
    lambaiTap()'''

class ConNguoi:
    def __init__(self, hoVaTen, namSinh):
        self.hoVaTen = hoVaTen
        self.namSinh = namSinh
    
    def an():
        print("Unknow")
    def uong():
        print("Unknow")
    def ngu():
        print("Unknow")

class HocSinh(ConNguoi):
    def __init__(self, hoVaTen, namSinh, lop, tenTruong):
        super().__init__(hoVaTen, namSinh)
        self.lop = lop
        self.tenTruong = tenTruong
    def an(self):
        print("{0} an cua hoang de".format(self.hoVaTen))
    def uong(self):
        print("{0} uong nuoc cocacola".format(self.hoVaTen))
    def ngu(self):
        print("{0} tren giuong".format(self.hoVaTen))
    def lamBaiTap(self):
        print("{0} lam bai tap toan".format(self.hoVaTen))
    def printME(self):
        print("Ten la {0} sinh nam {1} hoc lop {2} o truong {3}".format(self.hoVaTen, self.namSinh, self.lop, self.tenTruong))
hocsinh1 = HocSinh("Vu Thanh Truong", "2004", "DCCT", "HUMG")
hocsinh1.an()
hocsinh1.uong()
hocsinh1.ngu()
hocsinh1.lamBaiTap()
hocsinh1.printME()