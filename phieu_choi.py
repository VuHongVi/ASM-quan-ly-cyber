def menu():
    while True:
        print('>> QUẢN LÝ PHIẾU CHƠI <<')
        print('+-----------------------+')
        print("| 1. Hiển thị danh sách phiếu chơi")
        print("| 2. Tìm kiếm/Lọc phiếu")
        print("| 3. Thêm mới phiếu chơi")
        print("| 4. Cập nhật thông tin phiếu chơi")
        print("| 5. Xóa phiếu chơi")
        print("| 6. Thống kê số phiếu chơi theo khách hàng")
        print("| 7. Tổng hợp dịch vụ sử dụng")
        print("| 8. Tìm kiếm phiếu chơi theo thời gian")
        print("| 9. Tính thời gian chơi")
        print("| 10. Tính doanh thu từ các dịch vụ")
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
                thong_ke_so_phieu()
            elif lua_chon == '7':
                tong_hop_dich_vu()
            elif lua_chon == '8':
                tim_phieu_theo_thoi_gian()
            elif lua_chon == '9':
                tinh_thoi_gian_choi()
            elif lua_chon == '10':
                tinh_doanh_thu()
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
    chuc_nang = "Hiển thị danh sách phiếu chơi"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tim_kiem():
    chuc_nang = "Tìm kiếm/Lọc phiếu"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def them_moi():
    xac_nhan("Bạn có chắc chắn muốn thêm mới máy tính không?")
    chuc_nang = "Thêm mới phiếu chơi"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def cap_nhat():
    xac_nhan("Bạn có chắc chắn muốn cập nhật thông tin cho máy?")
    chuc_nang = "Cập nhật thông tin phiếu chơi"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def xoa():
    xac_nhan("Bạn có chắc chắn muốn xóa máy?")
    chuc_nang = "Xóa phiếu chơi"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def thong_ke_so_phieu():
    chuc_nang = "Thống kê số phiếu chơi theo khách hàng"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tong_hop_dich_vu():
    chuc_nang = "Tổng hợp dịch vụ sử dụng"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tim_phieu_theo_thoi_gian():
    chuc_nang = "Tìm kiếm phiếu chơi theo thời gian"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tinh_thoi_gian_choi():
    chuc_nang = "Tính thời gian chơi"
    print(f'Chức năng {chuc_nang} sẽ sớm được cập nhật!')

def tinh_doanh_thu():
    chuc_nang = "Tính doanh thu từ các dịch vụ"
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