import random

Status		= ['Jomblo','Menikah','Pacaran']
Greeting	= ['Selamat Pagi','Selamat Siang','Selamat Malam']
Gender		= ['Laki-laki','Perempuan']
Job			= ['Sekolah','Guru anak tk','Pengacara','Tidak Ada']
Hobby		= ['Turu','Main game','Ngoprek']
Quotes		= ['Jangan semangat!','Teruslah gagal!','Teruslah hidup!','Semangat!']

#output
def output():
	print('\n====== ' +	random.choice(Greeting) )

	print('\n====== hai, statusku saat ini ' +	random.choice(Status) )

	print('\n====== jenis kelaminku adalah ' +	random.choice(Gender) )

	print('\n====== dan aku punya hobby ' +	random.choice(Hobby) )
	
	print('\n====== untuk saat ini, pekerjaanku ' +	random.choice(Job) )

	print('\n====== Apapun yang sudah kamu lakukan hari ini, ' + random.choice(Quotes) )
	
output()
