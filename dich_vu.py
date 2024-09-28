def thoat (v):
    while True: # chay lien tuc khi nao gap false dung lai
        a = input(v).lower().strip() # hoa-> thuong
        if a == 'y':
            return True 
        elif a == 'n':
            return False
        else:
            print('--VUI LONG CHI NHAP Y HOAC N--')

def hien_thi_danh_sach ():
    print('CHUC NANG 1')

def tim_kiem ():
    print('CHUC NANG 2')

def them_dich_vu ():
    if thoat ('\n BAN CO MUON THEM DICH VU KHONG ?(nhap y hoac n) '):
        print('-THEM DICH VU-')
    else:
        print('-KHONG THEM DUOC DICH VU-')

def sua_thong_tin ():
    if thoat ('\n BAN CO MUON SUA THONG TIN KHONG ? (nhap y hoac n) '):
        print('-SUA THONG TIN-')
    else:
        print('-KHONG SUA DUOC THONG TIN-')

def xoa_mot_dich_vu ():
    if thoat ('\n BAN CO MUON XOA DICH VU KHONG ?(nhap y hoac n) '):
        print('-XOA DICH VU-')
    else:
        print('-KHONG XOA DUOC DICH VU-')

def sx_theo_gia ():
    print('CHUC NANG 6')

def thong_ke_theo_ma ():
    print('CHUC NANG 7')

def dem_sl_dv_theo_dv():
    print('CHUC NANG 8')

def tinh_tong():
    print('CHUC NANG 9')

def xuat_file():
    if thoat ('\n BAN CO MUON XUAT FILE KHONG ?(nhap y hoac n)'):
        print('-XUAT FILE-')
    else:
        print('-KHONG THE XUAT FILE-')

def menu ():
    try:
        while True:
            print('\n--Quản lý quán game internet--')
            print('1.Hien thi danh sach dich vu ')
            print('2.Tìm kiếm dịch vụ theo mã.')
            print('3.Thêm dịch vụ mới vào danh sách. ')
            print('4.Sửa thông tin một dịch vụ cụ thể. ')
            print('5.Xóa một dịch vụ khỏi danh sách. ')
            print('6.Sap xep theo gia.  ')
            print('7.Thong ke theo ma.')
            print('8.Dem so luong dich vu theo dich vu.')
            print('9.Tính tổng tất cả giá trị của các dịch vụ trong danh sách.')
            print('10.Xuat file. ')
            print('0.Thoat\n')

            van = input('MOI NHAP CHUC NANG: ')

            van = int(van)
            match van :
                case 1:
                    hien_thi_danh_sach()
                case 2:
                    tim_kiem()
                case 3:
                    them_dich_vu()
                case 4:
                    sua_thong_tin()
                case 5:
                    xoa_mot_dich_vu()
                case 6:
                    sx_theo_gia()
                case 7:
                    thong_ke_theo_ma()
                case 8:
                    dem_sl_dv_theo_dv()
                case 9:
                    tinh_tong()
                case 10:
                    xuat_file()
                case 0:
                    if thoat('BAN CO MUON THOAT CHUONG TRINH: '):
                        print('DA THOAT CHUONG TRINH ')
                        break
                    else:
                        print('THAO TAC BI HUY')
                
    except ValueError:
        print('---VUI LONG NHAP DUNG CU PHAP (hay nhap 0 -> 10 )---')

if __name__ == "__main__":
    menu()


