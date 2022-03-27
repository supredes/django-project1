valor_saque = float(input("Valor do saque: "))
cedula = 200

qtd_cedulas = 0

while True:
    if valor_saque >= cedula:
        valor_saque -= cedula
        qtd_cedulas += 1
    else:
        if qtd_cedulas > 0:
            if qtd_cedulas == 1:
                print(f'{qtd_cedulas} cédula de {cedula}')
            else:
                print(f'{qtd_cedulas} cédulas de {cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        qtd_cedulas = 0
        if valor_saque == 0:
            break