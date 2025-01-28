from django.contrib import admin
from .models import SinhVien, GiangVien, DeTai, DoAn

# Quản lý model SinhVien
@admin.register(SinhVien)
class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('ma_sinh_vien', 'ho_ten', 'so_tin_chi_da_dat', 'gpa', 'co_no_mon')
    search_fields = ('ma_sinh_vien', 'ho_ten')
    list_filter = ('co_no_mon',)
    ordering = ('ma_sinh_vien',)

# Quản lý model GiangVien
@admin.register(GiangVien)
class GiangVienAdmin(admin.ModelAdmin):
    list_display = ('ma_giang_vien', 'ho_ten', 'email', 'so_dien_thoai', 'khoa', 'so_luong_toi_da')
    search_fields = ('ma_giang_vien', 'ho_ten', 'email', 'khoa')
    list_filter = ('khoa',)
    ordering = ('ma_giang_vien',)

@admin.register(DeTai)
class DeTaiAdmin(admin.ModelAdmin):
    list_display = ('ma_de_tai','ten_de_tai','so_luong_toi_da')
    search_fields = ('ma_de_tai','ten_de_tai')

@admin.register(DoAn)
class DeTaiAdmin(admin.ModelAdmin):
    list_display = ('de_tai','sinh_vien','giang_vien_huong_dan',)
    search_fields = ('de_tai',)
