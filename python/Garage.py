class Garage:
    # Konstruktor untuk kelas Garasi.
    def __init__(self, namaGarasi="", luas="", daftarKendaraan=[]):
        """
        Args:
            namaGarasi (str): Nama garasi. Defaultnya kosong.
            luas (str): Luas garasi. Defaultnya kosong.
            daftarKendaraan (list): Daftar kendaraan dalam garasi. Defaultnya kosong.
        """
        self.namaGarasi = namaGarasi
        self.luas = luas
        self.daftarKendaraan = daftarKendaraan
    
    def getNamaGarasi(self):
        # Metode getter untuk mendapatkan nama garasi.
        return self.namaGarasi

    def setNamaGarasi(self, namaGarasi):
        # Metode setter untuk mendapatkan nama garasi.
        self.namaGarasi = namaGarasi

    def getLuas(self):
        # Metode getter untuk mendapatkan luas garasi.
        return self.luas

    def setLuas(self, luas):
        # Metode setter untuk mendapatkan luas garasi.
        self.luas = luas

    def getDaftarKendaraan(self):
        # Metode getter untuk mendapatkan daftar kendaraan dalam garasi.
        return self.daftarKendaraan

    def setDaftarKendaraan(self, daftarKendaraan):
        # Metode setter untuk mengatur daftar kendaraan dalam garasi.
        self.daftarKendaraan = daftarKendaraan
