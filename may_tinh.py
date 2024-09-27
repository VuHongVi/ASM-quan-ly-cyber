def menu():
    while True:
        print(">> QUẢN LÝ MÁY TÍNH <<")
        print("+--------------------+")
        print("| 1. Hiển thị danh sách máy tính")
        print("| 2. Tìm kiếm/Lọc máy tính")
        print("| 3. Thêm mới máy tính")
        print("| 4. Cập nhật thông tin máy tính")
        print("| 5. Xóa máy tính")
        print("| 6. Sắp xếp máy tính theo giá")
        print("| 7. Sắp xếp máy tính theo tình trạng")
        print("| 8. Sắp xếp máy tính theo cấu hình")
        print("| 9. Hiển thị các máy còn trống")
        print("| 10. Tính tổng giá trị tất cả máy tính")
        print("| 11. THOÁT CHƯƠNG TRÌNH")
        print("+--------------------+")

        try:
            lua_chon = input("Nhập lựa chọn của bạn (từ 1 đến 11): ").strip()

            if lua_chon == '1':
                hien_thi_danh_sach()
            elif lua_chon == '2':
                tim_kiem()
            elif lua_chon == '3':
                them_moi()
            elif lua_chon == '4':
                cap_nhat()
            elif lua_chon == '5':
                xoa()
            elif lua_chon == '6':
                sap_xep_theo_gia()
            elif lua_chon == '7':
                sap_xep_theo_tinh_trang()
            elif lua_chon == '8':
                sap_xep_theo_cau_hinh()
            elif lua_chon == '9':
                hien_thi_may_trong()
            elif lua_chon == '10':
                tinh_tong_gia_tri()
            elif lua_chon == '11':
                if xac_nhan("Bạn có chắc chắn muốn thoát chương trình?"):
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại. Hãy nhập số từ 1 đến 11!")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

def hien_thi_danh_sach():
    chuc_nang = "hiển thị danh sách máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tim_kiem():
    chuc_nang = "tìm kiếm/Lọc máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def them_moi():
    xac_nhan("Bạn có chắc chắn muốn thêm mới máy tính không?")
    chuc_nang = "thêm mới máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def cap_nhat():
    xac_nhan("Bạn có chắc chắn muốn cập nhật thông tin cho máy?")
    chuc_nang = "cập nhật thông tin máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def xoa():
    xac_nhan("Bạn có chắc chắn muốn xóa máy?")
    chuc_nang = "xóa máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def sap_xep_theo_gia():
    chuc_nang = "sắp xếp máy tính theo giá"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def sap_xep_theo_tinh_trang():
    chuc_nang = "sắp xếp máy tính theo tình trạng"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def hien_thi_may_trong():
    chuc_nang = "hiển thị máy trống"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tinh_tong_gia_tri():
    chuc_nang = "tính tổng giá trị tất cả máy tính"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def sap_xep_theo_cau_hinh():
    chuc_nang = "sắp xếp máy tính theo cấu hình"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def xac_nhan( message):
    while True:
        try:
            xac_nhan = input(f"{message} (Y/N): ").strip().lower()
            if xac_nhan == 'y':
                return True
            elif xac_nhan == 'n':
                return False
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập Y hoặc N.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

if __name__ == "__main__":
    menu()
