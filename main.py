import may_tinh
import phieu_choi
import khach_hang
import dich_vu

def main_menu():
    while True:
        print("\n>>== MENU CHÍNH ==<<")
        print("+------------------+")
        print("1. Quản lý máy tính")
        print("2. Quản lý khách hàng")
        print("3. Quản lý dịch vụ")
        print("4. Quản lý phiếu chơi")
        print("5. Thoát chương trình")
        print("+------------------+")
        
        try:
            lua_chon = input("Nhập lựa chọn của bạn (từ 1 đến 5): ").strip()
    
            if not lua_chon.isdigit() or not (1 <= int(lua_chon) <= 5):
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng nhập số nguyên từ 1 đến 5!\n(Không nhập theo dạng số thực có dấu phẩy động!)")

            lua_chon = int(lua_chon)
            if lua_chon == 1:
                may_tinh.menu()
            elif lua_chon == 2:
                try:
                    khach_hang.menu()
                except Exception as e:
                    print(f"Có lỗi: {e}. Hãy thử lại!")
            elif lua_chon == 3:
                try:
                    dich_vu.menu()
                except Exception as e:
                    print(f"Có lỗi: {e}. Hãy thử lại!")
            elif lua_chon == 4:
                try:
                    phieu_choi.menu()
                except Exception as e:
                    print(f"Có lỗi: {e}. Hãy thử lại!")
            elif lua_chon == 5:
                confirm = may_tinh.xac_nhan("Bạn có chắc chắn muốn thoát chương trình?")
                if confirm:
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")
        except ValueError as v:
            print(v)
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
