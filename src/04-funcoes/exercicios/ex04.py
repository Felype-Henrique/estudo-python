def soma_numeros(*args):
    return sum(args)


print(f"Soma de 3 números: {soma_numeros(10, 20, 30)}")
print(f"Soma de 5 números: {soma_numeros(5, 15, 25, 35, 45)}")
print(f"Soma de 2 números: {soma_numeros(100, 200)}")
