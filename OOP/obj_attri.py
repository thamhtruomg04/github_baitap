class Item():
    def __init__(self, tenMatHang, soLuong, giaCa):
        self.tenMatHang = tenMatHang
        self.soLuong = soLuong
        self.giaCa = giaCa
item1 = Item("IPhone 14 promax 14", 12, 23000000)
item2 = Item("Sam Sumg glx 21 ultra,", 15, 26000000)

print("Mat hang 1 co ten la: ", item1.tenMatHang)
print("Mat hang 2 co gia la: ", item2.giaCa)

print(f"Gia mat hang 1 la: {item1.giaCa} va so luong con lai cua mat hang 1 la: {item1.soLuong}")


class SinhVien():
    def __init__(self, hoTen, maSinhVien, queQuan):
        self.hoTen = hoTen
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan
sinhvien1 = SinhVien("Vũ Thành Trương", 234324, "Hưng Yên")
sinhvien2 = SinhVien("Vũ Hoàng Đức", 2783924, "Hưng Yên")
sinhvien3 = SinhVien("Vũ Minh Khang", 2823, "Hưng Yên")

print(f"Sinh viên 1 có tên là: {sinhvien1.hoTen} và có mã sinh viên là: {sinhvien1.maSinhVien}, quê ở {sinhvien1.queQuan}")
print(f"Sinh viên 2 có tên là: {sinhvien2.hoTen} và mã sinh viên là: {sinhvien2.maSinhVien}, quê ở {sinhvien2.queQuan}")
print(f"Sinh viên 3 có tên là: {sinhvien3.hoTen} và có mã sinh viên là: {sinhvien3.maSinhVien}, quê ở {sinhvien3.queQuan}")
        