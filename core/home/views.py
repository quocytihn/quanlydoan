from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *  # Form do bạn tự định nghĩa
from .models import GiangVien
from .forms import GiangVienForm  # Form do bạn tự định nghĩa


# Hiển thị danh sách sinh viên
def sinhvien_list(request):
    sinh_vien_list = SinhVien.objects.all()
    return render(request, 'quanly/sinhvien_list.html', {'sinh_vien_list': sinh_vien_list})

# Thêm mới sinh viên
def sinhvien_create(request):
    if request.method == "POST":
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sinhvien_list')
    else:
        form = SinhVienForm()
    return render(request, 'quanly/sinhvien_form.html', {'form': form})

# Cập nhật thông tin sinh viên
def sinhvien_update(request, pk):
    sinhvien = get_object_or_404(SinhVien, pk=pk)
    if request.method == "POST":
        form = SinhVienForm(request.POST, instance=sinhvien)
        if form.is_valid():
            form.save()
            return redirect('sinhvien_list')
    else:
        form = SinhVienForm(instance=sinhvien)
    return render(request, 'quanly/sinhvien_form.html', {'form': form})

# Xóa sinh viên
def sinhvien_delete(request, pk):
    sinhvien = get_object_or_404(SinhVien, pk=pk)
    if request.method == "POST":
        sinhvien.delete()
        return redirect('sinhvien_list')
    return render(request, 'quanly/sinhvien_confirm_delete.html', {'sinhvien': sinhvien})

# Hiển thị danh sách giảng viên
def giangvien_list(request):
    giang_vien_list = GiangVien.objects.all()
    return render(request, 'quanly/giangvien_list.html', {'giang_vien_list': giang_vien_list})

# Thêm mới giảng viên
def giangvien_create(request):
    if request.method == "POST":
        form = GiangVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giangvien_list')
    else:
        form = GiangVienForm()
    return render(request, 'quanly/giangvien_form.html', {'form': form})

# Cập nhật thông tin giảng viên
def giangvien_update(request, pk):
    giangvien = get_object_or_404(GiangVien, pk=pk)
    if request.method == "POST":
        form = GiangVienForm(request.POST, instance=giangvien)
        if form.is_valid():
            form.save()
            return redirect('giangvien_list')
    else:
        form = GiangVienForm(instance=giangvien)
    return render(request, 'quanly/giangvien_form.html', {'form': form})

# Xóa giảng viên
def giangvien_delete(request, pk):
    giangvien = get_object_or_404(GiangVien, pk=pk)
    if request.method == "POST":
        giangvien.delete()
        return redirect('giangvien_list')
    return render(request, 'quanly/giangvien_confirm_delete.html', {'giangvien': giangvien})

def detai_list(request):
    query = request.GET.get('q')  # Lấy từ khóa tìm kiếm từ URL
    detai = DeTai.objects.all()
    if query:
        detai = detai.filter(ma_de_tai__icontains=query) | detai.filter(ten_de_tai__icontains=query)
    return render(request, 'phancong/detai_list.html', {'detai': detai, 'query': query})
# Sửa đề tài
def detai_update(request, pk):
    detai = get_object_or_404(DeTai, pk=pk)
    if request.method == 'POST':
        form = DeTaiForm(request.POST, instance=detai)
        if form.is_valid():
            form.save()
            return redirect('detai_list')
    else:
        form = DeTaiForm(instance=detai)
    return render(request, 'phancong/detai_form.html', {'form': form})

# Xóa đề tài
def detai_delete(request, pk):
    detai = get_object_or_404(DeTai, pk=pk)
    if request.method == 'POST':
        detai.delete()
        return redirect('detai_list')
    return render(request, 'phancong/detai_confirm_delete.html', {'object': detai})


def doan_list(request):
    query = request.GET.get('q')  # Lấy từ khóa tìm kiếm từ URL
    doan = DoAn.objects.select_related('de_tai', 'sinh_vien', 'giang_vien_huong_dan')
    if query:
        doan = doan.filter(
            sinh_vien__ten__icontains=query
        ) | doan.filter(de_tai__ma_de_tai__icontains=query)
    return render(request, 'phancong/doan_list.html', {'doan': doan, 'query': query})

# Sửa đồ án
def doan_update(request, pk):
    doan = get_object_or_404(DoAn, pk=pk)
    if request.method == 'POST':
        form = DoAnForm(request.POST, instance=doan)
        if form.is_valid():
            form.save()
            return redirect('doan_list')
    else:
        form = DoAnForm(instance=doan)
    return render(request, 'doan_form.html', {'form': form})

# Xóa đồ án
def doan_delete(request, pk):
    doan = get_object_or_404(DoAn, pk=pk)
    if request.method == 'POST':
        doan.delete()
        return redirect('doan_list')
    return render(request, 'doan_confirm_delete.html', {'object': doan})
