

def main():
    num_r=int(input(''))
    num_c=int(input(''))

    res=num_r*num_c

    lista=[]
    i=1
    
    while i<=res:
        i=i+1
        a=int(input(''))
        if a<10:
           lista.append(a) 
    print(lista)



if __name__=='__main__':
    main()
