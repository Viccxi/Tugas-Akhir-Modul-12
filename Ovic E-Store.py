import tkinter as tk
from tkinter import ttk, messagebox

# Inisialisasi data produk
produk = {
    'Laptop': 10000000,
    'Smartphone': 5000000,
    'Headphone': 1000000,
    'Charger': 500000,
    'Printer': 2000000,
    'Mouse': 300000,
    'Keyboard': 400000,
    'Monitor': 1500000,
    'Speaker': 800000,
    'External HDD': 1200000,
    'Tablet': 3500000,
    'Camera': 6000000,
    'Gaming Console': 4500000,
    'Desk Lamp': 250000,
    'USB Flash Drive': 150000,
    'Wireless Router': 800000,
    'Fitness Tracker': 900000,
    'Portable Speaker': 700000,
    'Bluetooth Earphones': 400000,
    'Smartwatch': 3000000,
    'Electric Toothbrush': 200000,
    'Air Purifier': 1800000,
    'Coffee Maker': 1200000,
    'Vacuum Cleaner': 2500000,
    'Hair Dryer': 500000,
    'Rice Cooker': 800000,
    'Toaster': 300000,
    'Blender': 700000,
    'Drone': 4000000,
    'Projector': 3500000,
    'Digital Camera': 2500000,
    'Power Bank': 300000,
    'Action Camera': 1800000,
    'External SSD': 2800000,
    'Gaming Mouse': 600000,
    'Wireless Earbuds': 1500000,
    'Robot Vacuum': 3500000,
    'Smart Thermostat': 900000,
    'Smart Doorbell': 1200000,
    'E-book Reader': 1000000,
    'Instant Pot': 1800000,
    'VR Headset': 3000000,
    'Wireless Printer': 2000000,
    'Electric Kettle': 600000,
    'Soundbar': 1200000,
    'Computer Microphone': 500000,
    'Smart Scale': 800000,
    'Car Dash Cam': 1000000,
    'Coffee Grinder': 400000,
    'Air Fryer': 1800000,
    'Wireless Headphones': 2500000,
    'Digital Drawing Tablet': 3500000,
    'Smart TV': 7000000,
    'Electric Scooter': 3000000,
    'Security Camera System': 4000000,
    'Cordless Drill': 1200000,
    'Electric Blanket': 900000,
    'Wireless Gaming Mouse': 1800000,
    'Smart Light Bulbs': 500000,
    'Digital Photo Frame': 800000,
    'Portable Air Conditioner': 2500000,
    'Wireless Charging Dock': 1500000,
    'Digital Alarm Clock': 300000,
    'Mini Fridge': 1200000,
    'Electric Skateboard': 3500000,
    'Robot Lawn Mower': 5000000,
    'Smart Ceiling Fan': 1800000,
    'Home Theater System': 8000000,
    'Robot Bartender': 6000000,
    'Smart Coffee Machine': 2000000,
    'Wireless Meat Thermometer': 500000,
    'Smart Window Blinds': 3000000,
    'UV Sanitizer': 1500000,
    'Pet Camera': 1200000,
    'Voice Translator': 1000000,
    'Smart Mirror': 4000000,
    'Smart Garden': 2500000,
    'Smart Water Bottle': 800000,
    'Smart Air Fryer': 2000000,
    'Foldable Electric Bike': 3500000,
    'Solar Power Bank': 1500000,
    'Portable Espresso Maker': 1000000,
    'Wireless Baby Monitor': 1800000,
    'AI-Powered Backpack': 500000,
}

