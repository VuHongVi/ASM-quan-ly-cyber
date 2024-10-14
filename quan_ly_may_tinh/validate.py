from decimal import Decimal, InvalidOperation
import re

def validate_ma(ma, danh_sach_may_tinh):
    """Kiểm tra mã máy tính: không được rỗng, có định dạng hợp lệ và duy nhất."""
    ma = ma.strip()
    if not ma:
        raise ValueError("Mã máy tính không được để trống.")
    if not re.match(r"^mamay\d{3}$", ma):
        raise ValueError("Mã máy tính phải có định dạng 'mamayxxx' với xxx là các số từ 001 đến 999.")
    number_part = int(ma[-3:])
    if not (1 <= number_part <= 999):
        raise ValueError("Phần số của mã máy tính phải nằm trong khoảng từ 001 đến 999.")
    if any(may.ma == ma for may in danh_sach_may_tinh):
        raise ValueError("Mã máy tính đã tồn tại. Vui lòng nhập mã khác.")
    return ma

def validate_tinh_trang(tinh_trang):
    """Kiểm tra tình trạng máy tính: phải là một trong các giá trị hợp lệ."""
    tinh_trang_hop_le = ['trong', 'dang_su_dung', 'bao_tri']
    tinh_trang = tinh_trang.strip().lower()
    if tinh_trang not in tinh_trang_hop_le:
        raise ValueError(f"Tình trạng máy tính không hợp lệ. Chỉ chấp nhận: {', '.join(tinh_trang_hop_le)}.")
    return tinh_trang

def validate_vi_tri(vi_tri):
    """Kiểm tra vị trí: phải có định dạng hợp lệ."""
    vi_tri = vi_tri.strip()
    if not re.match(r"^[A-Za-z]\d{2}$", vi_tri):
        raise ValueError("Vị trí phải có định dạng 'Xxx', với 'X' là một chữ cái và 'xx' là hai chữ số.")
    return vi_tri

def validate_gia(gia):
    """Kiểm tra giá trị giá: phải là một số dương và trong khoảng hợp lệ."""
    try:
        gia_value = Decimal(gia)
        if gia_value <= 0:
            raise ValueError("Giá máy tính phải lớn hơn 0.")
        if gia_value > 1_000_000_000:
            raise ValueError("Giá máy tính không được vượt quá 1 tỷ.")
    except InvalidOperation:
        raise ValueError("Giá máy tính phải là một số hợp lệ.")
    return gia_value

def validate_cau_hinh(cau_hinh):
    """Kiểm tra cấu hình máy tính: không được rỗng."""
    if not cau_hinh.strip():
        raise ValueError("Cấu hình máy tính không được để trống.")
    return cau_hinh.strip()

def xac_nhan(message):
    while True:
        try:
            xac_nhan = input(f"{message} (Y/N): ").strip().lower()
            if xac_nhan == 'y':
                return True
            elif xac_nhan == 'n':
                return False
            else:
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng nhập Y hoặc N.")
        except ValueError as ve:
            print(ve)
