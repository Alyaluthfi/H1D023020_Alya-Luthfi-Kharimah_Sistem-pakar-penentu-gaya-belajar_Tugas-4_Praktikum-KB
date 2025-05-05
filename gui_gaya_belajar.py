import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

class GayaBelajarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Penentuan Gaya Belajar")
        self.root.geometry("750x500")
        self.root.configure(bg="#f0f4f8")

        self.prolog = Prolog()
        self.prolog.consult("gaya_belajar.pl")

        self.pertanyaan = [
            ("Apakah kamu senang membaca?", "senang_membaca"),
            ("Apakah kamu cepat paham melalui warna dan simbol?", "cepat_paham_warna"),
            ("Apakah kamu suka melihat gambar saat belajar?", "suka_gambar"),
            ("Apakah kamu senang mendengar penjelasan?", "senang_mendengar"),
            ("Apakah kamu mudah paham dari cerita lisan?", "mudah_paham_dari_cerita"),
            ("Apakah kamu suka berdiskusi dengan orang lain?", "suka_diskusi"),
            ("Apakah kamu senang praktik langsung?", "senang_praktik"),
            ("Apakah kamu suka bergerak saat belajar?", "suka_bergerak"),
            ("Apakah kamu lebih suka belajar dengan melakukan sesuatu?", "belajar_dengan_melakukan"),
        ]

        self.index = 0
        self.fakta_diyakin = []

        # Heading
        self.title_label = tk.Label(root, text="Sistem Pakar Gaya Belajar", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#333")
        self.title_label.pack(pady=15)

        # Pertanyaan
        self.label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=650, justify="center", bg="#f0f4f8", fg="#222")
        self.label.pack(pady=25)

        # Tombol Ya/Tidak
        self.button_frame = tk.Frame(root, bg="#f0f4f8")
        self.button_frame.pack(pady=10)

        self.btn_ya = tk.Button(self.button_frame, text="✔ Ya", command=lambda: self.jawab("ya"),
                                font=("Helvetica", 14), bg="#4caf50", fg="white", padx=20, pady=10, width=10)
        self.btn_ya.grid(row=0, column=0, padx=15)

        self.btn_tidak = tk.Button(self.button_frame, text="✖ Tidak", command=lambda: self.jawab("tidak"),
                                   font=("Helvetica", 14), bg="#f44336", fg="white", padx=20, pady=10, width=10)
        self.btn_tidak.grid(row=0, column=1, padx=15)

        # Tombol reset
        self.btn_reset = tk.Button(root, text="🔁 Reset", command=self.reset,
                                   font=("Helvetica", 12), bg="#2196f3", fg="white", padx=10, pady=5)
        self.btn_reset.pack(pady=20)

        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index < len(self.pertanyaan):
            self.label.config(text=self.pertanyaan[self.index][0])
        else:
            self.inferensi()

    def jawab(self, jawaban):
        fakta = self.pertanyaan[self.index][1]
        if jawaban == "ya":
            self.prolog.assertz(fakta)
            self.fakta_diyakin.append(fakta)
        self.index += 1
        self.tampilkan_pertanyaan()

    def inferensi(self):
        hasil = list(self.prolog.query("gaya_belajar(X)."))
        if hasil:
            gaya = hasil[0]["X"]
            messagebox.showinfo("Hasil", f"Gaya belajar kamu adalah: {gaya.upper()}")
        else:
            messagebox.showwarning("Hasil", "Gaya belajar kamu tidak dapat ditentukan.")
        self.label.config(text="Klik Reset untuk memulai kembali.")

    def reset(self):
        for fakta in self.fakta_diyakin:
            self.prolog.retract(fakta)
        self.fakta_diyakin.clear()
        self.index = 0
        self.tampilkan_pertanyaan()

if __name__ == "__main__":
    root = tk.Tk()
    app = GayaBelajarGUI(root)
    root.mainloop()
