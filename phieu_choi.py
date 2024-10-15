import json
from datetime import datetime, timedelta
from collections import Counter
import re

class PhieuChoi:
    def __init__(self, ma_phieu, khach_hang, may_tinh, gio_bat_dau, gio_ket_thuc, dich_vu):
        self.ma_phieu = ma_phieu
        self.khach_hang = khach_hang
        self.may_tinh = may_tinh
        self.gio_bat_dau = gio_bat_dau
        self.gio_ket_thuc = gio_ket_thuc
        self.dich_vu = dich_vu
    def __str__(self):
        return f'Ma phieu: {self.ma_phieu}, Khách hàng: {self.khach_hang}, Máy tính: {self.may_tinh}, Giờ bắt đầu: {self.gio_bat_dau}, Giờ kết thúc: {self.gio_ket_thuc}, Dịch vụ: {self.dich_vu}'
    def to_dict(self):
        return{
            "ma_phieu": self.ma_phieu,
            "khach_hang": self.khach_hang,
            "may_tinh": self.may_tinh,
            "gio_bat_dau": self.gio_bat_dau,
            "gio_ket_thuc": self.gio_ket_thuc,
            "dich_vu": self.dich_vu
        }
    @staticmethod
    def from_dict(data):
        return PhieuChoi(data['ma_phieu'], data['khach_hang'], data['may_tinh'], data['gio_bat_dau'], data['gio_ket_thuc'], data['dich_vu'])

phieu_choi = []

File_path = r"D:\FPT Polytechnic\DAT2011 - LẬP TRÌNH PYTHON\code\ASM-quan-ly-cyber\phieu_choi.json"

def menu():
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
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
        print("| 10. Thống kê sử dụng dịch vụ theo giờ cao điểm")
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
                thong_ke_gio_cao_diem()
            elif lua_chon == '11':
                if xac_nhan("Bạn có chắc chắn muốn thoát chương trình?"):
                    print("Đã thoát chương trình...")
                    break
                else:
                    print("Hủy thao tác thoát.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1-11!")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

