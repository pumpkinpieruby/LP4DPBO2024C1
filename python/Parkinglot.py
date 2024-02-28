from Garage import Garage

class Parkinglot(Garage):
    #  Konstruktor untuk kelas Parkinglot, mewarisi dari kelas Garage.
    def __init__(self, namaGarasi="", luas="", daftarKendaraan=[], kapasitas="", JumKendaraan=""):
        """
        Args:
            namaGarasi (str): Nama garasi. Defaultnya kosong.
            luas (str): Luas garasi. Defaultnya kosong.
            daftarKendaraan (list): Daftar kendaraan dalam garasi. Defaultnya kosong.
            kapasitas (str): Kapasitas parkir. Defaultnya kosong.
            JumKendaraan (str): Jumlah kendaraan yang terparkir. Defaultnya kosong.
        """
        super().__init__(namaGarasi, luas, daftarKendaraan)
        self.kapasitas = kapasitas
        self.JumKendaraan = JumKendaraan

    def getKapasitas(self):
        # Metode getter untuk mendapatkan kapasitas parkir.
        return self.kapasitas

    def setKapasitas(self, kapasitas):
        # Metode setter untuk mendapatkan kapasitas parkir
        self.kapasitas = kapasitas

    def getJumKendaraan(self):
        # Metode getter untuk mendapatkan jumlah kendaraan yang terparkir.
        return self.JumKendaraan

    def setJumKendaraan(self, JumKendaraan):
        # Metode setter untuk mengatur jumlah kendaraan yang terparkir.
        self.JumKendaraan = JumKendaraan
