def nactiCislo():
    return int(input("Zadejte cislo"))

prvniCislo= nactiCislo()
druheCislo= nactiCislo()
operace = int(input("Zadejte operaci: 1,2,3,4"))
if(operace ==1):
    print (prvniCislo + druheCislo)
elif(operace ==2):
    print(prvniCislo - druheCislo)
elif(operace ==3):
    print(prvniCislo / druheCislo)
else:
    print(prvniCislo * druheCislo)




