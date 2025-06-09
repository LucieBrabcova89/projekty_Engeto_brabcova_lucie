ukoly = {}

def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1 - Přidat nový úkol")
    print("2 - Zobrazit všechny úkoly")
    print("3 - Odstranit úkol")
    print("4 - Konec programu")
    ciselne_moznosti = input("Vyberte možnost (1 - 4):")
    ciselne_moznosti = int(ciselne_moznosti)
    while True:
        if ciselne_moznosti == 4:
            exit()
        elif ciselne_moznosti == 3:
            odstranit_ukol()
            hlavni_menu()
        elif ciselne_moznosti == 2:
            zobrazit_ukoly()
            hlavni_menu()
        elif ciselne_moznosti == 1:
            pridat_ukol()
            hlavni_menu()
        else:
            print("Neplatná hodnota! Opakujte volbu.")
            ciselne_moznosti=input("Vyberte možnost (1 - 4):")
            ciselne_moznosti = int(ciselne_moznosti)

def pridat_ukol():
    nazev_ukolu = input("Název úkolu:")
    popis_ukolu = input("Popis úkolu:")
    if nazev_ukolu == "" or popis_ukolu == "":
        if nazev_ukolu == "":
            print("Prosím vyplňte název úkolu.")
        if popis_ukolu == "":
            print("Prosím vyplňte popis úkolu.")
        pridat_ukol()
    else:
        ukoly[nazev_ukolu] = popis_ukolu
        print("Úkol " + nazev_ukolu + " byl přidán.")

def zobrazit_ukoly():
    #print(ukoly)
    print("Seznam úkolů:")
    for klic in ukoly.keys():
        print(klic + " - " + ukoly[klic] + "\n") 
    
def odstranit_ukol():
    zobrazit_ukoly()
    co_smazat = input("Jaký úkol chceš smazat?")
    if ukoly.get(co_smazat, 0) != 0:
        del ukoly[co_smazat]
        print("Úkol byle úspěšně smazán.")
    else:
        print("Tento úkol neexistuje!")


hlavni_menu()
    

