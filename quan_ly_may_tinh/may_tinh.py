from decimal import Decimal, InvalidOperation
import os
import json
# import validate
from . import validate
import dich_vu
import phieu_choi

# Lớp Máy Tính đại diện cho máy tính trong quán game
class MayTinh:
    def __init__(self, ma, tinh_trang, vi_tri, gia, cau_hinh):
        self.ma = ma
        self.tinh_trang = tinh_trang
        self.vi_tri = vi_tri
        self.gia = Decimal(gia)
        self.cau_hinh = cau_hinh

    def __str__(self):
        return f"Mã: {self.ma}, Tình trạng: {self.tinh_trang}, Vị trí: {self.vi_tri}, Giá: {self.gia}, Cấu hình: {self.cau_hinh}"

    def to_dict(self):
        return {
            "ma": self.ma,
            "tinh_trang": self.tinh_trang,
            "vi_tri": self.vi_tri,
            "gia": str(self.gia),
            "cau_hinh": self.cau_hinh
        }

    @staticmethod
    def from_dict(data):
        return MayTinh(data['ma'], data['tinh_trang'], data['vi_tri'], data['gia'], data['cau_hinh'])

# Lớp quản lý máy tính
class QuanLyMayTinh:
    def __init__(self, data_file):
        self.data_file = data_file
        self.danh_sach_may_tinh = []
        self.doc_tu_file()

    # Lưu danh sách máy tính vào file
    def luu_vao_file(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump([may.to_dict() for may in self.danh_sach_may_tinh], file)
            print("Lưu dữ liệu vào file thành công.")
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu: {e}")

    # Đọc thông tin máy tính từ file
    def doc_tu_file(self):  
        # Kiểm tra nếu file chưa tồn tại, tạo file mới
        if not os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'w') as file:
                    json.dump([], file)  # Tạo một danh sách rỗng trong file
                print(f"File dữ liệu mới đã được tạo: {self.data_file}")
            except Exception as e:
                print(f"Lỗi khi tạo file dữ liệu mới: {e}")
                return
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.danh_sach_may_tinh = [MayTinh.from_dict(may) for may in data]
            print("Đọc dữ liệu từ file thành công.")
        except json.JSONDecodeError:
            print("File dữ liệu không đúng định dạng.")
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu: {e}")

    # Các phương thức quản lý máy tính
    def hien_thi_danh_sach(self):
        if self.danh_sach_may_tinh:
            print("\nDanh sách máy tính:")
            for may in self.danh_sach_may_tinh:
                print(may)
        else:
            print("Hiện không có máy tính nào trong danh sách.")

    def tim_kiem(self):
        ma = input("Nhập mã máy tính cần tìm: ").strip()
        ket_qua = [may for may in self.danh_sach_may_tinh if may.ma == ma]
        if ket_qua:
            print("\nKết quả tìm kiếm:")
            for may in ket_qua:
                print(may)
        else:
            print("Không tìm thấy máy tính với mã đã nhập.")

    def them_moi(self):
        if validate.xac_nhan("Bạn có chắc chắn muốn thêm mới máy tính không?"):
            try:
                # Nhập mã máy tính với vòng lặp
                while True:
                    try:
                        ma = validate.validate_ma(
                            input("Nhập mã máy tính (mamayxxx): ").strip(),
                            self.danh_sach_may_tinh
                        )
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Nhập tình trạng với vòng lặp
                while True:
                    try:
                        tinh_trang = validate.validate_tinh_trang(
                            input("Nhập tình trạng máy tính (trong/dang_su_dung/bao_tri): ").strip()
                        )
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Nhập vị trí với vòng lặp
                while True:
                    try:
                        vi_tri = validate.validate_vi_tri(
                            input("Nhập vị trí máy tính (Xxxx, ví dụ A001): ").strip(),
                            self.danh_sach_may_tinh
                        )
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Nhập giá với vòng lặp
                while True:
                    try:
                        gia = validate.validate_gia(
                            input("Nhập giá máy tính: ").strip()
                        )
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Nhập cấu hình với vòng lặp
                while True:
                    try:
                        cau_hinh = validate.validate_cau_hinh(
                            input("Nhập cấu hình máy tính: ").strip()
                        )
                        break
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Hiển thị thông tin đã nhập để xác nhận lại
                print("\nThông tin máy tính bạn đã nhập:")
                print(f"Mã máy tính: {ma}")
                print(f"Tình trạng: {tinh_trang}")
                print(f"Vị trí: {vi_tri}")
                print(f"Giá: {gia}")
                print(f"Cấu hình: {cau_hinh}")

                # Xác nhận lần cuối trước khi lưu vào danh sách và file
                if validate.xac_nhan("Bạn có chắc chắn muốn lưu thông tin này không?"):
                    # Tạo đối tượng máy tính và thêm vào danh sách
                    may_tinh = MayTinh(ma, tinh_trang, vi_tri, gia, cau_hinh)
                    self.danh_sach_may_tinh.append(may_tinh)
                    self.luu_vao_file()
                    print("Thêm máy tính mới thành công!")
                else:
                    print("Hủy thao tác thêm mới máy tính.")
            except Exception as e:
                print(f"Lỗi khi thêm máy tính: {e}")

    def cap_nhat(self):
        if validate.xac_nhan("Bạn có chắc chắn muốn cập nhật máy tính không?"):
            ma = input("Nhập mã máy tính cần cập nhật: ").strip()
            for may in self.danh_sach_may_tinh:
                if may.ma == ma:
                    # Cập nhật thông tin
                    try:
                        # Cập nhật tình trạng
                        tinh_trang = input(f"Cập nhật tình trạng ({may.tinh_trang}) (trong/dang_su_dung/bao_tri). Nhấn Enter nếu không muốn thay đổi: ").strip() or may.tinh_trang
                        tinh_trang = validate.validate_tinh_trang(tinh_trang)

                        # Cập nhật vị trí
                        vi_tri = input(f"Cập nhật vị trí ({may.vi_tri}) (Xxxx, ví dụ A001). Nhấn Enter nếu không muốn thay đổi: ").strip() or may.vi_tri
                        vi_tri = validate.validate_vi_tri(vi_tri, self.danh_sach_may_tinh, ma_may_hien_tai=ma)

                        # Cập nhật giá
                        gia = input(f"Cập nhật giá ({may.gia}). Nhấn Enter nếu không muốn thay đổi: ").strip() or may.gia
                        gia = validate.validate_gia(gia)

                        # Cập nhật cấu hình
                        cau_hinh = input(f"Cập nhật cấu hình ({may.cau_hinh}). Nhấn Enter nếu không muốn thay đổi: ").strip() or may.cau_hinh
                        cau_hinh = validate.validate_cau_hinh(cau_hinh)
                    except ValueError as e:
                        print(f"Lỗi: {e}")
                        return

                    # Hiển thị thông tin đã cập nhật để xác nhận lại
                    print("\nThông tin máy tính sau khi cập nhật:")
                    print(f"Mã máy tính: {ma}")
                    print(f"Tình trạng: {tinh_trang}")
                    print(f"Vị trí: {vi_tri}")
                    print(f"Giá: {gia}")
                    print(f"Cấu hình: {cau_hinh}")

                    # Xác nhận lần cuối trước khi lưu vào danh sách và file
                    if validate.xac_nhan("Bạn có chắc chắn muốn lưu thay đổi này không?"):
                        may.tinh_trang = tinh_trang
                        may.vi_tri = vi_tri
                        may.gia = gia
                        may.cau_hinh = cau_hinh

                        self.luu_vao_file()
                        print("Cập nhật thông tin máy tính thành công!")
                    else:
                        print("Hủy thao tác cập nhật.")
                    return
            print("Không tìm thấy máy tính với mã đã nhập.")

    def xoa(self):
        if validate.xac_nhan("Bạn có chắc chắn muốn xóa máy tính không?"):
            ma = input("Nhập mã máy tính cần xóa: ").strip()
            may_can_xoa = next((may for may in self.danh_sach_may_tinh if may.ma == ma), None)
            if may_can_xoa:
                # Hiển thị thông tin máy tính cần xóa
                print("\nThông tin máy tính sẽ bị xóa:")
                print(f"Mã máy tính: {may_can_xoa.ma}")
                print(f"Tình trạng: {may_can_xoa.tinh_trang}")
                print(f"Vị trí: {may_can_xoa.vi_tri}")
                print(f"Giá: {may_can_xoa.gia}")
                print(f"Cấu hình: {may_can_xoa.cau_hinh}")

                # Xác nhận xóa máy tính
                if validate.xac_nhan("Bạn có chắc chắn muốn xóa máy tính này không?"):
                    self.danh_sach_may_tinh.remove(may_can_xoa)
                    self.luu_vao_file()
                    print("Xóa máy tính thành công!")
                else:
                    print("Hủy thao tác xóa.")
            else:
                print("Không tìm thấy máy tính với mã đã nhập.")

    def sap_xep_theo_gia(self):
        self.danh_sach_may_tinh.sort(key=lambda x: x.gia)
        print("Danh sách máy tính đã được sắp xếp theo giá.")
        for may in self.danh_sach_may_tinh:
            print(may)

    def sap_xep_theo_tinh_trang(self):
        self.danh_sach_may_tinh.sort(key=lambda x: x.tinh_trang)
        print("Danh sách máy tính đã được sắp xếp theo tình trạng.")
        for may in self.danh_sach_may_tinh:
            print(may)

    def sap_xep_theo_cau_hinh(self):
        self.danh_sach_may_tinh.sort(key=lambda x: x.cau_hinh)
        print("Danh sách máy tính đã được sắp xếp theo cấu hình.")
        for may in self.danh_sach_may_tinh:
            print(may)

    def hien_thi_may_trong(self):
        may_trong = [may for may in self.danh_sach_may_tinh if may.tinh_trang.lower() == 'trong']
        if may_trong:
            print("\nCác máy còn trống:")
            for may in may_trong:
                print(may)
        else:
            print("Không có máy nào đang trống.")

    def tinh_tong_gia_tri(self):
        tong_gia_tri = sum(may.gia for may in self.danh_sach_may_tinh)
        print(f"Tổng giá trị tất cả máy tính: {tong_gia_tri}")

