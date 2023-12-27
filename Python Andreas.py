class MenuMakanan:
    def __init__ (self):
        self.menu = {}
    
    def tambah_menu(self, nama, harga):
        self.menu[nama] = harga

    def tampilkan_menu(self):
        print("Menu Makanan:")
        for nama, harga in self.menu.items():
            print(f"{nama}: Rp {harga}")

# Contoh penggunaan
menu_makanan = MenuMakanan()
menu_makanan.tambah_menu("Nasi Goreng", 25000)
menu_makanan.tambah_menu("Mie Ayam", 20000)
menu_makanan.tambah_menu("Soto Betawi", 30000)

menu_makanan.tampilkan_menu()