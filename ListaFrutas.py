def introdction():
    print("Bem-Vindo ao controlador de estoque\n")

def frutasestoque():
    fruits = ["Banana, Maça, Laranja, Manga, Melancia, Abacaxi"]
    i = 0
    while i < len(fruits):
        i = i + 1
    quantidade = ["100, 75, 150, 60, 20, 30"]
    i = 0
    while i < len(quantidade):
        i = i + 1

        print(f"Frutas em estoque: {fruits}")
        print(f"Quantidade disponível: {quantidade}")

introdction()
frutasestoque()
