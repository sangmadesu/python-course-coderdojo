from models import daftar_buku


def lihat_buku():
	print "Daftar Buku"
	print "------------"
	for buku in daftar_buku:
		print buku
	print "\n"

if __name__ == "__main__":
	lihat_buku()
