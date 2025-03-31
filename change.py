def change():
    expense = 23.75
    money = 100
    
    print(f"Ingresar gasto:")
    print(f"{expense}")
    print(f"Dinero recibido")
    print(f"{money}")
    print(f"")
    print(f"Vuelto")
    print(f"")
    print(f"Pesos:")
    print(f"{str(money - expense).split(".")[0]}")
    print(f"Centavos:")
    print(f"{str(money - expense).split(".")[1]}")
