from decimal import Decimal, InvalidOperation
import os
import json
import validate

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

# Danh sách máy tính
danh_sach_may_tinh = []

# Đường dẫn file dữ liệu
DATA_FILE = "D:\FPT Polytechnic\DAT2011 - LẬP TRÌNH PYTHON\code\ASM-quan-ly-cyber/may_tinh.json"

def menu():
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
        print("| 11. THOÁT CHƯƠNG TRÌNH")
        print("+--------------------+")

        try:
            lua_chon = input("Nhập lựa chọn của bạn (từ 1 đến 11): ").strip()
            
            try:
                lua_chon = Decimal(lua_chon)
            except InvalidOperation:
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 11!")

            if lua_chon % 1 != 0 or not (1 <= int(lua_chon) <= 11):
                raise ValueError("Lựa chọn phải là số nguyên từ 1 đến 11.")

            lua_chon = int(lua_chon)

            if lua_chon == 1:
                hien_thi_danh_sach()
            elif lua_chon == 2:
                tim_kiem()
            elif lua_chon == 3:
                them_moi()
            elif lua_chon == 4:
                cap_nhat()
            elif lua_chon == 5:
                xoa()
            elif lua_chon == 6:
                sap_xep_theo_gia()
            elif lua_chon == 7:
                sap_xep_theo_tinh_trang()
            elif lua_chon == 8:
                sap_xep_theo_cau_hinh()
            elif lua_chon == 9:
                hien_thi_may_trong()
            elif lua_chon == 10:
                tinh_tong_gia_tri()
            elif lua_chon == 11:
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

def press_any_key_to_continue():
    input("\nNhấn phím bất kỳ để tiếp tục...")

# Lưu danh sách máy tính vào file
def luu_vao_file():
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump([may.to_dict() for may in danh_sach_may_tinh], file)
        print("Lưu dữ liệu vào file thành công.")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu: {e}")

# Đọc thông tin máy tính từ file
def doc_tu_file():
    global danh_sach_may_tinh
    # Kiểm tra nếu file chưa tồn tại, tạo file mới
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump([], file)  # Tạo một danh sách rỗng trong file
            print(f"File dữ liệu mới đã được tạo: {DATA_FILE}")
        except Exception as e:
            print(f"Lỗi khi tạo file dữ liệu mới: {e}")
            return  # Thoát hàm nếu gặp lỗi khi tạo file
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            danh_sach_may_tinh = [MayTinh.from_dict(may) for may in data]
        print("Đọc dữ liệu từ file thành công.")
    except json.JSONDecodeError:
        print("File dữ liệu không đúng định dạng.")
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu: {e}")


def hien_thi_danh_sach():
    doc_tu_file()  # Đọc dữ liệu từ file trước khi hiển thị
    if danh_sach_may_tinh:
        print("\nDanh sách máy tính:")
        for may in danh_sach_may_tinh:
            print(may)
    else:
        print("Hiện không có máy tính nào trong danh sách.")

def tim_kiem():
    doc_tu_file()  # Đọc dữ liệu từ file
    ma = input("Nhập mã máy tính cần tìm: ").strip()
    ket_qua = [may for may in danh_sach_may_tinh if may.ma == ma]
    if ket_qua:
        print("\nKết quả tìm kiếm:")
        for may in ket_qua:
            print(may)
    else:
        print("Không tìm thấy máy tính với mã đã nhập.")

def them_moi():
    doc_tu_file()  # Đọc dữ liệu từ file
    if validate.xac_nhan("Bạn có chắc chắn muốn thêm mới máy tính không?"):
        try:
            # Nhập mã máy tính với vòng lặp
            while True:
                try:
                    ma = validate.validate_ma(input("Nhập mã máy tính (mamayxxx): ").strip(), danh_sach_may_tinh)
                    break  # Thoát vòng lặp nếu mã hợp lệ
                except ValueError as e:
                    print(f"Lỗi: {e}. Vui lòng nhập lại.")

            # Nhập tình trạng với vòng lặp
            while True:
                try:
                    tinh_trang = validate.validate_tinh_trang(input("Nhập tình trạng máy tính (trong/dang_su_dung/bao_tri): ").strip())
                    break  # Thoát vòng lặp nếu tình trạng hợp lệ
                except ValueError as e:
                    print(f"Lỗi: {e}. Vui lòng nhập lại.")

            # Nhập vị trí với vòng lặp
            while True:
                try:
                    vi_tri = validate.validate_vi_tri(input("Nhập vị trí máy tính (Xxx, ví dụ A01): ").strip())
                    break  # Thoát vòng lặp nếu vị trí hợp lệ
                except ValueError as e:
                    print(f"Lỗi: {e}. Vui lòng nhập lại.")

            # Nhập giá với vòng lặp
            while True:
                try:
                    gia = validate.validate_gia(input("Nhập giá máy tính: ").strip())
                    break  # Thoát vòng lặp nếu giá hợp lệ
                except ValueError as e:
                    print(f"Lỗi: {e}. Vui lòng nhập lại.")

            # Nhập cấu hình với vòng lặp
            while True:
                try:
                    cau_hinh = validate.validate_cau_hinh(input("Nhập cấu hình máy tính: ").strip())
                    break  # Thoát vòng lặp nếu cấu hình hợp lệ
                except ValueError as e:
                    print(f"Lỗi: {e}. Vui lòng nhập lại.")

            # Tạo đối tượng máy tính và thêm vào danh sách
            may_tinh = MayTinh(ma, tinh_trang, vi_tri, gia, cau_hinh)
            danh_sach_may_tinh.append(may_tinh)
            luu_vao_file()  # Lưu dữ liệu vào file sau khi thêm mới
            print("Thêm máy tính mới thành công!")
        except Exception as e:
            print(f"Lỗi khi thêm máy tính: {e}")


