val1 = input("Digite o primeiro número:")
val2 = input("Digite o segundo número:")
val1 = int(val1)
val2 = int(val2)
Ope = input("Selecione a operação desejada (x, /, +, -)")
if Ope == "x":
 print("Resultado:",val1 * val2)
elif Ope == "/":
  print("resultado:",val1 / val2)
elif Ope == "+":
  print("resultado:",val1 + val2)
elif Ope == "-":
  print("resultado:",val1 - val2)
