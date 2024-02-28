from Vehicle import Vehicle

class Motorcycle(Vehicle):
    # Konstruktor untuk kelas Motor, mewarisi dari kelas Vehicle.
    def __init__(self):
        self.JenisMotor = ""
        self.KapasitasTang = "" # kapasitas tangki
    
    def __init__(self, PlatNomor="", Merk="", TahunProduk="", Warna="", JenisMotor="", KapasitasTang=""):
        """
        Args:
            PlatNomor (str): Nomor plat motor. Defaultnya kosong.
            Merk (str): Merek motor. Defaultnya kosong.
            TahunProduk (str): Tahun produksi motor. Defaultnya kosong.
            Warna (str): Warna motor. Defaultnya kosong.
            JenisMotor (str): Jenis motor. Defaultnya kosong.
            KapasitasTang (str): Kapasitas tangki motor. Defaultnya kosong.
        """
        super().__init__(PlatNomor, Merk, TahunProduk, Warna)
        self.JenisMotor = JenisMotor
        self.KapasitasTang = KapasitasTang
    
    def getJenisMotor(self):
        # Metode getter untuk mendapatkan jenis motor.
        return self.JenisMotor

    def setJenisMotor(self, JenisMotor):
        # Metode setter untuk mendapatkan jenis motor.
        self.JenisMotor = JenisMotor

    def getKapasitasTang(self):
        # Metode getter untuk mendapatkan kapasitas tangki
        return self.KapasitasTang

    def setKapasitasTang(self, KapasitasTang):
        # Metode setter untuk mendapatkan kapasitas tangki
        self.KapasitasTang = KapasitasTang