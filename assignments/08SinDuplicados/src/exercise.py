def main():
    #escribe tu código abajo de esta línea

    num = int(input())
    lista = []
    i = 0

    if num>0 : 
        while i<num:
            valor = input()
            lista.append(valor)
            i = i+1
        print(lista)
        sin_repetir = []
        for i in lista : 
            if i not in sin_repetir:
                sin_repetir.append(i)
        print(sin_repetir)
    else: 
        print('Error')

    pass
if __name__=='__main__':
    main()
