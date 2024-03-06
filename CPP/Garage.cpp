#include "header.hh"

Garage::Garage() 
{
    this->namaGarasi = "";
    this->luas = "";
    this->daftarKendaraan = {}; //
}

Garage::Garage(string namaGarasi, string luas, vector<string> daftarKendaraan)
    {
        this->namaGarasi = namaGarasi;
        this->luas = luas;
        this->daftarKendaraan = daftarKendaraan;
    }

string Garage::getNamaGarasi()  
{ 
    return this->namaGarasi; 
}

void Garage::setNamaGarasi(string namaGarasi) 
{ 
    this->namaGarasi = namaGarasi; 
}

string Garage::getLuas()  
{ 
    return this->luas; 
}

void Garage::setLuas(string luas) 
{ 
    this->luas = luas; 
}

vector<string> Garage::getDaftarKendaraan()  
{ 
    return this->daftarKendaraan; 
}

void Garage::setDaftarKendaraan(vector<string> daftarKendaraan) 
{ 
    this->daftarKendaraan = daftarKendaraan; 
}

Garage::~Garage() {}
