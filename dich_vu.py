import time
def thoat (v):
    while True: # chay lien tuc khi nao gap false dung lai
        a = input(v).lower().strip() # hoa-> thuong
        if a == 'y':
            return True 
        elif a == 'n':
            return False
        else:
            print('--VUI LONG CHI NHAP Y HOAC N--')


dich_vu = [
    {'ma': 'DV001', 'ten': 'Internet', 'gia': 200000},
    {'ma': 'DV002', 'ten': 'Truyen hinh cap', 'gia': 150000},
    {'ma': 'DV001', 'ten': 'Internet', 'gia': 100000},
    {'ma': 'DV003', 'ten': 'Dien thoai', 'gia': 250000},
    {'ma': 'DV002', 'ten': 'Truyen hinh cap', 'gia': 150000}
]

def hien_thi_danh_sach ():
    print('CHUC NANG 1')
    for dv in dich_vu:
        print(f"Ma: {dv['ma']}, Ten: {dv['ten']}, Gia: {dv['gia']}")

def tim_kiem ():
    print('CHUC NANG 2')
    
    ma = input('Nhap ma dich vu can tim: ')
    for dv in (dich_vu):
        if dv['ma'] == ma:
            print(f"Ma: {dv['ma']}, Ten: {dv['ten']}, Gia: {dv['gia']}")
            return
    print('KHONG TIM THAY DICH VU.')



def them_dich_vu ():
    print('CHUC NANG 3')
    if thoat ('\n BAN CO MUON THEM DICH VU KHONG ?(nhap y hoac n) '):
        print('-THEM DICH VU-')

        ma = input('Nhap ma dich vu: ')
        ten = input('Nhap ten dich vu: ')
        gia = float(input('Nhap gia dich vu: '))
        dich_vu.append({'ma': ma, 'ten': ten, 'gia': gia})
        print('-THEM DICH VU THANH CONG-')

    else:
        print('-KHONG THEM DUOC DICH VU-')

def sua_thong_tin():
    print('CHUC NANG 4')
    if thoat('\nBAN CO MUON SUA THONG TIN KHONG? (nhap y hoac n) '):
        print('-SUA THONG TIN-')
        ma = input('Nhap ma dich vu can sua: ')
        for dv in dich_vu:
            if dv['ma'] == ma:
                dv['ten'] = input('Nhap ten dich vu moi: ')
                dv['gia'] = float(input('Nhap gia dich vu moi: '))
                print('-SUA THONG TIN THANH CONG-')
                return
        print('Khong tim thay dich vu can sua.')
    else:
        print('-KHONG SUA DUOC THONG TIN-')

def xoa_mot_dich_vu ():
    print('CHUC NANG 5')
    if thoat ('\n BAN CO MUON XOA DICH VU KHONG ?(nhap y hoac n) '):
        print('--XOA DICH VU--')

        ma = input('Nhap ma dich vu can xoa: ')
        for dv in dich_vu:
            if dv['ma'] == ma:
                dich_vu.remove(dv)
                print('-XOA DICH VU THANH CONG-')
                return
        print('Khong tim thay dich vu can xoa.')

    else:
        print('-KHONG XOA DUOC DICH VU-')

def sx_theo_gia():
    print('CHUC NANG 6')
    
    dich_vu.sort(key=lambda dv: dv['gia'])
    print('-DANH SACH DA DUOC SAP XEP THEO GIA-')
    hien_thi_danh_sach()


def thong_ke_theo_ma ():
    print('CHUC NANG 7')

    ma_dv = input('Nhap ma dich vu can thong ke: ')
    dem = sum(1 for dv in dich_vu if dv['ma'] == ma_dv)
    print(f'-SO LUONG DICH VU VOI MA "{ma_dv}": {dem}')

def dem_sl_dv_theo_dv():
    print('CHUC NANG 8')
    dich_vu_counts = {}
    
    for dv in dich_vu:
        if dv['ten'] in dich_vu_counts:
            dich_vu_counts[dv['ten']] += 1
        else:
            dich_vu_counts[dv['ten']] = 1
            
    print('---THONG KE SO LUONG DICH VU---')
    for ten, count in dich_vu_counts.items():
        print(f'{ten}: {count}')

def tinh_tong():
    print('CHUC NANG 9')

    tong_gia_tri = sum(dv['gia'] for dv in dich_vu)
    print(f'-TONG GIA TRI TAT CA DICH VU: {tong_gia_tri}-')


import csv
def xuat_file():
    print('CHUC NANG 10')
    ten_file = 'dich_vu.csv'
    with open(ten_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ma', 'Ten', 'Gia'])
        for dv in dich_vu:
            writer.writerow([dv['ma'], dv['ten'], dv['gia']])
    
    print(f'-XUAT FILE THANH CONG: {ten_file}-')

    
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
                        print('-DA THOAT CHUONG TRINH- ')
                        break
                    else:
                        print('-THAO TAC BI HUY-')
                
    except ValueError:
        print('---VUI LONG NHAP DUNG CU PHAP (hay nhap 0 -> 10)---')
    

