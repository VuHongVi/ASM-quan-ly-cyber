import may_tinh
import phieu_choi
import khach_hang
import dich_vu
from decimal import Decimal, InvalidOperation
import os

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

            # Cố gắng chuyển đổi giá trị nhập vào thành Decimal
            try:
                lua_chon = Decimal(lua_chon)
            except InvalidOperation:
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")

            # Kiểm tra xem giá trị đã nhập có phải là số nguyên (sau khi làm tròn)
            if lua_chon % 1 != 0 or not (1 <= int(lua_chon) <= 5):
                raise ValueError("Lựa chọn phải là số nguyên từ 1 đến 5.")

            lua_chon = int(lua_chon)  # Chuyển đổi thành số nguyên sau khi kiểm tra

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
                confirm = may_tinh.xac_nhan("Bạn có chắc chắn muốn thoát chương trình? (y/n): ")
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