kategori_produk = {
    'Komputer': ['Laptop', 'Desktop', 'Mouse', 'Keyboard', 'Monitor', 'Printer', 'External HDD', 'Tablet'],
    'Gadget': ['Smartphone', 'Smartwatch', 'Bluetooth Earphones', 'Fitness Tracker', 'Power Bank', 'Wireless Earbuds'],
    'Elektronik Rumah Tangga': ['Desk Lamp', 'Air Purifier', 'Coffee Maker', 'Vacuum Cleaner', 'Hair Dryer'],
    'Dapur': ['Rice Cooker', 'Toaster', 'Blender', 'Coffee Grinder', 'Air Fryer'],
    'Kamera': ['Camera', 'Digital Camera', 'Action Camera'],
    'Gaming': ['Gaming Console', 'Gaming Mouse'],
    'Peralatan Elektronik': ['Charger', 'External SSD', 'Wireless Router', 'Computer Microphone', 'Smart Thermostat'],
    'Smart Home': ['Smart Doorbell', 'Smart TV', 'Smart Scale', 'Smart Light Bulbs', 'Smart Mirror'],
    'Perkakas Elektronik': ['Electric Toothbrush', 'Electric Kettle', 'Soundbar', 'Robot Vacuum'],
    'Outdoor': ['Drone', 'Digital Drawing Tablet', 'Electric Scooter', 'Portable Espresso Maker'],
    'Keamanan': ['Security Camera System', 'Car Dash Cam', 'AI-Powered Backpack'],
    'Peralatan Rumah': ['Electric Blanket', 'Mini Fridge', 'Portable Air Conditioner', 'Cordless Drill'],
    'Hiburan': ['Speaker', 'Portable Speaker', 'Projector', 'Soundbar', 'Home Theater System'],
    'Lainnya': ['USB Flash Drive', 'Wireless Printer', 'Instant Pot', 'E-book Reader', 'VR Headset']
}



#Ongkir
ongkir = {
    'Jakarta': 40000,
    'Bandung': 35000,
    'Yogyakarta': 5000,
    'Surabaya': 35000,
    'Denpasar': 60000,
    'Medan': 80000,
    'Semarang': 10000,
    'Makassar': 90000,
    'Palembang': 30000,
    'Balikpapan': 75000,
    'Padang': 60000,
    'Manado': 120000,
    'Pekanbaru': 55000,
    'Banjarmasin': 85000,
    'Malang': 20000,
    'Purwokerto': 15000,
    'Pontianak': 55000,
    'Samarinda': 45000,
    'Banda Aceh': 75000,
    'Jayapura': 90000,
    'Ambon': 80000,
    'Manokwari': 85000,
    'Ternate': 95000,
    'Mamuju': 70000,
    'Tarakan': 50000,
    'Kendari': 60000,
    'Gorontalo': 55000,
    'Palangkaraya': 45000,
    'Tanjung Pinang': 65000,
}

lokasi = 'Yogyakarta'  # Lokasi default

def tampilkan_produk_kategori():
    kategori = dropdown_kategori.get()
    list_produk.delete(0, tk.END)
    for category, items in kategori_produk.items():
        if kategori == category:
            for item in items:
                if item in produk:
                    harga = produk[item]
                    formatted_harga = "{:,.0f}".format(harga).replace(",", ".")
                    list_produk.insert(tk.END, f"{item}: Rp {formatted_harga}")


# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    list_produk.delete(0, tk.END)
    for item, harga in produk.items():
        formatted_harga = "{:,.0f}".format(harga).replace(",", ".")
        list_produk.insert(tk.END, f"{item}: Rp {formatted_harga}")

def tambah_ke_keranjang():
    pilihan = list_produk.get(tk.ACTIVE)
    qty = int(entry_qty.get())

    if qty > 0:
        produk_terpilih = pilihan.split(':')[0].strip()
        harga_produk = produk[produk_terpilih] * qty
        biaya_ongkir = ongkir[lokasi]
        total_harga_produk = harga_produk + biaya_ongkir

        formatted_harga_produk = "Rp {:,.0f}".format(harga_produk).replace(",", ".")
        formatted_total_harga_produk = "Rp {:,.0f}".format(total_harga_produk).replace(",", ".")

        keranjang.insert('', tk.END, values=(produk_terpilih, qty, formatted_total_harga_produk))
        update_total_keranjang()
    else:
        label_total_keranjang.config(text="Jumlah harus lebih besar dari 0.")

def update_total_keranjang():
    total_harga_keranjang = sum(float(keranjang.item(item, 'values')[2].split()[1].replace(".", "").replace(",", "")) for item in keranjang.get_children())
    formatted_total_harga_keranjang = "Rp {:,.0f}".format(total_harga_keranjang).replace(",", ".")
    label_total_keranjang.config(text=f"Total Pembelian: {formatted_total_harga_keranjang}")

