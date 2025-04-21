from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *  # Form do bạn tự định nghĩa
from .models import GiangVien
from .forms import GiangVienForm  # Form do bạn tự định nghĩa
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
# Thêm đề tài 
def add_detai(request):
    if request.method == 'POST':
        form = DeTaiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đề tài mới đã được thêm thành công!')
            return redirect('detai_list')  # Chuyển hướng về trang danh sách đề tài
        else:
            messages.error(request, 'Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.')
    else:
        form = DeTaiForm()
    return render(request, 'phancong/add_detai.html', {'form': form})
# Thêm đồ án
def doan_create(request):
    if request.method == 'POST':
        form = DoAnForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('doan_list')  # Chuyển hướng về danh sách đồ án sau khi thêm
            except ValueError as e:
                form.add_error(None, str(e))  # Hiển thị lỗi nếu có
    else:
        form = DoAnForm()

    return render(request, 'phancong/doan_create.html', {'form': form})
# Hiện thị đồ án
def doan_list(request):
    query = request.GET.get('q')  # Lấy từ khóa tìm kiếm từ URL
    doan = DoAn.objects.select_related('de_tai', 'sinh_vien', 'giang_vien_huong_dan')
    if query:
        doan = doan.filter(
            sinh_vien__ho_ten__icontains=query
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
    return render(request, 'phancong/doan_form.html', {'form': form})

# Xóa đồ án
def doan_delete(request, pk):
    doan = get_object_or_404(DoAn, pk=pk)
    if request.method == 'POST':
        doan.delete()
        return redirect('doan_list')
    return render(request, 'phancong/doan_confirm_delete.html', {'object': doan})


# Đăng nhập
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("sinhvien_list")  # Điều hướng sau khi đăng nhập thành công
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")

    return render(request, "login/login.html")

def hoidong_list(request):
    hoi_dong = HoiDongCham.objects.all()
    return render(request, 'hoidongchamthi/list.html', {'hoi_dong': hoi_dong})

def hoi_dong_create(request):
    if request.method == "POST":
        form = HoiDongChamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hoi_dong_list')
    else:
        form = HoiDongChamForm()
    return render(request, 'hoidongchamthi/form.html', {'form': form})


# Xóa hội đồng
def hoi_dong_delete(request, pk):
    hoi_dong = get_object_or_404(HoiDongCham, pk=pk)
    hoi_dong.delete()
    return redirect('hoi_dong_list')
# Sửa hội đồng
def hoi_dong_update(request, pk):
    hoi_dong = get_object_or_404(HoiDongCham, pk=pk)
    if request.method == "POST":
        form = HoiDongChamForm(request.POST, instance=hoi_dong)
        if form.is_valid():
            form.save()
            return redirect('hoi_dong_list')
    else:
        form = HoiDongChamForm(instance=hoi_dong)
    return render(request, 'hoidongchamthi/form.html', {'form': form})