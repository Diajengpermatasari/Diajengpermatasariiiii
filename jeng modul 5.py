def konversi_nilai(huruf):
    if huruf == "A":
        peringkat = 4.00
    elif huruf == "A-":
        peringkat = 3.75
    elif huruf == "B+":
        peringkat = 3.50
    elif huruf == "B":
        peringkat = 3.00
    elif huruf == "B-":
        peringkat = 2.75
    elif huruf == "C+":
        peringkat = 2.50
    elif huruf == "C":
        peringkat = 2.00
    elif huruf == "C-":
        peringkat = 1.75
    elif huruf == "D":
        peringkat = 1.50
    elif huruf == "E":
        peringkat = 1.25
    else:
        peringkat = None

    return peringkat

# Variabel untuk menghitung total dan jumlah data
total_bobot = 0
jumlah_data = 0

print("Masukkan nilai huruf satu per satu. Tekan Enter langsung jika sudah selesai.")

while True:
    masukan = input("Masukkan nilai huruf: ").strip()
    
    # Jika pengguna langsung menekan Enter, perulangan berhenti
    if masukan == "":
        break
        
    nilai = masukan.upper()
    hasil = konversi_nilai(nilai)

    if hasil is not None:
        print("Nilai angka =", format(hasil, ".2f"))
        total_bobot += hasil
        jumlah_data += 1
    else:
        print("Kategori nilai tidak valid!")

# Menghitung dan menampilkan rata-rata di akhir
if jumlah_data > 0:
    rata_rata = total_bobot / jumlah_data
    print("\n--- Hasil Akhir ---")
    print(f"Rata-rata nilai angka adalah: {rata_rata:.2f}")
else:
    print("Tidak ada nilai yang dimasukkan.")


# DIAJENG PERMATASARI

def hitung_tiket_kebun_binatang():
    total_harga = 0.0
    
    while True:
        masukan = input("masukkan umur: ").strip()
        
        # Jika pengguna langsung menekan Enter, perulangan berhenti
        if masukan == "":
            break
            
        umur = int(masukan)
        
        # Menentukan harga berdasarkan aturan umur[cite: 3]
        if umur <= 2:
            harga = 0.0
            print("Gratis")
        elif 3 <= umur <= 12:
            harga = 14.0
            print("Harga $14.00")
        elif umur >= 65:
            harga = 18.0
            print("Harga $18.00")
        else:
            harga = 23.0
            print("Harga $23.00")
            
        total_harga += harga
        print(f"Running total: {total_harga:.2f}")
        
    # Proses pembayaran dan pengembalian uang (kembalian)[cite: 3]
    if total_harga > 0:
        uang_masuk = float(input("masukkan jumlah uang: "))
        kembalian = uang_masuk - total_harga
        print(f"Running kembalian: {kembalian:.2f}")
    else:
        print("Tidak ada tiket yang dipesan.")

if __name__ == "__main__":
    hitung_tiket_kebun_binatang()
