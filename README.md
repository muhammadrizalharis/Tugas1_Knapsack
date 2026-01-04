# Analisis 0/1 Knapsack pada Optimasi Isi Tas Mahasiswa Informatika

Repository ini berisi dataset dan program untuk menyelesaikan kasus **optimasi isi tas mahasiswa Informatika** menggunakan **0/1 Knapsack**. Metode utama yang digunakan adalah **Dynamic Programming**, serta disertai perbandingan **Brute Force** dan **Backtracking** (pruning).

## Struktur Folder

- dataset_knapsack_tas_mahasiswa_informatika.csv  
  Dataset item (berat dan nilai).
- knapsack_dp_from_csv.py  
  Program 0/1 Knapsack dengan Dynamic Programming (input dari CSV).
- compare_bruteforce_backtracking_save_ms.py  
  Program perbandingan Brute Force vs Backtracking dan penyimpanan output.
- tabel_perbandingan_bruteforce_vs_backtracking_ms.csv  
  Output tabel perbandingan (CSV).
- grafik_node_bruteforce_vs_backtracking.png  
  Output grafik jumlah evaluasi.
- grafik_waktu_ms_bruteforce_vs_backtracking.png  
  Output grafik waktu eksekusi (ms).
- README.md  

## Dataset

Dataset disimpan dalam format CSV dengan kolom:
- Item_ID
- Item_Name
- Weight_kg
- Value

File: `dataset_knapsack_tas_mahasiswa_informatika.csv`

## Menjalankan Program

### 1) Dynamic Programming (Solusi Optimal)
Jalankan:
```bash
python knapsack_dp.py
```

Output yang ditampilkan:
- nilai maksimum
- total berat
- daftar item terpilih

### 2) Perbandingan Brute Force vs Backtracking
Jalankan:
```bash
python knapsack_tugas1.py
```

Program akan menghasilkan file:
- `tabel_perbandingan_bruteforce_vs_backtracking_ms.csv`
- `grafik_node_bruteforce_vs_backtracking.png`
- `grafik_waktu_ms_bruteforce_vs_backtracking.png`

## Catatan
- Satuan waktu disimpan dalam **milidetik (ms)** agar mudah dibaca dan tidak tampil dalam notasi scientific.
- Semua file output tersimpan pada folder yang sama dengan file program.

## Identitas
Kelompok 6 — Informatika
