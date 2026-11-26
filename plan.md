# Rencana Implementasi 3mate Unlimited

## Arah desain

Aplikasi diubah dari daily challenge menjadi latihan puzzle tanpa batas. Visualnya mobile-first dengan nuansa chess trainer modern: background charcoal, papan hijau-krem, aksen kuning, kartu gelap/terang dengan radius membulat, bayangan lembut, dan tanpa karakter/avatar.

## Implementasi

- Pertahankan engine catur internal, dataset puzzle, aset bidak, audio, pointer interaction, promosi, hint, dan reveal.
- Ganti daily lifecycle dengan pemilihan puzzle berdasarkan rating pemain dan daftar puzzle terbaru.
- Tambahkan onboarding rating awal sekali per browser.
- Simpan rating, streak, statistik, puzzle terakhir, opsi suara, dan sesi aktif di localStorage/window.storage.
- Terapkan rating Elo-style per puzzle: solve tanpa bantuan mendapat kenaikan penuh, hint mengurangi kualitas, reveal menghasilkan kualitas rendah, dan satu langkah salah langsung menyelesaikan puzzle sebagai gagal dengan rating turun.
- Tambahkan layout responsif: papan sebagai fokus utama; panel status dan kontrol di bawah pada mobile serta panel samping pada desktop.
- Tambahkan statistik ringkas dan pengaturan sederhana di overlay.

## File utama

- `index.html`: aplikasi aktif hasil implementasi.
- `experiment.html`: disinkronkan sebagai varian unlimited yang sama agar tidak tertinggal.
- `index-1.html`: dipertahankan sebagai snapshot lama.
- `README.md`: diperbarui untuk menjelaskan mode unlimited.
