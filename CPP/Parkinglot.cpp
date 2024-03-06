#include "header.hh"

Parkinglot::Parkinglot() 
{
    this->kapasitas = "";
    this->JumKendaraan = "";
}

Parkinglot::Parkinglot(string namaGarasi, string luas, vector<string> daftarKendaraan, string kapasitas, string JumKendaraan)
    : Garage(namaGarasi, luas, daftarKendaraan)
    {
        this->kapasitas = kapasitas;
        this->JumKendaraan = JumKendaraan;
    }

string Parkinglot::getKapasitas()  
{ 
    return this->kapasitas; 
}

void Parkinglot::setKapasitas(string kapasitas) 
{ 
    this->kapasitas = kapasitas; 
}

string Parkinglot::getJumKendaraan()  
{ 
    return this->JumKendaraan; 
}

void Parkinglot::setJumKendaraan(string JumKendaraan) 
{ 
    this->JumKendaraan = JumKendaraan; 
}

Parkinglot::~Parkinglot() {}
