# MAIN PROGAM
daftar_menu = {
    1: {"nama": "Nasi Goreng", "harga": 12000},
    2: {"nama": "Mie Ayam", "harga": 10000},
    3: {"nama": "Seblak", "harga": 12000},
    4: {"nama": "ES Teh", "harga": 4000},
    5: {"nama": "ES Lemon", "harga": 5000},
    6: {"nama": "Siomay", "harga": 10000},
    7: {"nama": "Sate Kambih", "harga": 50000},
}

belanjaan = []

while True:
    print("""
========== MENU MAKANAN ==========
No      Nama Makanan      Harga       
----------------------------------
[1]  Nasi Goreng         Rp12,000
[2]  Mie Ayam            Rp10,000
[3]  Seblak              Rp12,000
[4]  ES Teh              Rp4,000
[5]  ES Lemon            Rp5,000
[6]  Siomay              Rp10,000
[7]  Sate Kambing        Rp50,000
    
[0]  Selesai
----------------------------------""")

    pilihan = int(input("Pilih menu makanan yang akan dibeli : "))

    if pilihan == 0:
        break

    if pilihan < 1 or pilihan > len(daftar_menu):
        print("Pilihan tidak valid. Silakan pilih item yang sesuai.")
        continue

    jumlah = int(input("Masukkan jumlah pesanan             : "))

    menu_terpilih = daftar_menu[pilihan]
    menu_terpilih["jumlah"] = jumlah
    belanjaan.append(menu_terpilih)

total_belanja = 0
total_harga = 0

# STRUK PEMBELIAN
print("")
print("                 WARUNG MA'E                 ")
print(" Jl.Raya Susah, Tenggulangharjo, Kec. Subah  ")
print("             Kab. Batang, 51262              ")
print("")
print("---------------------------------------------")
import datetime
waktu = datetime.datetime.now()
f_waktu = waktu.strftime("%Y-%m-%d %H:%M")
print(f_waktu, "               12042/NoNm/02")
print("---------------------------------------------")
for item in belanjaan:
    nama = item['nama']
    jumlah = item['jumlah']
    harga = item['harga']
    subtotal = harga * jumlah
    print(f"{nama.ljust(15)}{str(jumlah).ljust(10)}Rp{str(harga).ljust(9)}Rp{subtotal}")
    total_belanja += subtotal
    f_total_belanja = f"{total_belanja:,.0f}"

print("                     ------------------------")
print("                     Total Belanja : Rp%s"%(f_total_belanja))

# Diskon
if total_belanja > 100000:
    diskon = total_belanja * 0.05
    total_harga = total_belanja - diskon
else :
    diskon = 0 
    total_harga = total_belanja - diskon

f_diskon = f"{diskon:,.0f}"
f_total_harga = f"{total_harga:,.0f}"
print("                     Diskon        : Rp%s" %(f_diskon))
print("                     ------------------------")
print("                     Total Harga   : Rp%s" %(f_total_harga))

# Bayar
uang_bayar = int(input("                     Bayar         : Rp"))
while uang_bayar < total_harga:
    print("   !!! Uang Pembayaran Kurang'  !!!   ")
    uang_bayar = int(input("                     Bayar Ulang   : Rp"))

# Kembalian
kembalian = uang_bayar - total_harga
f_kembalian = f"{kembalian:,.0f}"
print("                     Kembalian     : Rp%s"%(f_kembalian))
print("")
print("")
print("             Suwon Wes Belonjo Bolo'               ")
print("    CUST.CARE SMS 081234567981 - WA 085212345685   ")
print("       CALL 1200 290 - WARUNGMae03@GMAIL.COM       ")

# Eksport struk ke .txt
eksport = input("Apakah Anda ingin menyimpan struk pembelian sebagai file .txt? (y/n): ").lower()
if eksport == 'y':
    # Nama file txt
    nama_file = "struk_pembelian.txt"

    # Menulis struk ke .txt
    with open(nama_file, "w") as file:
        file.write("\n")
        file.write("                WARUNG MA'E                  \n")
        file.write(" Jl.Raya Susah, Tenggulangharjo, Kec. Subah  \n")
        file.write("             Kab. Batang, 51262              \n\n")
        file.write("---------------------------------------------\n")
        import datetime
        waktu = datetime.datetime.now()
        f_waktu = waktu.strftime("%Y-%m-%d %H:%M")
        file.write(f"{f_waktu}               12042/NoNm/02\n")
        file.write("---------------------------------------------\n")
        for item in belanjaan:
            nama = item['nama']
            jumlah = item['jumlah']
            harga = item['harga']
            subtotal = harga * jumlah
            file.write(f"{nama.ljust(15)}{str(jumlah).ljust(10)}Rp{str(harga).ljust(9)}Rp{subtotal}\n")

        file.write("                     ------------------------\n")
        file.write(f"                     Total Belanja : Rp{total_belanja:,.0f}\n")
        if total_belanja > 100000:
            diskon = total_belanja * 0.05
            total_harga = total_belanja - diskon
            f_diskon = f"{diskon:,.0f}"
            f_total_harga = f"{total_harga:,.0f}"
            file.write(f"                     Diskon        : Rp{f_diskon}\n")
            file.write("                     ------------------------\n")
            file.write(f"                     Total Harga   : Rp{f_total_harga}\n")

        file.write(f"                     Bayar         : Rp{uang_bayar}\n")
        f_kembalian = f"{(uang_bayar - total_harga):,.0f}"
        file.write(f"                     Kembalian     : Rp{f_kembalian}\n\n\n")
        file.write("             Suwon Wes Belonjo Bolo'               \n")
        file.write("    CUST.CARE SMS 081234567981 - WA 085212345685   \n")
        file.write("       CALL 1200 290 - WARUNGMAE03@GMAIL.COM       \n")

    print(f"Struk pembelian telah berhasil disimpan sebagai file {nama_file}")
