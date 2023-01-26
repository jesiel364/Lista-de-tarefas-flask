import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

mes = time.strftime('%m')
b = '0'
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
format = int(mes.replace(b, "")) - 1


t = time.strftime(f'%d de {meses[format]} %H:%M')