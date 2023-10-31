produk1 = {
    'brand' : 'toyota',
    'type' : 'SUV',
    'year' : 2020,
    'model' : 'CHR'
}

produk2 = {
    'brand' : 'tesla',
    'type' : 'sedan',
    'year' : 2021,
    'model' : 'Model S'
}

produk3 = {
    'brand' : 'tesla',
    'type' : 'sedan',
    'year' : 2021,
    'model' : 'Model 3'
}

warehouse1 = [produk1,produk2,produk3]

# print(produk1['brand'])
produk4 = {
    'brand' : 'mitsubishi',
    'type' : 'sedan',
    'year' : 2021,
    'model' : 'lancer'
}

# print(produk4)

#class/ kelas/ object
# seperti kerangka atau dasar dari sesuatu
# seorang developer perumahan, dia punya model rumahnya, ada yang 36 ada yang 45 ada yang 54

#example

class car:
    def __init__(self, brand, model, year, type):#ini adalah constructor
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type

    def print(self): #method class
        print(self.brand, self.model, self.year, self.type)

mobil = car('mclaren', 'artura', 2022,'sportcar')
print('brand', mobil.brand, 'year', mobil.year, 'type', mobil.type,'model', mobil.model)
mobil.print()
#input new product tidak perlu lagi membuat statement print, hanya memanggil method class print saja

# tugas buatlah kelas untuk hewan
# atribut nama, famili, spesies, cara bergerak, suara, 

#metodenya
#print detailnya di paragraf

#method suara "guk-guk"
# anjing.suara() return guk-guk