def press_any_key_to_continue():
    input("\nNhấn phím bất kỳ để tiếp tục...")

def menu():
    # Đường dẫn file dữ liệu
    DATA_FILE = r"D:\FPT Polytechnic\DAT2011 - LẬP TRÌNH PYTHON\code\ASM-quan-ly-cyber\quan_ly_may_tinh\may_tinh.json"
    quan_ly = QuanLyMayTinh(DATA_FILE)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
        print("| 11. Hiển thị danh sách phiếu chơi")
        print("| 12. THOÁT CHƯƠNG TRÌNH")
        print("+--------------------+")

        try:
            lua_chon = input("Nhập lựa chọn của bạn (từ 1 đến 12): ").strip()
            try:
                lua_chon = Decimal(lua_chon)
            except InvalidOperation:
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 12!")

            if lua_chon % 1 != 0 or not (1 <= int(lua_chon) <= 12):
                raise ValueError("Lựa chọn phải là số nguyên từ 1 đến 12.")

            if lua_chon == 1:
                quan_ly.hien_thi_danh_sach()
            elif lua_chon == 2:
                quan_ly.tim_kiem()
            elif lua_chon == 3:
                quan_ly.them_moi()
            elif lua_chon == 4:
                quan_ly.cap_nhat()
            elif lua_chon == 5:
                quan_ly.xoa()
            elif lua_chon == 6:
                quan_ly.sap_xep_theo_gia()
            elif lua_chon == 7:
                quan_ly.sap_xep_theo_tinh_trang()
            elif lua_chon == 8:
                quan_ly.sap_xep_theo_cau_hinh()
            elif lua_chon == 9:
                quan_ly.hien_thi_may_trong()
            elif lua_chon == 10:
                quan_ly.tinh_tong_gia_tri()
            elif lua_chon == 11:
                phieu_choi.hien_thi_danh_sach()
            elif lua_chon == 12:
                if validate.xac_nhan("Bạn có chắc chắn muốn thoát chương trình?"):
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")
            press_any_key_to_continue()
        except ValueError as v:
            print(v)
            press_any_key_to_continue()
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")
            press_any_key_to_continue()

if __name__ == "__main__":
    menu()