def hapus_dari_keranjang():
    selected_item = keranjang.selection()[0]  # Mengambil item yang dipilih
    keranjang.delete(selected_item)  # Menghapus item dari keranjang yang dipilih
    update_total_keranjang()  # Memperbarui total harga setelah penghapusan

def ganti_lokasi():
    global lokasi
    lokasi = dropdown_lokasi.get()
    label_lokasi.config(text=f"Lokasi Pengiriman: {lokasi}")

    # Memperbarui nilai biaya ongkir saat lokasi diubah
    biaya_ongkir = ongkir[lokasi]

    # Memperbarui nilai biaya ongkir untuk setiap item dalam keranjang
    for item in keranjang.get_children():
        qty = int(keranjang.item(item, 'values')[1])
        produk_terpilih = keranjang.item(item, 'values')[0]
        harga_produk = produk[produk_terpilih] * qty
        total_harga_produk = harga_produk + biaya_ongkir
        formatted_total_harga_produk = "Rp {:,.0f}".format(total_harga_produk).replace(",", ".")
        keranjang.item(item, values=(produk_terpilih, qty, formatted_total_harga_produk))

    update_total_keranjang()  # Memperbarui total harga setelah perubahan lokasi


def proses_pembayaran():
    # Memproses pembayaran berdasarkan metode yang dipilih
    metode_pembayaran = dropdown_metode.get()

    if metode_pembayaran == "Dana":
        # Proses pembayaran dengan metode Dana
        print("Pembayaran menggunakan Dana")
    elif metode_pembayaran == "OVO":
        # Proses pembayaran dengan metode OVO
        print("Pembayaran menggunakan OVO")
    elif metode_pembayaran == "Gopay":
        # Proses pembayaran dengan metode Gopay
        print("Pembayaran menggunakan Gopay")
    elif metode_pembayaran == "BNI":
        # Proses pembayaran dengan metode BNI
        print("Pembayaran menggunakan BNI")
    elif metode_pembayaran == "BRI":
        # Proses pembayaran dengan metode BRI
        print("Pembayaran menggunakan BRI")
    elif metode_pembayaran == "Bank Mandiri":
        # Proses pembayaran dengan metode Bank Mandiri
        print("Pembayaran menggunakan Bank Mandiri")


def proses_checkout():
    confirm = messagebox.askokcancel("Konfirmasi Pembelian", "Anda yakin ingin melakukan pembelian?")
    if confirm:
        # Mengumpulkan informasi dari keranjang
        items = [(keranjang.item(item, 'values')[0], keranjang.item(item, 'values')[1], keranjang.item(item, 'values')[2]) for item in keranjang.get_children()]
        total_harga = label_total_keranjang.cget("text")

        # Menyiapkan teks nota
        nota = f"{'='*50}\n{'Nota Pembelian':^50}\n{'='*50}\n\n"
        nota += f"{'Nama Produk':<25}{'Jumlah':<10}{'Harga':<15}\n"
        nota += f"{'-'*50}\n"
        for item in items:
            nota += f"{item[0]:<25}{item[1]:<10}{item[2]}\n"
        nota += f"\n{'-'*50}\nTotal Pembelian: {total_harga}\n{'-'*50}\n\n"
        nota += "Pesanan sedang Diproses dan akan Dikirim ke Lokasi anda\nTerima Kasih sudah Belanja di Ovic E-Store"

        # Menampilkan nota dalam pesan box
        messagebox.showinfo("Nota Pembelian", nota)

        # Mengosongkan keranjang setelah pembelian
        keranjang.delete(*keranjang.get_children())
        update_total_keranjang()

