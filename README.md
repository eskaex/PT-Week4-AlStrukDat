# Penentuan Juara Coswalk di Panggung REQUIEM

Malam puncak REQUIEM: Feast To The Unseen di bulan November semakin dekat! Panitia mengadakan Coswalk Competition yang diikuti oleh ratusan cosplayer. Penilaian dilakukan oleh tiga juri berdasarkan tiga kriteria: Detail Kostum, Penghayatan Karakter, dan Reaksi Penonton (sorakan).

Karena antusiasme yang luar biasa, data skor peserta masuk secara acak dan panitia harus mengumumkan pemenang tepat sebelum DJ Performance dimulai dalam waktu 10 menit. Bantulah panitia REQUIEM membuat sistem pengurutan menggunakan **algoritma Divide and Conquer** untuk mengurutkan peserta dari Total Skor tertinggi. Jika total skor sama, prioritaskan peserta dengan nilai "Reaksi Penonton" tertinggi!

### Tugas

Buatlah program yang mengurutkan seluruh peserta Coswalk Competition berdasarkan Total Skor (Skor_Kostum + Skor_Karakter + Skor_Penonton), dari yang tertinggi ke terendah, menggunakan salah satu algoritma *Divide and Conquer*:
- **Merge Sort**
- **Quick Sort**

*(Pilih salah satu saja)*

**Aturan pengurutan:**
1. Total Skor lebih tinggi → posisi lebih atas.
2. Jika Total Skor sama, peserta dengan Skor Reaksi Penonton lebih tinggi berhak menang.

---

### Ketentuan

1. **WAJIB** menggunakan Merge Sort atau Quick Sort dengan pendekatan rekursif *Divide and Conquer*. Pilih salah satu saja.
2. **Dilarang** menggunakan fungsi bawaan seperti `sorted()`, `.sort()`, atau sejenisnya untuk melakukan pengurutan datanya.
3. Aturan perbandingan (Total Skor, lalu *tie-break* Skor Penonton) harus ada di dalam logika pembagian/penggabungan algoritma kalian sendiri (bagian *partition/merge*).
4. Program harus tetap efisien untuk jumlah peserta yang besar — hindari algoritma $O(n^2)$ seperti Bubble Sort atau Insertion Sort, karena panitia cuma punya waktu 10 menit sebelum *DJ Performance* dimulai!
5. Kalian harus bisa menjelaskan ke asisten dosen bagian *divide* (bagaimana data dipecah), *conquer* (bagaimana sub-masalah diselesaikan), dan *combine* (bagaimana hasil digabung/dipartisi) dari algoritma yang dipilih saat demo.

---

### Format Input

- Baris pertama: `N` — jumlah peserta.
- `N` baris berikutnya, masing-masing berisi (dipisah spasi):
  `Nama_Karakter Skor_Kostum Skor_Karakter Skor_Penonton`
  
*(Gunakan underscore `_` sebagai pengganti spasi pada nama karakter, misalnya `Ratu_Bayangan`)*

### Format Output

Leaderboard peserta dari Juara 1 (Total Skor tertinggi) sampai peserta terakhir, masing-masing menampilkan peringkat, nama karakter, dan total skor.


print("===== HASIL COSWALK COMPETITION - REQUIEM: FEAST TO THE UNSEEN =====")
for i, p in enumerate(hasil, start=1):
    print(f"Juara {i} : {p[0]} (Total Skor: {p[4]})")
