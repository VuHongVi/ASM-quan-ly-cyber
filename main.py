# main.py

import sys
import os
# Import các module từ package
from quan_ly_may_tinh import menu as may_tinh_menu
from quan_ly_may_tinh import validate
import phieu_choi
import khach_hang
import dich_vu

def press_any_key_to_continue():
    input("\nNhấn phím bất kỳ để tiếp tục...")

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình cho rõ ràng
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
            lua_chon = int(lua_chon)

            if not (1 <= lua_chon <= 5):
                raise ValueError("Lựa chọn phải là số nguyên từ 1 đến 5.")

            if lua_chon == 1:
                may_tinh_menu()
            elif lua_chon == 2:
                khach_hang.menu()
            elif lua_chon == 3:
                dich_vu.menu()
            elif lua_chon == 4:
                phieu_choi.menu()
            elif lua_chon == 5:
                confirm = validate.xac_nhan("Bạn có chắc chắn muốn thoát chương trình?")
                if confirm:
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")

            press_any_key_to_continue()  # Đợi người dùng nhấn phím để tiếp tục
        except ValueError as v:
            print(v)
            press_any_key_to_continue()  # Đợi người dùng nhấn phím trước khi quay lại menu
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")
            press_any_key_to_continue()  # Đợi người dùng nhấn phím trước khi quay lại menu

if __name__ == "__main__":
    main_menu()
