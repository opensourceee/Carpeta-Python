#laboratiorio de metodos numericos
if __name__ == '__main__':
	a = [str() for ind0 in range(50)]
	print("Ingrese cantidad de datos: ")
	n = int(input())
	for i in range(1,n+1):
		print("Ingrese el dato ",i,":")
		a[i-1] = int(input())
	min = a[0]
	for i in range(2,n+1):
		if a[i-1]<min:
			min = a[i-1]
	print("El minimo de los ",n," numeros es: ",min)
