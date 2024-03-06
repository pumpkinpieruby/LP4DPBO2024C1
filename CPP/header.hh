
#include <bits/stdc++.h>

using namespace std;

class Vehicle {
private:
    string PlatNomor;
    string Merk;
    string TahunProduk;
    string Warna;

public:
    Vehicle();
    Vehicle(string PlatNomor);
    Vehicle(string PlatNomor, string Merk);
    Vehicle(string PlatNomor, string Merk, string TahunProduk);
    Vehicle(string PlatNomor, string Merk, string TahunProduk, string Warna);
    string getPlatNomor();
    void setPlatNomor(string platNomor);
    string getMerk();
    void setMerk(string merk);
    string getTahunProduk();
    void setTahunProduk(string tahunProduk);
    string getWarna();
    void setWarna(string warna);
    ~Vehicle();

};

class Car : public Vehicle {
private:
    string JumKursi;
    string JumPintu;

public:
    Car();
    Car(string platNomor, string merk, string tahunProduk, string warna, string jumKursi, string jumPintu);
    string getJumKursi();
    void setJumKursi(string jumKursi);
    string getJumPintu();
    void setJumPintu(string jumPintu);
    ~Car();
};

class Motorcycle : public Vehicle {
private:
    string JenisMotor;
    string KapasitasTang;

public:
    Motorcycle();
    Motorcycle(string platNomor, string merk, string tahunProduk, string warna, string jenisMotor, string kapasitasTang);
    string getJenisMotor();
    void setJenisMotor(string jenisMotor);
    string getKapasitasTang();
    void setKapasitasTang(string kapasitasTang);
    ~Motorcycle();
};

class Garage {
private:
    string namaGarasi;
    string luas;
    vector<string> daftarKendaraan;

public:
    Garage();
    Garage(string namaGarasi, string luas, vector<string> daftarKendaraan);
    string getNamaGarasi();
    void setNamaGarasi(string namaGarasi);
    string getLuas();
    void setLuas(string luas);
    vector<string> getDaftarKendaraan();
    void setDaftarKendaraan(vector<string> daftarKendaraan);
    ~Garage();
};

class Parkinglot : public Garage {
private:
    string kapasitas;
    string JumKendaraan;

public:
    Parkinglot();
    Parkinglot(string namaGarasi, string luas, vector<string> daftarKendaraan, string kapasitas, string JumKendaraan);
    string getKapasitas();
    void setKapasitas(string kapasitas);
    string getJumKendaraan();
    void setJumKendaraan(string JumKendaraan);
    ~Parkinglot();
};
