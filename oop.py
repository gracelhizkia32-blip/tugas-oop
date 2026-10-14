```python
class Produk:
    def __init__(self, nama_produk, harga_produk):
        self.nama_produk = nama_produk
        self.harga_produk = harga_produk

    def tampilkan_info(self):
        print("Nama Produk :", self.nama_produk)
        print("Harga Produk : Rp{:,.0f}".format(
            self.harga_produk
        ).replace(",", "."))

    def hitung_total(self, jumlah_beli):
        return self.harga_produk * jumlah_beli

    def hitung_diskon(self, total_pembelian):
        if total_pembelian > 5000:
            return total_pembelian * 0.05
        else:
            return 0


jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

total_seluruh = 0

for i in range(jumlah_produk):
    print("\n=== Produk ke-", i + 1, "===")

    nama_produk = input("Nama produk  : ")
    harga_produk = int(input("Harga produk : Rp"))
    jumlah_beli = int(input("Jumlah beli  : "))

    produk = Produk(nama_produk, harga_produk)

    print("\n--- Informasi Produk ---")
    produk.tampilkan_info()

    total_produk = produk.hitung_total(jumlah_beli)

    print("Total pembelian : Rp{:,.0f}".format(
        total_produk
    ).replace(",", "."))

    total_seluruh += total_produk

diskon = produk.hitung_diskon(total_seluruh)

total_bayar = total_seluruh - diskon

print("\n=== HASIL PEMBELIAN ===")
print("Total Pembelian : Rp{:,.0f}".format(
    total_seluruh
).replace(",", "."))

print("Diskon 5%       : Rp{:,.0f}".format(
    diskon
).replace(",", "."))

print("Total Bayar     : Rp{:,.0f}".format(
    total_bayar
).replace(",", "."))
```