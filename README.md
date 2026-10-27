# Pertemuan 12 - File I/O dan Error Handling
Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM,nilai

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- `FileNotFoundError` (saat file `data/nilai.txt` tidak ditemukan)
- `ValueError` (saat nilai pada baris file tidak dapat dikonversi menjadi tipe data float/angka)

## Test Case
| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| Normal (Semua baris valid) | Semua record diproses dan rekap benar | Semua record diproses dan rekap benar | Lulus |
| File hilang (`nilai.txt` tidak ada) | Pesan file tidak ditemukan; program tidak crash | Pesan file tidak ditemukan; program tidak crash | Lulus |
| Nilai invalid (`A004,abc`) | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Lulus |
| Baris kosong | Baris kosong dilewati | Baris kosong dilewati | Lulus |
| Batas lulus (Nilai 60) | Dihitung sebagai lulus | Dihitung sebagai lulus | Lulus |

## Refleksi
Error `ValueError` sering terjadi ketika program mencoba mengonversi data string non-angka (seperti teks `"abc"`) menjadi `float`. Hal ini ditangani menggunakan blok `try-except` di dalam perulangan baris, sehingga baris yang tidak valid dapat dilewati dan dilaporkan tanpa membuat program berhenti atau mengalami *crash*.