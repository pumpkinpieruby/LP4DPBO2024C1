from Vehicle import Vehicle

class Car(Vehicle):
    # Konstruktor untuk kelas Mobil, mewarisi dari kelas Vehicle.
    def __init__(self):
        self.JumKursi = ""
        self.JumPintu = ""
        
    def __init__(self, PlatNomor="", Merk="", TahunProduk="", Warna="", JumKursi="", JumPintu=""):
        """
            Argumen:
            PlatNomor (str): Nomor plat mobil. Defaultnya kosong.
            Merk (str): Merek mobil. Defaultnya kosong.
            TahunProduk (str): Tahun produksi mobil. Defaultnya kosong.
            Warna (str): Warna mobil. Defaultnya kosong.
            JumKursi (str): Jumlah kursi dalam mobil. Defaultnya kosong.
            JumPintu (str): Jumlah pintu dalam mobil. Defaultnya kosong.
        """
        super().__init__(PlatNomor, Merk, TahunProduk, Warna)
        self.JumKursi = JumKursi
        self.JumPintu = JumPintu
        
    def getJumKursi(self):
        # Metode getter untuk mendapatkan jumlah kursi dalam mobil.
        return self.JumKursi

    def setJumKursi(self, JumKursi):
        # Metode setter untuk mengatur jumlah kursi dalam mobil.
        self.JumKursi = JumKursi

    def getJumPintu(self):
        # Metode getter untuk mendapatkan jumlah pintu dalam mobil.
        return self.JumPintu

    def setJumPintu(self, JumPintu):
        # Metode setter untuk mengatur jumlah pintu dalam mobil.
        self.JumPintu = JumPintu