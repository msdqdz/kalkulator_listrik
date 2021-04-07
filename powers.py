from vir import Vir
import math

class Powers(Vir):
	def __init__(self,a,b,phi):
		super().__init__(a,b)
		self.phi = phi

	def watt(self):
		print('Anda menghitung Daya Aktif (Watt)')
		self.a = float(input('Masukkan tegangan : '))
		self.b = float(input('Masukkan arus : '))
		self.phi = float(input('Masukkan faktor daya : '))
		print("P = V·I · cosφ")
		print('(',self.a,'V','x',self.b,'A)','x','cos(',self.phi,')','=',(self.a*self.b)*math.cos(math.radians(self.phi)),"W")

	def var(self):
		print('Anda menghitung Daya Reaktif (VAR)')
		self.a = float(input('Masukkan tegangan : '))
		self.b = float(input('Masukkan arus : '))
		self.phi = float(input('Masukkan faktor daya : '))	
		print("Q = V·I · sinφ")
		print('(',self.a,'V','x',self.b,'A)','x','sin(',self.phi,')','=',(self.a*self.b)*math.sin(math.radians(self.phi)),"VAR")