% Fakta-fakta dan aturan gaya belajar (berdasarkan forward chaining)

% Aturan gaya belajar Visual
gaya_belajar(visual) :- 
    senang_membaca,
    cepat_paham_warna,
    suka_gambar.

% Aturan gaya belajar Auditori
gaya_belajar(auditori) :- 
    senang_mendengar,
    mudah_paham_dari_cerita,
    suka_diskusi.

% Aturan gaya belajar Kinestetik
gaya_belajar(kinestetik) :- 
    senang_praktik,
    suka_bergerak,
    belajar_dengan_melakukan.

% Fakta dinamis (digunakan untuk input dari Python)
:- dynamic senang_membaca/0.
:- dynamic cepat_paham_warna/0.
:- dynamic suka_gambar/0.
:- dynamic senang_mendengar/0.
:- dynamic mudah_paham_dari_cerita/0.
:- dynamic suka_diskusi/0.
:- dynamic senang_praktik/0.
:- dynamic suka_bergerak/0.
:- dynamic belajar_dengan_melakukan/0.
