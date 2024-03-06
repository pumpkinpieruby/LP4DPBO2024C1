#include "header.hh"

Car::Car() 
{
    this->JumKursi = "";
    this->JumPintu = "";
}

Car::Car(string platNomor, string merk, string tahunProduk, string warna, string jumKursi, string jumPintu)
    : Vehicle(platNomor, merk, tahunProduk, warna)
    {
        this->JumKursi = jumKursi;
        this->JumPintu = jumPintu;
    }

string Car::getJumKursi()
{
    return this->JumKursi; 
}

void Car::setJumKursi(string jumKursi) 
{ 
    this->JumKursi = jumKursi; 
}

string Car::getJumPintu()  
{ 
    return this->JumPintu; 
}

void Car::setJumPintu(string jumPintu) 
{ 
    this->JumPintu = jumPintu; 
}

Car::~Car() {}
