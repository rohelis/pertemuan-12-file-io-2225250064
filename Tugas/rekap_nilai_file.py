def baca_data(nama_file):
    data_valid = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data_valid.append({"nim": nim.strip(), "nilai": nilai})
                except ValueError:
                    print(f"Baris {nomor} tidak valid (diabaikan): {baris}")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    return data_valid

def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return
    
    jumlah_data = len(data)
    total_nilai = sum(mhs["nilai"] for mhs in data)
    rata_rata = total_nilai / jumlah_data
    nilai_min = min(mhs["nilai"] for mhs in data)
    nilai_max = max(mhs["nilai"] for mhs in data)
    jumlah_lulus = sum(1 for mhs in data if mhs["nilai"] >= 60)
    
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("=== REKAP NILAI MAHASISWA ===\n")
        file.write(f"Jumlah Data Valid: {jumlah_data}\n")
        file.write(f"Rata-rata Nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai Minimum: {nilai_min}\n")
        file.write(f"Nilai Maksimum: {nilai_max}\n")
        file.write(f"Jumlah Lulus (>= 60): {jumlah_lulus}\n")
    
    print(f"Rekap berhasil ditulis ke {nama_file}")
    print(f"Jumlah Data Valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Minimum: {nilai_min} | Maksimum: {nilai_max}")
    print(f"Lulus: {jumlah_lulus}")

input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

hasil_baca = baca_data(input_file)
if hasil_baca:
    tulis_rekap(output_file, hasil_baca)