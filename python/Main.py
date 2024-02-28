from tabulate import tabulate
from Car import Car
from Motorcycle import Motorcycle
from Parkinglot import Parkinglot

def print_vehicle_info(vehicles):
    """
    Fungsi untuk mencetak informasi kendaraan.

    Args:
        vehicles (list): Daftar kendaraan yang akan dicetak informasinya.
    """
    vehicle_data = []

    # Mengumpulkan informasi kendaraan dalam format yang sesuai
    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            vehicle_data.append([
                "Car",
                vehicle.getPlatNomor(),
                vehicle.getMerk(),
                vehicle.getTahunProduk(),
                vehicle.getWarna(),
                vehicle.getJumKursi(),
                vehicle.getJumPintu(),
                "",  # Kolom untuk jenis motor kosong untuk mobil
                ""   # Kolom untuk kapasitas tangki kosong untuk mobil
            ])
        elif isinstance(vehicle, Motorcycle):
            vehicle_data.append([
                "Motorcycle",
                vehicle.getPlatNomor(),
                vehicle.getMerk(),
                vehicle.getTahunProduk(),
                vehicle.getWarna(),
                "",  # Kolom untuk jumlah kursi kosong untuk sepeda motor
                "",  # Kolom untuk jumlah pintu kosong untuk sepeda motor
                vehicle.getJenisMotor(),
                vehicle.getKapasitasTang()
            ])

    headers = ["Tipe", "Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jumlah Kursi", "Jumlah Pintu", "Jenis Motor", "Kapasitas Tangki"]

    # Mencetak informasi kendaraan menggunakan tabulate
    print("\nDaftar Kendaraan:")
    print(tabulate(vehicle_data, headers=headers, tablefmt="pretty"))

def print_parkinglot_info(parkinglot):
    """
    Fungsi untuk mencetak informasi parkiran.

    Args:
        parkinglot (Parkinglot): Objek parkiran yang akan dicetak informasinya.
    """
    print("\nInformasi Parkiran:")
    print(f"{'Nama Parkiran':<40}: {parkinglot.getNamaGarasi()}")
    print(f"{'Luas Parkiran':<40}: {parkinglot.getLuas()}")
    print(f"{'Kapasitas Parkiran':<40}: {parkinglot.getKapasitas()}")
    print(f"{'Jumlah Kendaraan di Parkiran':<40}: {len(parkinglot.getDaftarKendaraan())}")

def print_daftar_kendaraan(parkinglot):
    """
    Fungsi untuk mencetak daftar kendaraan di parkiran.

    Args:
        parkinglot (Parkinglot): Objek parkiran yang akan dicetak daftar kendaraannya.
    """
    print("\nDaftar Kendaraan di Parkiran:")
    for i, vehicle in enumerate(parkinglot.getDaftarKendaraan(), 1):
        print(f"{i}. {type(vehicle).__name__:<11} - Plat Nomor: {vehicle.getPlatNomor():<12}- Merk: {vehicle.getMerk()}")

def main():
    # Membuat instance kendaraan
    car1 = Car("AB 1234 CD", "Toyota", "2022", "Black", "5", "4")
    car2 = Car("XY 5678 ZW", "Honda", "2023", "White", "4", "4")
    motorcycle1 = Motorcycle("XX 9999 YY", "Yamaha", "2021", "Red", "Sport", "10L")
    motorcycle2 = Motorcycle("ZZ 1111 WW", "Suzuki", "2020", "Blue", "Cruiser", "12L")

    # Membuat instance parkiran
    parkiran = Parkinglot("Parkiran C", "500m2", [car1, car2, motorcycle1, motorcycle2], "50", "4")
    
    # Cetak informasi kendaraan
    print_vehicle_info([car1, car2, motorcycle1, motorcycle2])

    # Cetak informasi parkiran
    print_parkinglot_info(parkiran)

    # Cetak daftar kendaraan di parkiran
    print_daftar_kendaraan(parkiran)

if __name__ == "__main__":
    main()
