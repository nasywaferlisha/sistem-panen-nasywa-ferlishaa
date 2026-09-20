hasil_panen = [10, 15, 20, 12]

total = sum(hasil_panen)

def hitung_diskon(total, diskon):
    return total - (total * diskon / 100)

diskon = 10
total_setelah_diskon = hitung_diskon(total, diskon)

print("Hasil panen:", hasil_panen)
print("Total hasil panen:", total, "kg")
print("Diskon:", diskon, "%")
print("Total setelah diskon:", total_setelah_diskon, "kg")
