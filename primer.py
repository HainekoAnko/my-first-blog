e = 4
f = 6
h = 8
print(e+f+h)
if e <= f:
	print("ok")

def hi(name):
	if name == 'Ola':
		print('Hi Ola!')
	elif name == 'Sonja':
		print('Hi Sonja!')
	else:
		print('Hi anonymous!')

hi("name")

def he(name):
	print('Hola ' + name + '!')

girls = ['rei', 'moni', 'pii', 'sol']
for i in girls:
	he(i)
	print('next:')
for i in range(1, 6):
	print(i)