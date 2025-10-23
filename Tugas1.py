# Tugas Dasar-Dasar Pemrograman

print("\tPROGRAM HITUNG GAJI KARYAWAN")

gaji = 300000

nama_karyawan = input("Masukan nama karyawan = ")
golongan_jabatan = int(input("Masukan golongan jabatan (1/2/3) = "))
pendidikan = input("Masukan pendidikan (SMA/D1/D3/S1) = ")
jumlah_jam_kerja = int(input("Masukan jam kerja = "))

# Tunjangan jabatan

if golongan_jabatan == 1:
    tunjangan_jabatan = 0.05 * gaji
elif golongan_jabatan == 2:
    tunjangan_jabatan = 0.1 *gaji
elif golongan_jabatan == 3:
    tunjangan_jabatan = 0.15 *gaji
else :
    tunjangan_jabatan = 0
    print("Golongan tidak valid, tunjangan jabatan = 0 ")



# Tunjangan pendidikan

if pendidikan == 'SMA' or pendidikan == 'sma':
    tunjangan_pendd = gaji*0.25
elif pendidikan == 'D1' or pendidikan == 'd1':
    tunjangan_pendd = gaji*0.05
elif pendidikan == 'D3' or pendidikan == 'd3':
    tunjangan_pendd = gaji*0.2
elif pendidikan == 'S1' or pendidikan == 's1':
    tunjangan_pendd = gaji*0.3
else :
    tunjangan_pendd = 0
    print("Pendidikan tidak valid, tunjangan pendidikan = 0 ")


# Honor lembur

if jumlah_jam_kerja > 8:
    lebih_jam_kerja = (jumlah_jam_kerja - 8)*3500
else:
    lebih_jam_kerja = 0


# Total gaji

total_gaji = gaji + tunjangan_jabatan + tunjangan_pendd + lebih_jam_kerja


# Output
print("\n\tRINCIAN GAJI KARYAWAN\n")
print("Nama Karyawan        :",nama_karyawan)
print("Tunjangan Jabatan    :",tunjangan_jabatan)
print("Tunjangan Pendidikan :",tunjangan_pendd)
print("----------------------------------------------")
print("Tunjangan jabatan anda adalah Rp...",tunjangan_jabatan)
print("Tunjangan pendidikan Rp...",tunjangan_pendd)
print("Honor lembur anda Rp...",lebih_jam_kerja)
print("---------------------------------------------+")
print("Total gaji anda Rp...",total_gaji)
print("===========================================================")