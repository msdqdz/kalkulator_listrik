#volt current resistance power calculator
#3/4/21 - 7/4/21 made with love by MSD 

from vir import Vir
from powers import Powers

print('\n-------------Kalkulator listrik-------------\n')

y = ['Tegangan V=I·R',
	'Arus I=V/R',
	'Tahanan R=V/I',
	'Daya Aktif (Watt) P=V·I·cosφ',
	'Daya Reaktif (VAR) Q=V·I·sinφ',
	'Daya Semu (VA) S=V·I',
	'Arus I=S/V']

z = 1
while z <= len(y):
	for j in y:
	 	print(z,j)
	 	z += 1 

hitung = Vir(0,0)
hitungPow = Powers(0,0,0)

x = input("\nMau hitung apa ?\n")

if int(x) == 1:
	hitung.volt()
	
elif int(x) == 2:
	hitung.current()

elif int(x) == 3:
	hitung.resistance()

elif int(x) == 4:	
	hitungPow.watt()

elif int(x) == 5:
	hitungPow.var()

elif int(x) == 6:	
	hitung.powerVA()

elif int(x) == 7:
	hitung.powerCurrent()

else:
	print('Pilihan salah, silakan coba lagi.')