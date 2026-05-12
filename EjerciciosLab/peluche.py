precio = int(input("Hola Lu, ingresa el precio del peluche: $ "))
b100 = precio // 100
resto = precio % 100

b50 = resto // 50
resto = resto % 50

b20 = resto // 20
resto = resto % 20

b10 = resto // 10
resto = resto % 10

b5 = resto // 5
resto = resto % 5

b1 = resto // 1

print(b100, "billetes de $100")
print(b50, "billetes de $50")
print(b20, "billetes de $20")
print(b10, "billetes de $10")
print(b5, "billetes de $5")
print(b1, "billetes de $1")

 