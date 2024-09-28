def menu():
    while True:
        print('>> QUẢN LÝ KHÁCH HÀNG <<')
        print('+-----------------------+')
        print("| 1. Hiển thị danh sách khách hàng")
        print("| 2. Tìm kiếm/Lọc khách hàng")
        print("| 3. Thêm mới khách hàng")
        print("| 4. Cập nhật thông tin khách hàng")
        print("| 5. Xóa khách hàng")
        print("| 6. Thống kê số khách hàng theo loại thẻ thành viên")
        print("| 7. Tìm kiếm khách hàng theo thẻ thành viên")
        print("| 8. Hiển thị thông tin chi tiết khách hàng ")
        print("| 9. Gửi email tới khách hàng")
        print("| 10. Tính tổng chi tiêu khách hàng")
        print("| 11. THOÁT CHƯƠNG TRÌNH")
        print("+--------------------+")

        try:
            lua_chon = input("Nhập lựa chọn của bạn: ").strip()
            
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
                thong_ke_so_khach_hang_theo_the()
            elif lua_chon == '7':
                tim_khach_hang_theo_the()
            elif lua_chon == '8':
                hien_thi_chi_tiet_khach_hang()
            elif lua_chon == '9':
                gui_email()
            elif lua_chon == '10':
                tinh_tong_chi_tieu()
            elif lua_chon == '11':
                if xac_nhan("Bạn có chắc chắn muốn thoát chương trình?"):
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

def hien_thi_danh_sach():
    print(f'Chức năng hiển thị danh sách sẽ sớm được cập nhật!')

def tim_kiem():
    print(f'Chức năng tìm kiếm/ lọc khách hàng sẽ sớm được cập nhật!')

def them_moi():
    xac_nhan("Bạn có chắc chắn muốn thêm mới tên, mã, email, sđt khách hàng không?")
    print(f'Chức năng thêm mới khách hàng sẽ sớm được cập nhật!')

def cap_nhat():
    xac_nhan("Bạn có chắc chắn muốn cập nhật thông tin cho khách hàng?")
    print(f'Chức năng cập nhật khách hàng sẽ sớm được cập nhật!')

def xoa():
    xac_nhan("Bạn có chắc chắn muốn xóa khách hàng dựa trên mã?")
    print(f'Chức năng xóa khách hàng sẽ sớm được cập nhật!')

def thong_ke_so_khach_hang_theo_the():
    print(f'Chức năng thống kê khách hàng sẽ sớm được cập nhật!')

def hien_thi_chi_tiet_khach_hang():
    print(f'Chức năng tìm kiếm khách hàng sẽ sớm được cập nhật!')

def tim_khach_hang_theo_the():
    print(f'Chức năng tìm kiếm khách hàng sẽ sớm được cập nhật!')

def gui_email():
    print(f'Chức năng tìm kiếm khách hàng sẽ sớm được cập nhật!')

def tinh_tong_chi_tieu():
    print(f'Chức năng tìm kiếm khách hàng sẽ sớm được cập nhật!')

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