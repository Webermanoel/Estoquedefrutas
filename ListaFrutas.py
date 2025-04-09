def introduction():
    print("Bem-vindo ao controlador de estoque\n")

def frutas_estoque():
    fruits = []
    quantities = []

    num = int(input("Quantas frutas deseja adicionar à lista?\n"))

    for i in range(num):
        fruta = input(f"\nDigite o nome da fruta #{i+1}: ")
        fruits.append(fruta)

        quantia = int(input(f"Digite a quantidade de {fruta}: "))
        quantities.append(quantia)

    print("\n--- Estoque Atual ---")
    for i in range(len(fruits)):
        print(f"{fruits[i]}: {quantities[i]} unidades")


# Executando
introduction()
frutas_estoque()
