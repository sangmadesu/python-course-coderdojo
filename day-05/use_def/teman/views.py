from models import daftar_teman


def lihat_teman():
	print "Daftar Teman"
	print "------------"
	for teman in daftar_teman:
		print teman 
	print "\n"


if __name__ == "__main__":
	lihat_teman()