# Đọc dữ liệu từ file
def doc_du_lieu_tu_file():
    try:
        with open(File_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Lưu dữ liệu vào file
def luu_du_lieu_vao_file():
    with open(File_path, 'w') as file:
        json.dump(phieu_choi, file, indent=4)

phieu_choi = doc_du_lieu_tu_file()

# Hiển thị danh sách phiếu chơi 
def hien_thi_danh_sach():
    # phieu_choi = doc_du_lieu_tu_file()
    if not phieu_choi:
        print("Danh sách phiếu chơi trống.")
    else:
        print("|         DANH SÁCH PHIẾU CHƠI           |")
        for phieu in phieu_choi:
            print(f" Mã phiếu    : {phieu['ma_phieu']}")
            print(f" Khách hàng  : {phieu['khach_hang']}")
            print(f" Máy tính      : {phieu['may_tinh']}")
            print(f" Giờ bắt đầu : {phieu['gio_bat_dau']}")
            print(f" Giờ kết thúc: {phieu['gio_ket_thuc']}")
            print(f" Dịch vụ     : {phieu['dich_vu']}")
            print("+----------------------------------------+")

# Tìm kiếm phiếu chơi theo mã phiếu
def tim_kiem():
    ma = input("Nhập mã phiếu: ").strip()
    ket_qua = [phieu for phieu in phieu_choi if phieu['ma_phieu'] == int(ma)]
    
    if ket_qua:
        print("|          KẾT QUẢ TÌM KIẾM           |")
        for phieu in ket_qua:
            print(phieu)
    else:
        print('Không tìm thấy phiếu nào với mã đã nhập.')

def them_moi():
    try:
        ma_phieu = int(input("Nhập mã phiếu: ").strip())
        
        # Kiểm tra mã phiếu không được trùng
        if any(p['ma_phieu'] == ma_phieu for p in phieu_choi):
            print("Mã phiếu đã tồn tại. Vui lòng nhập mã khác.")
            return
        
        khach_hang = input("Nhập tên khách hàng: ").strip()

        # Nhập số máy
        may_tinh = input("Nhập số máy: ").strip()
        if not may_tinh.isdigit() or int(may_tinh) <= 0:
            print("Số máy không hợp lệ. Vui lòng nhập số nguyên dương.")
            return

        # Kiểm tra định dạng ngày tháng với regex
        regex = r"^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}$"

        # Nhập giờ bắt đầu
        gio_bat_dau = input("Nhập giờ bắt đầu (yyyy-mm-dd HH:MM): ").strip()
        if not re.match(regex, gio_bat_dau):
            print("Giờ bắt đầu không đúng định dạng. Vui lòng nhập lại.")
            return

        # Nhập giờ kết thúc
        gio_ket_thuc = input("Nhập giờ kết thúc (yyyy-mm-dd HH:MM): ").strip()
        if not re.match(regex, gio_ket_thuc):
            print("Giờ kết thúc không đúng định dạng. Vui lòng nhập lại.")
            return
        
        # Chuyển đổi giờ bắt đầu và giờ kết thúc sang datetime để kiểm tra logic thời gian
        try:
            gio_bat_dau_dt = datetime.strptime(gio_bat_dau, "%Y-%m-%d %H:%M")
            gio_ket_thuc_dt = datetime.strptime(gio_ket_thuc, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Định dạng thời gian không hợp lệ.")
            return
        
        if gio_bat_dau_dt >= gio_ket_thuc_dt:
            print("Giờ bắt đầu phải nhỏ hơn giờ kết thúc.")
            return

        # Kiểm tra số máy không được trùng thời gian với các phiếu khác
        for phieu in phieu_choi:
            if phieu['may_tinh'] == int(may_tinh):
                phieu_gio_bat_dau_dt = datetime.strptime(phieu['gio_bat_dau'], "%Y-%m-%d %H:%M")
                phieu_gio_ket_thuc_dt = datetime.strptime(phieu['gio_ket_thuc'], "%Y-%m-%d %H:%M")

                if (gio_bat_dau_dt < phieu_gio_ket_thuc_dt and gio_ket_thuc_dt > phieu_gio_bat_dau_dt):
                    print("Số máy này đã được sử dụng trong khoảng thời gian đã nhập. Vui lòng chọn thời gian khác.")
                    return

        dich_vu = input("Nhập dịch vụ: ").strip()

        # Thêm phiếu chơi mới vào danh sách
        phieu_moi = {
            'ma_phieu': ma_phieu,
            'khach_hang': khach_hang,
            'may_tinh': int(may_tinh),
            'gio_bat_dau': gio_bat_dau,
            'gio_ket_thuc': gio_ket_thuc,
            'dich_vu': dich_vu
        }
        phieu_choi.append(phieu_moi)

        # Lưu dữ liệu vào file
        luu_du_lieu_vao_file()
        print("Đã thêm phiếu chơi thành công!")

    except ValueError:
        print("Lỗi: Vui lòng nhập mã phiếu và số máy là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")


def cap_nhat():
    try:
        ma_phieu = int(input("Nhập mã phiếu cần cập nhật: ").strip())

        # Tìm phiếu chơi theo mã
        phieu = next((p for p in phieu_choi if p['ma_phieu'] == ma_phieu), None)

        if phieu is None:
            print("Không tìm thấy phiếu chơi với mã này.")
            return

        print(f"Các thông tin hiện tại của phiếu chơi (mã {ma_phieu}):")
        print(f"Khách hàng: {phieu['khach_hang']}")
        print(f"Máy tính: {phieu['may_tinh']}")
        print(f"Giờ bắt đầu: {phieu['gio_bat_dau']}")
        print(f"Giờ kết thúc: {phieu['gio_ket_thuc']}")
        print(f"Dịch vụ: {phieu['dich_vu']}")

        # Nhập mã phiếu mới
        ma_phieu_moi = input("Nhập mã phiếu mới: ").strip()
        if ma_phieu_moi:
            ma_phieu_moi = int(ma_phieu_moi)
            # Kiểm tra mã phiếu mới có bị trùng hay không
            if any(p['ma_phieu'] == ma_phieu_moi and p['ma_phieu'] != ma_phieu for p in phieu_choi):
                print("Mã phiếu đã tồn tại. Vui lòng nhập mã khác.")
                return
        else:
            ma_phieu_moi = ma_phieu  # Giữ nguyên mã phiếu hiện tại nếu không nhập mới

        # Nhập các thông tin khác và kiểm tra hợp lệ
        khach_hang = input("Nhập tên khách hàng mới: ").strip()
        may_tinh = input("Nhập số máy mới: ").strip()
        if may_tinh and (not may_tinh.isdigit() or int(may_tinh) <= 0):
            print("Số máy không hợp lệ. Vui lòng nhập số nguyên dương.")
            return

        # Kiểm tra định dạng ngày tháng với regex
        regex = r"^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}$"

        # Nhập giờ bắt đầu mới
        gio_bat_dau = input("Nhập giờ bắt đầu mới (yyyy-mm-dd HH:MM): ").strip()
        if gio_bat_dau and not re.match(regex, gio_bat_dau):
            print("Giờ bắt đầu không đúng định dạng. Vui lòng nhập lại.")
            return

        # Nhập giờ kết thúc mới
        gio_ket_thuc = input("Nhập giờ kết thúc mới (yyyy-mm-dd HH:MM): ").strip()
        if gio_ket_thuc and not re.match(regex, gio_ket_thuc):
            print("Giờ kết thúc không đúng định dạng. Vui lòng nhập lại.")
            return

        # Chuyển đổi giờ bắt đầu và giờ kết thúc sang datetime để kiểm tra logic thời gian
        if gio_bat_dau:
            try:
                gio_bat_dau_dt = datetime.strptime(gio_bat_dau, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Giờ bắt đầu không hợp lệ.")
                return

        if gio_ket_thuc:
            try:
                gio_ket_thuc_dt = datetime.strptime(gio_ket_thuc, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Giờ kết thúc không hợp lệ.")
                return

        if gio_bat_dau and gio_ket_thuc and gio_bat_dau_dt >= gio_ket_thuc_dt:
            print("Giờ bắt đầu phải nhỏ hơn giờ kết thúc.")
            return

        # Kiểm tra trùng thời gian cho số máy (nếu có thay đổi máy)
        if may_tinh:
            for p in phieu_choi:
                if p['may_tinh'] == int(may_tinh) and p['ma_phieu'] != ma_phieu:
                    phieu_gio_bat_dau_dt = datetime.strptime(p['gio_bat_dau'], "%Y-%m-%d %H:%M")
                    phieu_gio_ket_thuc_dt = datetime.strptime(p['gio_ket_thuc'], "%Y-%m-%d %H:%M")

                    if (gio_bat_dau_dt < phieu_gio_ket_thuc_dt and gio_ket_thuc_dt > phieu_gio_bat_dau_dt):
                        print("Số máy này đã được sử dụng trong khoảng thời gian đã nhập. Vui lòng chọn thời gian khác.")
                        return

        dich_vu = input("Nhập dịch vụ mới: ").strip()

        # Cập nhật các thuộc tính nếu có thay đổi
        phieu['ma_phieu'] = ma_phieu_moi  # Cập nhật mã phiếu mới nếu có
        if khach_hang:
            phieu['khach_hang'] = khach_hang
        if may_tinh:
            phieu['may_tinh'] = int(may_tinh)  # Chuyển đổi sang số nguyên
        if gio_bat_dau:
            phieu['gio_bat_dau'] = gio_bat_dau
        if gio_ket_thuc:
            phieu['gio_ket_thuc'] = gio_ket_thuc
        if dich_vu:
            phieu['dich_vu'] = dich_vu

        # Cập nhật dữ liệu trong file
        luu_du_lieu_vao_file()
        print("Đã cập nhật phiếu chơi thành công!")

    except ValueError:
        print("Lỗi: Vui lòng nhập mã phiếu là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

# Xóa phiếu chơi theo mã
def xoa():
    try:
        ma_phieu = int(input("Nhập mã phiếu cần xóa: ").strip())
        
        # Tìm phiếu chơi theo mã
        phieu = next((p for p in phieu_choi if p['ma_phieu'] == ma_phieu), None)
        
        if phieu is None:
            print("Không tìm thấy phiếu chơi với mã này.")
            return
        
        # Xác nhận trước khi xóa
        confirm = input(f"Bạn có chắc chắn muốn xóa phiếu chơi với mã {ma_phieu}? (y/n): ").strip().lower()
        if confirm == 'y':
            phieu_choi.remove(phieu)  # Xóa phiếu chơi khỏi danh sách
            luu_du_lieu_vao_file()  # Cập nhật lại dữ liệu vào file
            print("Đã xóa phiếu chơi thành công!")
        else:
            print("Hủy thao tác xóa.")
    
    except ValueError:
        print("Lỗi: Vui lòng nhập mã phiếu là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")

# Thống kê số phiếu chơi theo khách hàng
def thong_ke_so_phieu():
    thong_ke = {}
    for phieu in phieu_choi:
        khach_hang = phieu['khach_hang']
        if khach_hang in thong_ke:
            thong_ke[khach_hang] += 1
        else:
            thong_ke[khach_hang] = 1
            
    # Hiển thị kết quả thống kê
    print("|      THỐNG KÊ SỐ PHIẾU THEO KHÁCH HÀNG  |")
    for khach_hang, so_phieu in thong_ke.items():
        print(f" Khách hàng: {khach_hang} - Số phiếu: {so_phieu}")
    print("+----------------------------------------+")

# Tổng hợp dịch vụ sử dụng
def tong_hop_dich_vu():
    dich_vu_count = {}
    for phieu in phieu_choi:
        dich_vu = phieu['dich_vu']
        if dich_vu in dich_vu_count:
            dich_vu_count[dich_vu] += 1
        else:
            dich_vu_count[dich_vu] = 1

    # Hiển thị kết quả tổng hợp dịch vụ
    print("|       TỔNG HỢP DỊCH VỤ SỬ DỤNG        |")
    for dich_vu, so_luong in dich_vu_count.items():
        print(f" Dịch vụ: {dich_vu} - Số lần sử dụng: {so_luong}")
    print("+----------------------------------------+")

def tim_phieu_theo_thoi_gian():
    # Nhập khoảng thời gian
    gio_bat_dau = input("Nhập thời gian bắt đầu (định dạng: yyyy-mm-dd HH:MM): ").strip()
    gio_ket_thuc = input("Nhập thời gian kết thúc (định dạng: yyyy-mm-dd HH:MM): ").strip()

    try:
        # Chuyển đổi thành đối tượng datetime
        gio_bat_dau = datetime.strptime(gio_bat_dau, '%Y-%m-%d %H:%M')
        gio_ket_thuc = datetime.strptime(gio_ket_thuc, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Định dạng thời gian không hợp lệ. Vui lòng nhập lại.")
        return

    # Lọc phiếu chơi theo thời gian
    print("|         TÌM KIẾM PHIẾU CHƠI THEO THỜI GIAN      |")
    found = False
    for phieu in phieu_choi:
        try:
            # Chuyển đổi giờ bắt đầu và kết thúc của phiếu chơi
            phieu_gio_bat_dau = datetime.strptime(phieu['gio_bat_dau'], '%Y-%m-%d %H:%M')
            phieu_gio_ket_thuc = datetime.strptime(phieu['gio_ket_thuc'], '%Y-%m-%d %H:%M')

            # Kiểm tra xem phiếu chơi có trong khoảng thời gian yêu cầu không
            if gio_bat_dau <= phieu_gio_bat_dau <= gio_ket_thuc or gio_bat_dau <= phieu_gio_ket_thuc <= gio_ket_thuc:
                print(f"Phiếu: {phieu['ma_phieu']} - Khách hàng: {phieu['khach_hang']} - Giờ bắt đầu: {phieu['gio_bat_dau']} - Giờ kết thúc: {phieu['gio_ket_thuc']}")
                found = True
        except ValueError:
            print(f"Định dạng thời gian của phiếu {phieu['ma_phieu']} không hợp lệ.")
    
    if not found:
        print("Không tìm thấy phiếu nào trong khoảng thời gian này.")
    
    print("+-------------------------------------------------+")


# Tính thời gian chơi
def tinh_thoi_gian_choi():
    if not phieu_choi:
        print("Danh sách phiếu chơi trống.")
        return
    
    ma_phieu = int(input("Nhập mã phiếu cần tính thời gian chơi: ").strip())
    
    # Tìm phiếu chơi theo mã
    phieu = next((p for p in phieu_choi if p['ma_phieu'] == ma_phieu), None)
    
    if phieu is None:
        print("Không tìm thấy phiếu chơi với mã này.")
        return
    
    try:
        # Chuyển đổi giờ bắt đầu và giờ kết thúc sang đối tượng datetime
        time_bat_dau = datetime.strptime(phieu['gio_bat_dau'], "%Y-%m-%d %H:%M")
        time_ket_thuc = datetime.strptime(phieu['gio_ket_thuc'], "%Y-%m-%d %H:%M")
        
        # Tính thời gian chơi
        thoi_gian_choi = time_ket_thuc - time_bat_dau
        print(f"Thời gian chơi cho phiếu {ma_phieu}: {thoi_gian_choi}")
    
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tính toán thời gian chơi: {e}. Vui lòng thử lại.")

def thong_ke_gio_cao_diem():
    gio_su_dung = [phieu['gio_bat_dau'].split()[1].split(':')[0] for phieu in phieu_choi]
    thong_ke = Counter(gio_su_dung)
    print("Thống kê giờ cao điểm:")
    for gio, so_lan in thong_ke.items():
        print(f"Giờ {gio}: {so_lan} lần")

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