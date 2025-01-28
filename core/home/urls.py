from django.urls import path
from . import views

urlpatterns = [
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


    # URLs cho DoAn
    path('doan/', views.doan_list, name='doan_list'),
]