def generate_nota():
    nota = f"===== Nota Pembelian =====\n"
    total_harga = 0

    for item in keranjang.get_children():
        produk_terpilih = keranjang.item(item, 'values')[0]
        qty = int(keranjang.item(item, 'values')[1])
        harga_produk = produk[produk_terpilih]
        total_harga_item = harga_produk * qty

        formatted_total_harga_item = "Rp {:,.0f}".format(total_harga_item).replace(",", ".")
        nota += f"{produk_terpilih} - {qty} pcs - {formatted_total_harga_item}\n"
        total_harga += total_harga_item

    formatted_total_harga = "Rp {:,.0f}".format(total_harga).replace(",", ".")
    nota += f"Total Harga: {formatted_total_harga}\n\n"
    nota += "Pesanan sedang Diproses dan akan Dikirim ke Lokasi anda\n"
    nota += "Terima Kasih sudah Belanja di Ovic E-Store"

    # Menampilkan nota dalam messagebox
    tk.messagebox.showinfo("Nota Pembelian", nota)

    # Bersihkan keranjang setelah pembelian
    keranjang.delete(*keranjang.get_children())
    update_total_keranjang()


# Setup GUI
root = tk.Tk()
root.title("Ovic E-Store")

frame_produk = tk.Frame(root)
frame_produk.pack(side=tk.LEFT, padx=10, pady=10)

frame_keranjang = tk.Frame(root)
frame_keranjang.pack(side=tk.RIGHT, padx=10, pady=10)

label_produk = tk.Label(frame_produk, text="Daftar Produk")
label_produk.pack()

label_kategori = tk.Label(frame_produk, text="Pilih Kategori:")
label_kategori.pack()

kategori_options = sorted(list(kategori_produk.keys()))
dropdown_kategori = tk.StringVar(frame_produk)
dropdown_kategori.set(kategori_options[0])
dropdown_kategori_menu = tk.OptionMenu(frame_produk, dropdown_kategori, *kategori_options)
dropdown_kategori_menu.pack()

btn_tampilkan_kategori = tk.Button(frame_produk, text="Tampilkan Kategori", command=tampilkan_produk_kategori)
btn_tampilkan_kategori.pack()

list_produk = tk.Listbox(frame_produk, width=30, height=10)
list_produk.pack()

tampilkan_produk()

label_qty = tk.Label(frame_produk, text="Jumlah:")
label_qty.pack()
entry_qty = tk.Entry(frame_produk)
entry_qty.pack()

btn_tambah = tk.Button(frame_produk, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
btn_tambah.pack()

label_lokasi = tk.Label(frame_produk, text=f"Lokasi Pengiriman: {lokasi}")
label_lokasi.pack()

lokasi_options = list(ongkir.keys())
dropdown_lokasi = tk.StringVar(frame_produk)
dropdown_lokasi.set(lokasi_options[0])
dropdown_lokasi_menu = tk.OptionMenu(frame_produk, dropdown_lokasi, *lokasi_options)
dropdown_lokasi_menu.pack()

btn_ganti_lokasi = tk.Button(frame_produk, text="Ubah Lokasi", command=ganti_lokasi)
btn_ganti_lokasi.pack()

label_keranjang = tk.Label(frame_keranjang, text="Keranjang")
label_keranjang.pack()

columns = ('Produk', 'Qty', 'Harga')
keranjang = ttk.Treeview(frame_keranjang, columns=columns, show='headings')

for col in columns:
    keranjang.heading(col, text=col)
    keranjang.column(col, anchor='center')

keranjang.pack()

btn_hapus = tk.Button(frame_keranjang, text="Hapus dari Keranjang", command=hapus_dari_keranjang)
btn_hapus.pack()

label_total_keranjang = tk.Label(frame_keranjang, text="Total Pembelian: ")
label_total_keranjang.pack()

label_metode_pembayaran = tk.Label(frame_produk, text="Metode Pembayaran:")
label_metode_pembayaran.pack()

# Daftar metode pembayaran yang ditampilkan dalam dropdown
metode_options = ["Dana", "OVO", "Gopay", "BNI", "BRI", "Bank Mandiri"]
dropdown_metode = tk.StringVar(frame_produk)
dropdown_metode.set(metode_options[0])
dropdown_metode_menu = tk.OptionMenu(frame_produk, dropdown_metode, *metode_options)
dropdown_metode_menu.pack()

btn_proses_pembayaran = tk.Button(frame_produk, text="Proses Pembayaran", command=proses_pembayaran)
btn_proses_pembayaran.pack()

#Checkoutbutton
btn_checkout = tk.Button(frame_produk, text="Checkout", command=proses_checkout)
btn_checkout.pack()

root.mainloop()