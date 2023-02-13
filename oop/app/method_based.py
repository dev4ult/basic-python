def hitung_harga(harga_satuan, jumlah_barang: int):
    return harga_satuan * jumlah_barang

def say_hello(name : str) -> None:
    print('Hello ' + name)

if __name__ == '__main__':
    total_harga = hitung_harga(1000, 5)
    print(total_harga)

