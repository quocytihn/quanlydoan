from django import forms
from .models import SinhVien, GiangVien

class SinhVienForm(forms.ModelForm):
    class Meta:
        model = SinhVien
        fields = ['ma_sinh_vien', 'ho_ten', 'so_tin_chi_da_dat', 'gpa', 'co_no_mon']

class GiangVienForm(forms.ModelForm):
    class Meta:
        model = GiangVien
        fields = ['ma_giang_vien', 'ho_ten', 'email', 'so_dien_thoai', 'khoa', 'chuc_vu', 'so_luong_toi_da']
