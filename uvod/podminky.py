cisloStr = input ("Zadejte cislo")
cislo = int(cisloStr)
if (cislo > 0):
    print(cislo, " je kladne")
    if(cislo ==6):
        print("zadal jsem moje oblibene cislo")
elif(cislo < 0):
    print(cislo, " je zaporne")
else:
    print(cislo, "je nula")
