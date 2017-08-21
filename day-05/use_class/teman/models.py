class Teman(object):
	jumlah = 0
	"""docstring for Teman"""
	def __init__(self, nama, sex):
		self.nama = nama
		self.sex = sex
		self.alamat = ""
		Teman.jumlah = Teman.jumlah + 1

		# return "Teman dengan nama %s telah hadir" %self.nama

	def __str__(self):
		return "Teman dengan nama %s telah hadir" %self.nama		


	def berbicara(self):
		return "Teman dengan nama %s sedang mengatakan bahwa saya hadir disini" %self.nama

		
daftar_teman = []
daftar_teman.append(Teman('Andy', 'Laki-Laki'))
daftar_teman.append(Teman('Joko', 'Laki-Laki'))
daftar_teman.append(Teman('Sinta', 'Perempuan'))
daftar_teman.append(Teman('Ilham', 'Laki-Laki'))
daftar_teman.append(Teman('Agung', 'Laki-Laki'))


if __name__ == "__main__":
	for teman in daftar_teman:
		print teman
		print teman.berbicara()

	print "\n"

	agung = Teman('Agung', 'Laki-Laki')
	agung.alamat = "Jln kabonena"
	print agung
	print "Alamat rumah agung berada di %s" % agung.alamat
	
	print "\n"

	print Teman.jumlah
		


	# print teman
	# print teman.berbicara()