def cap_nhat():
    doc_tu_file()  # Đọc dữ liệu từ file
    if validate.xac_nhan("Bạn có chắc chắn muốn cập nhật máy tính không?"):
        ma = input("Nhập mã máy tính cần cập nhật: ").strip()
        for may in danh_sach_may_tinh:
            if may.ma == ma:
                # Cập nhật tình trạng với vòng lặp
                while True:
                    try:
                        tinh_trang = input(f"Cập nhật tình trạng ({may.tinh_trang}) (trong/dang_su_dung/bao_tri): ").strip() or may.tinh_trang
                        tinh_trang = validate.validate_tinh_trang(tinh_trang)
                        break  # Thoát vòng lặp nếu tình trạng hợp lệ
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Cập nhật vị trí với vòng lặp
                while True:
                    try:
                        vi_tri = input(f"Cập nhật vị trí ({may.vi_tri}) (Xxx, ví dụ A01): ").strip() or may.vi_tri
                        vi_tri = validate.validate_vi_tri(vi_tri)
                        break  # Thoát vòng lặp nếu vị trí hợp lệ
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Cập nhật giá với vòng lặp
                while True:
                    try:
                        gia = input(f"Cập nhật giá ({may.gia}): ").strip() or may.gia
                        gia = validate.validate_gia(gia)
                        break  # Thoát vòng lặp nếu giá hợp lệ
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Cập nhật cấu hình với vòng lặp
                while True:
                    try:
                        cau_hinh = input(f"Cập nhật cấu hình ({may.cau_hinh}): ").strip() or may.cau_hinh
                        cau_hinh = validate.validate_cau_hinh(cau_hinh)
                        break  # Thoát vòng lặp nếu cấu hình hợp lệ
                    except ValueError as e:
                        print(f"Lỗi: {e}. Vui lòng nhập lại.")

                # Cập nhật thông tin máy tính sau khi đã xác thực
                may.tinh_trang = tinh_trang
                may.vi_tri = vi_tri
                may.gia = gia
                may.cau_hinh = cau_hinh

                luu_vao_file()  # Lưu dữ liệu vào file sau khi cập nhật
                print("Cập nhật thông tin máy tính thành công!")
                return
        print("Không tìm thấy máy tính với mã đã nhập.")

def xoa():
    doc_tu_file()  # Đọc dữ liệu từ file
    if validate.xac_nhan("Bạn có chắc chắn muốn xóa máy tính không?"):
        while True:
            try:
                # Nhập mã máy tính cần xóa
                ma = input("Nhập mã máy tính cần xóa: ").strip()
                
                # Kiểm tra mã có tồn tại trong danh sách không
                if any(may.ma == ma for may in danh_sach_may_tinh):
                    # Xác nhận xóa máy tính
                    global danh_sach_may_tinh
                    danh_sach_may_tinh = [may for may in danh_sach_may_tinh if may.ma != ma]
                    luu_vao_file()  # Lưu dữ liệu vào file sau khi xóa
                    print("Xóa máy tính thành công!")
                    break  # Thoát khỏi vòng lặp sau khi xóa thành công
                else:
                    print("Không tìm thấy máy tính với mã đã nhập. Vui lòng thử lại.")
            except Exception as e:
                print(f"Lỗi khi xóa máy tính: {e}")

def sap_xep_theo_gia():
    doc_tu_file()  # Đọc dữ liệu từ file
    danh_sach_may_tinh.sort(key=lambda x: x.gia)
    print("Danh sách máy tính đã được sắp xếp theo giá.")
    for may in danh_sach_may_tinh:
        print(may)

def sap_xep_theo_tinh_trang():
    doc_tu_file()  # Đọc dữ liệu từ file
    danh_sach_may_tinh.sort(key=lambda x: x.tinh_trang)
    print("Danh sách máy tính đã được sắp xếp theo tình trạng.")
    for may in danh_sach_may_tinh:
        print(may)

def sap_xep_theo_cau_hinh():
    doc_tu_file()  # Đọc dữ liệu từ file
    danh_sach_may_tinh.sort(key=lambda x: x.cau_hinh)
    print("Danh sách máy tính đã được sắp xếp theo cấu hình.")
    for may in danh_sach_may_tinh:
        print(may)

def hien_thi_may_trong():
    doc_tu_file()  # Đọc dữ liệu từ file
    may_trong = [may for may in danh_sach_may_tinh if may.tinh_trang.lower() == 'trong']
    if may_trong:
        print("\nCác máy còn trống:")
        for may in may_trong:
            print(may)
    else:
        print("Không có máy nào đang trống.")

def tinh_tong_gia_tri():
    doc_tu_file()  # Đọc dữ liệu từ file
    tong_gia_tri = sum(may.gia for may in danh_sach_may_tinh)
    print(f"Tổng giá trị tất cả máy tính: {tong_gia_tri}")


if __name__ == "__main__":
    menu()
