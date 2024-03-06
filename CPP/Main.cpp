#include "header.hh"

int main() {
    // Creating vehicles
    Car car1("AB 1234 CD", "Toyota", "2022", "Black", "5", "4");
    Car car2("XY 5678 ZW", "Honda", "2023", "White", "4", "4");
    Motorcycle bike1("XX 9999 YY", "Yamaha", "2021", "Red", "Sport", "10L");
    Motorcycle bike2("ZZ 1111 WW", "Suzuki", "2020", "Blue", "Cruiser", "12L");
    
    // Displaying the list of vehicles
    cout << "Daftar Kendaraan:" << endl;
    cout << "+------------+------------+--------+----------------+-------+--------------+--------------+-------------+------------------+" << endl;
    cout << "|    Tipe    | Plat Nomor |  Merk  | Tahun Produksi | Warna | Jumlah Kursi | Jumlah Pintu | Jenis Motor | Kapasitas Tangki |" << endl;
    cout << "+------------+------------+--------+----------------+-------+--------------+--------------+-------------+------------------+" << endl;
    cout << "|    Car     | " << car1.getPlatNomor() << " | " << car1.getMerk() << " | " << car1.getTahunProduk() << "           | " << car1.getWarna() << " | " << car1.getJumKursi() << "            | " << car1.getJumPintu() << "            |             |                  |" << endl;
    cout << "|    Car     | " << car2.getPlatNomor() << " | " << car2.getMerk() << "  | " << car2.getTahunProduk() << "           | " << car2.getWarna() << " | " << car2.getJumKursi() << "            | " << car2.getJumPintu() << "            |             |                  |" << endl;
    cout << "| Motorcycle | " << bike1.getPlatNomor() << " | " << bike1.getMerk() << " | " << bike1.getTahunProduk() << "           | " << bike1.getWarna() << "   |              |              | " << bike1.getJenisMotor() << "       |       " << bike1.getKapasitasTang() << "        |" << endl;
    cout << "| Motorcycle | " << bike2.getPlatNomor() << " | " << bike2.getMerk() << " | " << bike2.getTahunProduk() << "           | " << bike2.getWarna() << "  |              |              | " << bike2.getJenisMotor() << "     |       " << bike2.getKapasitasTang() << "        |" << endl;
    cout << "+------------+------------+--------+----------------+-------+--------------+--------------+-------------+------------------+" << endl << endl;
    
    // Creating parking lot and adding vehicles
    vector<string> vehiclesInParkingLot = {car1.getPlatNomor(), car2.getPlatNomor(), bike1.getPlatNomor(), bike2.getPlatNomor()};
    Parkinglot parkinglot1("Parkiran C", "500m2", vehiclesInParkingLot, "50", "4");
    
    // Displaying parking information
    cout << "Informasi Parkiran:" << endl;
    cout << "Nama Parkiran                           : " << parkinglot1.getNamaGarasi() << endl;
    cout << "Luas Parkiran                           : " << parkinglot1.getLuas() << endl;
    cout << "Kapasitas Parkiran                      : " << parkinglot1.getKapasitas() << endl;
    cout << "Jumlah Kendaraan di Parkiran            : " << parkinglot1.getJumKendaraan() << endl << endl;
    
    // Displaying the list of vehicles in the parking lot
    cout << "Daftar Kendaraan di Parkiran:" << endl;
    int counter = 1;
    for (const auto& vehicle : parkinglot1.getDaftarKendaraan()) {
        cout << counter << ". ";
        if (vehicle == car1.getPlatNomor() || vehicle == car2.getPlatNomor()) {
            cout << "Car";
        } else {
            cout << "Motorcycle";
        }
        cout << "         - Plat Nomor: " << vehicle << "  - Merk: ";
        if (vehicle == car1.getPlatNomor()) {
            cout << car1.getMerk();
        } else if (vehicle == car2.getPlatNomor()) {
            cout << car2.getMerk();
        } else if (vehicle == bike1.getPlatNomor()) {
            cout << bike1.getMerk();
        } else {
            cout << bike2.getMerk();
        }
        cout << endl;
        counter++;
    }
    
    return 0;
}
