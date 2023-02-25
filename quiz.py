n = int(input("Insertar número de tres digitos: "))

m = n % 10
p = n // 10
c = p % 10
f = p // 10

D = m * 100
C = c * 10

M = D + C + f

print("El inverso del número es: " + str(M))
