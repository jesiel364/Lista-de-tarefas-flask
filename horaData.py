import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

mes = time.strftime('%m')
b = '0'
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
format = int(mes.replace(b, "")) - 1


t = time.strftime(f'%d de {meses[format]} %H:%M')

simples = time.strftime(f'%d/%m/%y %H:%M')

hoje = time.strftime('%d')

class Tempo:
	def __init__(self, Date):
		self.Date = Date
		self.dia = '27' #Date[:2]
		self.mes = Date[3:5]
		self.ano = Date[6:8]
		self.hora = Date[9:14]
		
	def legend(self):
	        hojeDia = time.strftime("%d")
	        hojeMes = time.strftime("%m")
	        hojeAno = time.strftime("%y")
	        if float(hojeMes) - float(self.mes == 0):
	        	if int(hojeDia) - int(self.dia) == 1:
	        		return 'Ontem'
	        	elif int(hojeDia) - int(self.dia) == 0:
	        		return 'Hoje'



data = Tempo(simples)


	
