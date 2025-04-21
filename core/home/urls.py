from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('', views.login_view, name='login'),
    # Sinh viên
    path('sinhvien/', views.sinhvien_list, name='sinhvien_list'),
    path('sinhvien/them/', views.sinhvien_create, name='sinhvien_create'),
    path('sinhvien/<int:pk>/capnhat/', views.sinhvien_update, name='sinhvien_update'),
    path('sinhvien/<int:pk>/xoa/', views.sinhvien_delete, name='sinhvien_delete'),

    # Giảng viên
    path('giangvien/', views.giangvien_list, name='giangvien_list'),
    path('giangvien/them/', views.giangvien_create, name='giangvien_create'),
    path('giangvien/<int:pk>/capnhat/', views.giangvien_update, name='giangvien_update'),
    path('giangvien/<int:pk>/xoa/', views.giangvien_delete, name='giangvien_delete'),
    # Các đường dẫn khác

    # URLs cho DeTai
    path('detai/', views.detai_list, name='detai_list'),
    path('detai/<int:pk>/update/', views.detai_update, name='detai_update'),
    path('detai/<int:pk>/delete/', views.detai_delete, name='detai_delete'),
    path('detai/add/', views.add_detai, name='add_detai'),

    # URLs cho DoAn
    path('doan/', views.doan_list, name='doan_list'),
    path('doan/<int:pk>/update/', views.doan_update, name='doan_update'),
    path('doan/<int:pk>/delete/', views.doan_delete, name='doan_delete'),
    path('doan/create/', views.doan_create, name='doan_create'),

    # URLs cho HoiDongCham
    path('hoi-dong/', views.hoidong_list, name='hoi_dong_list'),
    path('hoi-dong/create/', views.hoi_dong_create, name='hoi_dong_create'),
    path('hoi-dong/delete/<int:pk>/', views.hoi_dong_delete, name='hoi_dong_delete'),
    path('hoi-dong/update/<int:pk>/', views.hoi_dong_update, name='hoi_dong_update'),


    # URLs cho lichbaove
    
]