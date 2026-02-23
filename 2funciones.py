def max3 (a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
def main():
    numero1=int(input("Pon el primer numero:"))
    numero2=int(input("Pon el segundo numero:"))
    numero3=int(input("Pon el tercer numero:"))

    resultado = max3(numero1, numero2, numero3)
    print("El mayor es",resultado)

if __name__ == "__main__":
     main()