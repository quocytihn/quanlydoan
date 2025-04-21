from django.db import models

# sinh viên phải hoàn thành 100 tín chỉ và điểm trung bình tích lũy từ 2.5 trở lên và không nợ môn
class SinhVien(models.Model):
    ma_sinh_vien = models.CharField(max_length=255, unique=True)
    ho_ten = models.CharField(max_length=100)
    so_tin_chi_da_dat = models.PositiveIntegerField(default=0)  # Tín chỉ đã hoàn thành
    gpa = models.FloatField(default=0.0)  # Điểm trung bình tích lũy
    co_no_mon = models.BooleanField(default=False)  # Cờ để kiểm tra nợ môn

    def __str__(self):
        return f"{self.ma_sinh_vien}-{self.ho_ten}"
    def du_dieu_kien_do_an(self):
        return self.so_tin_chi_da_dat >= 100 and self.gpa >= 2.5 and not self.co_no_mon
    
# Mỗi giảng viên chỉ có thể hướng dẫn tối đa 5 đề tài 
class GiangVien(models.Model):
    ma_giang_vien = models.CharField(max_length=10, unique=True)
    ho_ten = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=15)
    khoa = models.CharField(max_length=50)
    chuc_vu = models.CharField(max_length=50, null=True, blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    so_luong_toi_da = models.PositiveIntegerField(default=5)  # Số lượng đồ án tối đa
    def __str__(self):
        return f"{self.ho_ten} - {self.khoa}"
    def so_luong_de_tai_hien_tai(self):
        return self.do_an_set.count()
    def con_du_kha_nang_huong_dan(self):
        return self.so_luong_de_tai_hien_tai() < self.so_luong_toi_da

# Mỗi đề tài chỉ cho phép tôi đa 3 sinh viên tham gia
class DeTai(models.Model):
    ma_de_tai = models.CharField(max_length=10, unique=True)
    ten_de_tai = models.CharField(max_length=200, unique=True)
    so_luong_toi_da = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.ma_de_tai}-{self.ten_de_tai  }"
    def con_sinh_vien_co_the_dang_ky(self):
        return self.do_an.count() < self.so_luong_toi_da


class DoAn(models.Model):
    de_tai = models.ForeignKey(DeTai, on_delete=models.CASCADE, related_name='do_an')
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='do_an_sinh_vien')
    giang_vien_huong_dan = models.ForeignKey(GiangVien, on_delete=models.SET_NULL, null=True, blank=True, related_name='do_an_set')
    #Giảng viên nếu bị xóa thì giảng viên sẽ để trống!
    #kiểm tra 
    def save(self, *args, **kwargs):
        if not self.de_tai.con_sinh_vien_co_the_dang_ky():
            raise ValueError("Đề tài này đã đủ số lượng sinh viên.")
        if self.giang_vien_huong_dan and not self.giang_vien_huong_dan.con_du_kha_nang_huong_dan():
            raise ValueError(f"Giảng viên {self.giang_vien_huong_dan.ho_ten} đã đạt giới hạn số lượng đồ án hướng dẫn.")
        super().save(*args, **kwargs)


class HoiDongCham(models.Model):
    ten_hoi_dong = models.CharField(max_length=100, unique=True)
    giang_vien = models.ManyToManyField(GiangVien, related_name='hoi_dong')

    def so_luong_thanh_vien(self):
        return self.giang_vien.count()

    def du_dieu_kien_thanh_lap(self):
        return 3 <= self.so_luong_thanh_vien() <= 5

class LichBaoVe(models.Model):
    hoi_dong = models.ForeignKey(HoiDongCham, on_delete=models.CASCADE, related_name='lich_bao_ve')
    do_an = models.ForeignKey(DoAn, on_delete=models.CASCADE, related_name='lich_bao_ve')

    def save(self, *args, **kwargs):
        if self.do_an.giang_vien_huong_dan in self.hoi_dong.giang_vien.all():
            raise ValueError("Giảng viên hướng dẫn không được tham gia chấm đồ án của mình.")
        super().save(*args, **kwargs)

