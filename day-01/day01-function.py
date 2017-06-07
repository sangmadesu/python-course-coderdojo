# Ternary
nilai = 60
lulus = True if nilai > 50 else False
print(lulus)

# Fungsi mengecek kelulusan
print('Program mengecek kelulusan')
def cek_kelulusan(nilai):
	print('Cek fungsi kelulusan')
	hasil = False
	if nilai > 50:
		hasil = True
	return hasil

# Fungsi hitung luas segitiga
def luas_segitiga(alas, tinggi):
	hasil = alas * tinggi / 2
	return hasil

lulus = cek_kelulusan(80)
print(lulus)

print luas_segitiga(4, 5)
print luas_segitiga(3, 9)
print luas_segitiga(7, 6)