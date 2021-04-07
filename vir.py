
class Vir:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def volt(self):
		print('Anda menghitung Tegangan')
		self.a = float(input('Masukkan arus : '))
		self.b = float(input('Masukkan tahanan : '))
		print(self.a,'A','x',self.b,'Ω','=',self.a*self.b,"V")

	def current(self):
		print('Anda menghitung Arus')
		self.a = float(input('Masukkan tegangan : '))
		self.b = float(input('Masukkan tahanan : '))	
		print(self.a,'V','/',self.b,'Ω','=',self.a/self.b,"A")

	def resistance(self):
		print('Anda menghitung Tahanan')
		self.a = float(input('Masukkan tegangan : '))
		self.b = float(input('Masukkan arus : '))
		print(self.a,'V','/',self.b,'A','=',self.a/self.b,"Ω")

	def powerVA(self):
		print('Anda menghitung Daya Semu (VA)')
		self.a = float(input('Masukkan tegangan : '))
		self.b = float(input('Masukkan arus : '))
		print("S = V·I")
		print(self.a,'V','x',self.b,'A','=',self.a*self.b,"VA")

	def powerCurrent(self):
		print('Anda menghitung Arus')
		self.a = float(input('Masukkan daya (VA) : '))
		self.b = float(input('Masukkan tegangan : '))
		print("I = S/V")
		print(self.a,'VA','/',self.b,'V','=',self.a/self.b,"A")