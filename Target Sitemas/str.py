def verifica_letra_a(string):
    string = string.lower()
    conta_a = string.count('a')

    if conta_a > 0:
        return f"A letra 'a' aparece {conta_a} vezes na string"
    else:
        return "A letra 'a' nao aparece na string"
    
texto = input("Informe a frase: ")
print(verifica_letra_a(texto))



