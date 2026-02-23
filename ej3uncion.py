def cuenta_letras(frase):
    contador =0
    for i in frase:
        contador +=1
    return contador

def main():
    frasecita = input("Por una frase: ")
    resultado = cuenta_letras(frasecita)
    print("El resultado es:",resultado)

if __name__ == "__main__":
    main()