from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import SinhVien
from .forms import SinhVienForm  # Form do bạn tự định nghĩa
from .models import GiangVien
from .forms import GiangVienForm  # Form do bạn tự định nghĩa


# Hiển thị danh sách sinh viên
def sinhvien_list(request):
    sinh_vien_list = SinhVien.objects.all()
    return render(request, 'sinhvien_list.html', {'sinh_vien_list': sinh_vien_list})

# Thêm mới sinh viên
def sinhvien_create(request):
    if request.method == "POST":
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sinhvien_list')
    else:
        form = SinhVienForm()
    return render(request, 'sinhvien_form.html', {'form': form})

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
    return render(request, 'sinhvien_form.html', {'form': form})

# Xóa sinh viên
def sinhvien_delete(request, pk):
    sinhvien = get_object_or_404(SinhVien, pk=pk)
    if request.method == "POST":
        sinhvien.delete()
        return redirect('sinhvien_list')
    return render(request, 'sinhvien_confirm_delete.html', {'sinhvien': sinhvien})

# Hiển thị danh sách giảng viên
def giangvien_list(request):
    giang_vien_list = GiangVien.objects.all()
    return render(request, 'giangvien_list.html', {'giang_vien_list': giang_vien_list})

# Thêm mới giảng viên
def giangvien_create(request):
    if request.method == "POST":
        form = GiangVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giangvien_list')
    else:
        form = GiangVienForm()
    return render(request, 'giangvien_form.html', {'form': form})

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
    return render(request, 'giangvien_form.html', {'form': form})

# Xóa giảng viên
def giangvien_delete(request, pk):
    giangvien = get_object_or_404(GiangVien, pk=pk)
    if request.method == "POST":
        giangvien.delete()
        return redirect('giangvien_list')
    return render(request, 'giangvien_confirm_delete.html', {'giangvien': giangvien})