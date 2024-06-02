# Tạo một lớp shape và lớp con là square kế thừa phương thức
# Tính diện tích của lớp cha shape tính diện tích hình vuông cạnh = 5

class Shape():
    def __init__(self, canh):
        self.canh = canh
    
class Square(Shape):
    def __init__(self, canh):
        super().__init__(canh)
    def dienTich_hinhVuong(canh):
        return canh * canh
dientich_hinhvuong = Square.dienTich(5)
print(dientich_hinhvuong)