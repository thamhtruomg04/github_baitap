class Item():
    def __init__(self, tenMatHang:str, soLuong=int, giaCa=1000):
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
    


item1 = Item("IPhone 14 promax 14", 12, 23000000)
item2 = Item("Sam Sumg glx 21 ultra,", 15, 26000000)
item3 = Item("Oppo zeno8",12)

print(item3.soLuong)

print(item1.tinhTien())

print(Item.checkGia(5000))



