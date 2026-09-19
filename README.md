# Penentuan Juara Coswalk di Panggung REQUIEM

Malam puncak REQUIEM: Feast To The Unseen di bulan November semakin dekat! Panitia mengadakan Coswalk Competition yang diikuti oleh ratusan cosplayer di Atrium Didaktos. Penilaian dilakukan oleh tiga juri berdasarkan tiga kriteria: Detail Kostum, Penghayatan Karakter, dan Reaksi Penonton (sorakan).

Karena antusiasme yang luar biasa, data skor peserta masuk secara acak dan panitia harus mengumumkan pemenang tepat sebelum DJ Performance dimulai dalam waktu 10 menit. Bantulah panitia REQUIEM membuat sistem pengurutan menggunakan **algoritma Divide and Conquer** untuk mengurutkan peserta dari Total Skor tertinggi. Jika total skor sama, prioritaskan peserta dengan nilai "Reaksi Penonton" tertinggi!

## Tugas

Buatlah program yang mengurutkan seluruh peserta Coswalk Competition berdasarkan Total Skor (Skor_Kostum + Skor_Karakter + Skor_Penonton), dari yang tertinggi ke terendah, menggunakan salah satu algoritma *Divide and Conquer*:
- **Merge Sort**
- **Quick Sort**

**Aturan pengurutan:**
1. Total Skor lebih tinggi → posisi lebih atas.
2. Jika Total Skor sama, peserta dengan Skor Reaksi Penonton lebih tinggi berhak menang (*tie-break*).

## Ketentuan

1. **WAJIB** menggunakan Merge Sort atau Quick Sort dengan pendekatan rekursif *Divide and Conquer*. Pilih salah satu saja.
2. **Dilarang** menggunakan fungsi bawaan seperti `sorted()`, `.sort()`, atau sejenisnya untuk melakukan pengurutan datanya.
3. Aturan perbandingan (Total Skor, lalu *tie-break* Skor Penonton) harus ada di dalam logika pembagian/penggabungan algoritma kalian sendiri (bagian *partition/merge*).
4. Program harus tetap efisien untuk jumlah peserta yang besar — hindari algoritma $O(n^2)$ seperti Bubble Sort atau Insertion Sort, karena panitia cuma punya waktu 10 menit sebelum *DJ Performance* dimulai!
5. Kalian harus bisa menjelaskan ke asisten dosen bagian *divide* (bagaimana data dipecah), *conquer* (bagaimana sub-masalah diselesaikan), dan *combine* (bagaimana hasil digabung/dipartisi) dari algoritma yang dipilih.

## Penjelasan Parameter

Terdapat beberapa parameter yang umumnya digunakan pada fungsi-fungsi rekursif dalam program ini (tergantung algoritma yang Anda pilih):

1. `peserta` = Tipe data **List**, berisi kumpulan **Dictionary** data cosplayer `{"nama": ..., "kostum": ..., "karakter": ..., "penonton": ..., "total": ...}` yang akan diurutkan.
2. `low` (atau `left`) = Tipe data **Integer**, menunjukkan batas awal atau indeks paling kiri dari sub-array yang sedang diproses dalam rekursi.
3. `high` (atau `right`) = Tipe data **Integer**, menunjukkan batas akhir atau indeks paling kanan dari sub-array yang sedang diproses.
4. `mid` = Tipe data **Integer**, menunjukkan titik tengah array (khusus jika menggunakan Merge Sort) yang digunakan untuk membagi sub-masalah.

## Test Case & Format Output

Pada program ini, *test case* awal sudah disediakan secara *hardcoded* di dalam kerangka program. Anda hanya perlu memastikan fungsi sorting Anda mengembalikan data yang sudah terurut dengan benar. 

**Contoh Output yang Diharapkan:**
```text
===== HASIL COSWALK COMPETITION - REQUIEM: FEAST TO THE UNSEEN =====
Juara 1 : Zhongli_Kagak_Punya_Mora (Total Skor: 278 | Skor Penonton: 85)
Juara 2 : Kafka_Stellaron (Total Skor: 275 | Skor Penonton: 95)
Juara 3 : Kobo_Pawang_Hujan (Total Skor: 270 | Skor Penonton: 90)
Juara 4 : Anya_Waku_Waku (Total Skor: 270 | Skor Penonton: 85)
Juara 5 : Windah_Bocil_Kematian (Total Skor: 265 | Skor Penonton: 100)
Juara 6 : Gojo_Nah_Id_Win (Total Skor: 265 | Skor Penonton: 90)
Juara 7 : Jett_Rebibe_Me (Total Skor: 265 | Skor Penonton: 88)
Juara 8 : Frieren_Males_Gerak (Total Skor: 263 | Skor Penonton: 85)
Juara 9 : Sigma_Mewing_Chad (Total Skor: 250 | Skor Penonton: 75)
Juara 10 : Bocil_Epep_Jumpshoot (Total Skor: 229 | Skor Penonton: 99)
```

## Catatan Tambahan

- Mohon baca soal sampai selesai sebelum bertanya.
- Perhatikan base case rekursi (baik untuk Merge Sort maupun Quick Sort) agar tidak terjadi infinite recursion.
- Kode difokuskan pada pemahaman pembagian masalah (Divide and Conquer), bukan sekadar output yang benar — jadi tetap wajib rekursif, bukan iteratif murni.
- Tiket presale REQUIEM (November 2026) udah mau buka nih. Jangan sampai kehabisan atau kamu bakal dihantui penyesalan! 🎃👻
- Pwiss follow IG & Tiktok @requiem.halloweenparty biar update sama infonya ya - THANK YOUU
