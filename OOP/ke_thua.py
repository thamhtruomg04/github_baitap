class Item():
    def __init__(self, tenMatHang: str, soLuong=int, giaCa=float):
        self.tenMatHang = tenMatHang
        self.soLuong = soLuong
        self.giaCa = giaCa

    # Kiem tra dieu kien thuoc tinh
        assert soLuong >= 0
        assert giaCa >= 0


    def tinhTien(self):
        return self.soLuong * self.giaCa

    # Phuong thuc tinh
    @staticmethod
    def checkGia(gia):
        if gia <= 500:
            return "Cheap, dat o tang 1"
        else:
            return "Expensive, dat o tang 2"
    
# khoi tao class con (Ke thua)
class Phone(Item):
    def __init__(self, tenMatHang: str, soLuong=int, giaCa=float, loai = "4G"):
        super().__init__(tenMatHang, soLuong, giaCa)
        self.loai = loai

    
    


phone1 = Phone("SumSum note 20", 12, 10000000, "5G")
phone2 = Phone("SamSum note 21", 12, 99000000)

print(f"{phone1.tenMatHang} co gia la: {phone1.loai}")

print(f"{phone2.tenMatHang} co gia la: {phone2.loai}")



item1 = Item("IPhone 14 promax 14", 12, 23000000)
item2 = Item("Sam Sumg glx 21 ultra,", 15, 26000000)
item3 = Item("Oppo zeno8",12, 18000000)

print(item3.soLuong)

print(item1.tinhTien())

print(Item.checkGia(5000))



