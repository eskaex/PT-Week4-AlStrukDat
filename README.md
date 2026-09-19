# Penentuan Juara Coswalk di Panggung REQUIEM

Malam puncak REQUIEM: Feast To The Unseen di bulan November semakin dekat! Panitia mengadakan Coswalk Competition yang diikuti oleh ratusan cosplayer. Penilaian dilakukan oleh tiga juri berdasarkan tiga kriteria: Detail Kostum, Penghayatan Karakter, dan Reaksi Penonton (sorakan).

Karena antusiasme yang luar biasa, data skor peserta masuk secara acak dan panitia harus mengumumkan pemenang tepat sebelum DJ Performance dimulai dalam waktu 10 menit. Bantulah panitia REQUIEM membuat sistem pengurutan menggunakan **algoritma Divide and Conquer** untuk mengurutkan peserta dari Total Skor tertinggi. Jika total skor sama, prioritaskan peserta dengan nilai "Reaksi Penonton" tertinggi!

<hr>

### Tugas

Buatlah program yang mengurutkan seluruh peserta Coswalk Competition berdasarkan Total Skor (Skor_Kostum + Skor_Karakter + Skor_Penonton), dari yang tertinggi ke terendah, menggunakan salah satu algoritma *Divide and Conquer*:
- **Merge Sort**, atau
- **Quick Sort**

*(Pilih salah satu — soal ini unguided, jadi tidak ada kerangka logika sorting yang diberikan; kalian yang merancang sendiri fungsi divide, conquer, dan combine-nya)*

**Aturan pengurutan:**
1. Total Skor lebih tinggi → posisi lebih atas.
2. Jika Total Skor sama, peserta dengan Skor Reaksi Penonton lebih tinggi berhak menang (*tie-break*).

<hr>

### ⚠️ Ketentuan

1. **WAJIB** menggunakan Merge Sort atau Quick Sort dengan pendekatan rekursif *Divide and Conquer*. Pilih salah satu saja.
2. **Dilarang** menggunakan fungsi bawaan seperti `sorted()`, `.sort()`, atau sejenisnya untuk melakukan pengurutan datanya.
3. Aturan perbandingan (Total Skor, lalu *tie-break* Skor Penonton) harus ada di dalam logika pembagian/penggabungan algoritma kalian sendiri (bagian *partition/merge*).
4. Program harus tetap efisien untuk jumlah peserta yang besar — hindari algoritma $O(n^2)$ seperti Bubble Sort atau Insertion Sort, karena panitia cuma punya waktu 10 menit sebelum *DJ Performance* dimulai!
5. Kalian harus bisa menjelaskan ke asisten dosen bagian *divide* (bagaimana data dipecah), *conquer* (bagaimana sub-masalah diselesaikan), dan *combine* (bagaimana hasil digabung/dipartisi) dari algoritma yang dipilih saat demo.

---

### 🛠️ Penjelasan Parameter

Terdapat beberapa parameter yang umumnya digunakan pada fungsi-fungsi rekursif dalam program ini (tergantung algoritma yang Anda pilih):

1. `peserta` = Tipe data **List**, berisi kumpulan *tuple* data cosplayer `(nama, skor_kostum, skor_karakter, skor_penonton, total_skor)` yang akan diurutkan.
2. `low` (atau `left`) = Tipe data **Integer**, menunjukkan batas awal atau indeks paling kiri dari sub-array yang sedang diproses dalam rekursi.
3. `high` (atau `right`) = Tipe data **Integer**, menunjukkan batas akhir atau indeks paling kanan dari sub-array yang sedang diproses.
4. `mid` = Tipe data **Integer**, menunjukkan titik tengah array (khusus jika menggunakan Merge Sort) yang digunakan untuk membagi sub-masalah.

<hr>

### Test Case & Format Output

```text
===== HASIL COSWALK COMPETITION - REQUIEM: FEAST TO THE UNSEEN =====
Juara 1 : Dewi_Kelam (Total Skor: 275 | Skor Penonton: 95)
Juara 2 : Ratu_Bayangan (Total Skor: 265 | Skor Penonton: 90)
Juara 3 : Ksatria_Kabut (Total Skor: 265 | Skor Penonton: 88)
Juara 4 : Sang_Penjaga_Fajar (Total Skor: 263 | Skor Penonton: 85)
Juara 5 : Roh_Pemburu (Total Skor: 250 | Skor Penonton: 75)

print("===== HASIL COSWALK COMPETITION - REQUIEM: FEAST TO THE UNSEEN =====")
for i, p in enumerate(hasil, start=1):
    print(f"Juara {i} : {p[0]} (Total Skor: {p[4]})")
