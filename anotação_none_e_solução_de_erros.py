resultado = None
if resultado is None
  print("ainda não existe resultado")

valor = None
if valor is None
  print("sem valor")


while True:
    try:
        numero = int(input("digite um numero: "))
        print(10 / numero)
        break
    except ValueError:
        print("numero invalido")
    except ZeroDivisionError:
        print("não e possivel dividir por 0")



texto = "python"
print(texto.upper())
print(texto.lower())
print(len(texto))
print(texto[0])
print(texto[1:4])
print("py" in texto)
