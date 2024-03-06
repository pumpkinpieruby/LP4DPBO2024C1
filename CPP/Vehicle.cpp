#include "header.hh"

Vehicle::Vehicle() 
{
    this->PlatNomor = "";
    this->Merk = "";
    this->TahunProduk = "";
    this->Warna = "";
}

Vehicle::Vehicle(string PlatNomor, string Merk, string TahunProduk, string Warna) 
{
    this->PlatNomor = PlatNomor;
    this->Merk = Merk;
    this->TahunProduk = TahunProduk;
    this->Warna = Warna;
}

string Vehicle::getPlatNomor()  
{ 
    return this->PlatNomor; 
}

void Vehicle::setPlatNomor(string platNomor) 
{ 
    this->PlatNomor = platNomor; 
}

string Vehicle::getMerk()  
{ 
    return this->Merk; 
}

void Vehicle::setMerk(string merk) 
{ 
    this->Merk = merk; 
}

string Vehicle::getTahunProduk()  
{ 
    return this->TahunProduk; 
}

void Vehicle::setTahunProduk(string tahunProduk) 
{ 
    this->TahunProduk = tahunProduk; 
}

string Vehicle::getWarna()  
{ 
    return this->Warna; 
}

void Vehicle::setWarna(string warna) 
{ 
    this->Warna = warna; 
}

Vehicle::~Vehicle() {}
