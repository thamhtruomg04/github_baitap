class Ngay:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    
    @staticmethod
    def kiemTraSoNgayCuaThang(thang, nam):
        if (thang in [1,3,5,7,8,10,12]):
            return 31
        elif (thang in [4,6,9,11]):
            return 30
        elif (thang == 2):
            if (nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
                return 29
            else:
                return 28
         

    def traVeNgayTrongNam(self):
        #thangTruoc = self.thang - 1
        giaTriNgayTrongNam = 0

        # Tinh tong so luong ngay cua nhung thang truoc
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.kiemTraSoNgayCuaThang(x, self.nam)
        giaTriNgayTrongNam += self.ngay

        # tra ve ket quan
        return giaTriNgayTrongNam
   
ngayA = Ngay(15,3,2022)
print(ngayA.traVeNgayTrongNam())

ngayB = Ngay(15,1,2022)
print(ngayB.traVeNgayTrongNam())