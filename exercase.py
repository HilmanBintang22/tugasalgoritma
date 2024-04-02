total_nilai_bobot = 0 
total_kredit = 0
print("Masukkan nilai dan kredit mata kuliah (ketik 'selesai' untuk mengakhiri)")
while True:
    nilai = input("Nilai Mata Kuliah (A/B/C/D/E): ").upper()
    if nilai == 'SELESAI':
        break
    kredit = float(input("Jumlah Kredit Mata Kuliah: "))
    bobot_nilai = 4 if nilai == 'A' else 3 if nilai == 'B' else 2 if nilai == 'C' else 1 if nilai == 'D' else 0
    nilai_bobot = bobot_nilai * kredit
    total_nilai_bobot += nilai_bobot
    total_kredit += kredit
if total_kredit == 0:
    ipk = 0
else: 
    ipk = total_nilai_bobot / total_kredit
print("Indeks Prestasi Kumulatif (IPK): {:.2f}".format(ipk))
