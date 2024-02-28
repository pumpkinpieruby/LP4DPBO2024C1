class Vehicle:
    def __init__(self):
        self.PlatNomor = ""
        self.Merk = ""
        self.TahunProduk = ""
        self.Warna = ""
        
    def __init__(self, PlatNomor="", Merk="", TahunProduk="", Warna=""):
        """
        Konstruktor untuk kelas Kendaraan.

        Argumen:
            PlatNomor (str): Nomor plat kendaraan. Defaultnya kosong.
            Merk (str): Merek kendaraan. Defaultnya kosong.
            TahunProduk (str): Tahun produksi kendaraan. Defaultnya kosong.
            Warna (str): Warna kendaraan. Defaultnya kosong.
        """
        self.PlatNomor = PlatNomor
        self.Merk = Merk
        self.TahunProduk = TahunProduk
        self.Warna = Warna
    
    def getPlatNomor(self):
        # Metode getter untuk mendapatkan nomor plat kendaraan.
        return self.PlatNomor
    
    def setPlatNomor(self, PlatNomor):
        # Metode setter untuk mengatur nomor plat kendaraan.
        self.PlatNomor = PlatNomor
        
    def getMerk(self):
        # Metode getter untuk mendapatkan merek kendaraan.
        return self.Merk
    
    def setMerk(self, Merk):
        # Metode setter untuk mengatur merek kendaraan.
        self.Merk = Merk
        
    def getTahunProduk(self):
        # Metode getter untuk mendapatkan tahun produksi kendaraan.
        return self.TahunProduk
    
    def setTahunProduksi(self, TahunProduk):
        # Metode setter untuk mengatur tahun produksi kendaraan.
        self.TahunProduk = TahunProduk
    
    def getWarna(self):
        # Metode getter untuk mendapatkan warna kendaraan.
        return self.Warna
    
    def setWarna(self, Warna):
        # Metode setter untuk mengatur warna kendaraan.
        self.Warna = Warna