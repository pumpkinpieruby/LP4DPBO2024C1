#include "header.hh"

Motorcycle::Motorcycle() 
{
    this->JenisMotor = "";
    this->KapasitasTang = "";
}

Motorcycle::Motorcycle(string platNomor, string merk, string tahunProduk, string warna, string jenisMotor, string kapasitasTang)
    : Vehicle(platNomor, merk, tahunProduk, warna)
    {
        this->JenisMotor= jenisMotor;
        this->KapasitasTang= kapasitasTang;
    }

string Motorcycle::getJenisMotor() 
{ 
    return this->JenisMotor; 
}

void Motorcycle::setJenisMotor(string jenisMotor) 
{ 
    this->JenisMotor = jenisMotor; 
}

string Motorcycle::getKapasitasTang()  
{ 
    return this->KapasitasTang; 
}

void Motorcycle::setKapasitasTang(string kapasitasTang) 
{ 
    this->KapasitasTang = kapasitasTang; 
}

Motorcycle::~Motorcycle() {}
