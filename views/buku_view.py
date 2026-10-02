import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Konfigurasi Jendela Utama
        self.title("Sistem Manajemen Koleksi Buku")
        self.geometry("800x500")
        ctk.set_appearance_mode("System")  # Menyesuaikan mode terang/gelap OS
        ctk.set_default_color_theme("blue")

        # Grid Weight untuk Layar Responsif
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # 1. FRAME KIRI: FORM INPUT DATA BUKU
        # ==========================================
        self.frame_input = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Judul Form Input
        self.lbl_title = ctk.CTkLabel(
            self.frame_input, 
            text="Form Input Buku", 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.lbl_title.pack(padx=10, pady=(15, 10))

        # Input Judul Buku
        self.entry_judul = ctk.CTkEntry(self.frame_input, placeholder_text="Judul Buku")
        self.entry_judul.pack(padx=10, pady=5, fill="x")

        # Input Penulis
        self.entry_penulis = ctk.CTkEntry(self.frame_input, placeholder_text="Penulis")
        self.entry_penulis.pack(padx=10, pady=5, fill="x")

        # Input Tahun Terbit
        self.entry_tahun = ctk.CTkEntry(self.frame_input, placeholder_text="Tahun Terbit")
        self.entry_tahun.pack(padx=10, pady=5, fill="x")

        # Tombol Simpan Data
        self.btn_simpan = ctk.CTkButton(
            self.frame_input, 
            text="Simpan Data", 
            command=self.on_simpan_click
        )
        self.btn_simpan.pack(padx=10, pady=15, fill="x")

        # ==========================================
        # 2. FRAME KANAN: TABEL DATA (TREEVIEW)
        # ==========================================
        self.frame_tabel = ctk.CTkFrame(self, corner_radius=10)
        self.frame_tabel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Setup Tabel Treeview
        columns = ("id", "judul", "penulis", "tahun")
        self.tree = ttk.Treeview(self.frame_tabel, columns=columns, show="headings")

        # Judul Kolom Tabel
        self.tree.heading("id", text="ID")
        self.tree.heading("judul", text="Judul Buku")
        self.tree.heading("penulis", text="Penulis")
        self.tree.heading("tahun", text="Tahun")

        # Lebar Kolom Tabel
        self.tree.column("id", width=40, anchor="center")
        self.tree.column("judul", width=200)
        self.tree.column("penulis", width=150)
        self.tree.column("tahun", width=80, anchor="center")

        # Layouting Tabel
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def on_simpan_click(self):
        # Callback sementara untuk pengujian statis tampilan
        print("Tombol Simpan diklik! (Pengujian View statis)")

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()