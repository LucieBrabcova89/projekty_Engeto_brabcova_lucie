import mysql.connector

def pripojeni():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= "1234",
        database="ukoly")

def tvorba_tabulky():
    conn=pripojeni()
    kurzor=conn.kurzor()

    kurzor.execute("""
CREATE TABLE ukoly.ukoly (
	id INT auto_increment NOT NULL PRIMARY KEY,
	nazev varchar(100) NOT NULL,
	popis_ukolu TEXT NULL,
	stav ENUM ('Nezahájeno', 'Hotovo', 'Probíhá') DEFAULT 'Nezahájeno' NOT NULL,
	datum_vytvoreni DATETIME DEFAULT now() NULL
)
    """)

ukoly = {}

def hlavni_menu ():
    print("Správce úkolů - Hlavní menu")
    print("1 - Přidat nový úkol")
    print("2 - Zobrazit všechny úkoly")
    print("3 - Aktualizovat úkol")
    print("4 - Odstranit úkol")
    print("5 - Konec programu")
    ciselne_moznosti = input("Vyberte možnost (1 - 4):")
    ciselne_moznosti = int(ciselne_moznosti)
    while True:
        if ciselne_moznosti == 5:
            exit()
        elif ciselne_moznosti == 4:
            odstranit_ukol()
            hlavni_menu()
        elif ciselne_moznosti == 3:
            aktualizovat_ukol()
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

def pridat_ukol(nazev_ukolu = None, popis_ukolu = None):
    if nazev_ukolu == None:
        nazev_ukolu = input("Název úkolu:")
    if popis_ukolu == None:
        popis_ukolu = input("Popis úkolu:")
    if nazev_ukolu == "" or popis_ukolu == "":
        if nazev_ukolu == "":
            print("Prosím vyplňte název úkolu.")
        if popis_ukolu == "":
            print("Prosím vyplňte popis úkolu.")
        pridat_ukol()
    else:
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
INSERT INTO ukoly.ukoly
(nazev, popis_ukolu)
VALUES('"""+ nazev_ukolu+"""', '"""+ popis_ukolu+"""')""")
        kurzor.close() 
        conn.commit()
        print("Úkol " + nazev_ukolu + " byl přidán.")

def zobrazit_ukoly():
    conn=pripojeni()
    kurzor=conn.cursor()
    print("Seznam úkolů:")
    kurzor.execute("SELECT id, nazev, popis_ukolu, stav FROM ukoly WHERE stav IN ('Nezahájeno', 'Probíhá')")

    myresult = kurzor.fetchall()

    for x in myresult:
        print(x)
    
def odstranit_ukol(co_smazat = None):
    zobrazit_ukoly()
    if co_smazat == None:
        co_smazat = input("Zadej ID úkolu, který chceš smazat: ")
    if co_smazat.isnumeric():
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
DELETE FROM ukoly.ukoly
WHERE id="""+ co_smazat)
        kurzor.close() 
        conn.commit()
        print("Úkol byl úspěšně smazán.")
    else:
        print("Tento úkol neexistuje!")

def aktualizovat_ukol(co_aktualizovat = None, akce = None):
    zobrazit_ukoly()
    if co_aktualizovat == None:
        co_aktualizovat = input("Zadej ID úkolu, který chceš aktualizovat: ")
    if akce == None:
        akce = input("Zadej 1 pro Probíhá nebo zadej 2 pro Hotovo: ")
    if akce==1:
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
UPDATE ukoly.ukoly SET stav='Probíhá' WHERE id="""+ co_aktualizovat)
        kurzor.close() 
        conn.commit()
        print("Úkol byl úspěšně aktualizován.")
    elif akce == 2:
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
UPDATE ukoly.ukoly SET stav='Hotovo' WHERE id="""+ co_aktualizovat)
        kurzor.close() 
        conn.commit()
        print("Úkol byle úspěšně aktualizován.")
    else:
        print("Chybná akce.")
        
#hlavni_menu()
    

