class Buku(object):
	"""docstring for Buku"""
	def __init__(self, jenis):
		self.jenis = jenis


	def __str__(self):
		return 'Buku %s telah hadir di Toko Kutu Buku' %self.jenis


	def pinjam(self):
		return 'Buku %s telah dipinjam' %self.jenis
		


daftar_buku = []
daftar_buku.append(Buku('Matematika'))
daftar_buku.append(Buku('Bahasa Indonesia'))
daftar_buku.append(Buku('Bahasa Inggris'))
daftar_buku.append(Buku('Ilmu Pengetahuan Alam'))


if __name__ == "__main__":
	for buku in daftar_buku:
		print buku

	IPS = Buku('Ilmu Pengetahuan Sosial')
	print IPS.pinjam()
