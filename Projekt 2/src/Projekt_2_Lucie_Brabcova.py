import mysql.connector

def pripojeni():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= "1234",
        database="ukoly")

def tvorba_tabulky():
    conn=pripojeni()
    kurzor=conn.cursor()

    kurzor.execute("""
CREATE TABLE IF NOT EXISTS ukoly.ukoly (
	id INT auto_increment NOT NULL PRIMARY KEY,
	nazev varchar(100) NOT NULL,
	popis_ukolu TEXT NULL,
	stav ENUM ('Nezahájeno', 'Hotovo', 'Probíhá') DEFAULT 'Nezahájeno' NOT NULL,
	datum_vytvoreni DATETIME DEFAULT now() NULL
)
    """)
    conn.close()
    return True

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Aktualizovat úkol")
        print("4 - Odstranit úkol")
        print("5 - Konec programu")
        ciselne_moznosti = input("Vyberte možnost (1 - 5):")
        while (not ciselne_moznosti.isnumeric()):
            print("Zadej číslo!")
            ciselne_moznosti = input("Vyberte možnost (1 - 5x):")
        ciselne_moznosti = int(ciselne_moznosti)
        if ciselne_moznosti == 5:
            exit()
        elif ciselne_moznosti == 4:
            odstranit_ukol_input()
        elif ciselne_moznosti == 3:
            aktualizovat_ukol_input()
        elif ciselne_moznosti == 2:
            zobrazit_ukoly()
        elif ciselne_moznosti == 1:
            pridat_ukol_input()
        else:
            print("Neplatná hodnota! Opakujte volbu.")
        return True

def pridat_ukol_input():
    nazev_ukolu = input("Název úkolu:")
    popis_ukolu = input("Popis úkolu:")
    return pridat_ukol(nazev_ukolu, popis_ukolu)

def pridat_ukol(nazev_ukolu = None, popis_ukolu = None):
    
    if nazev_ukolu == "" or popis_ukolu == "":
        if nazev_ukolu == "":
            print("Prosím vyplňte název úkolu.")
        if popis_ukolu == "":
            print("Prosím vyplňte popis úkolu.")
        return False
    else:
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
INSERT INTO ukoly.ukoly
(nazev, popis_ukolu)
VALUES('"""+ nazev_ukolu+"""', '"""+ popis_ukolu+"""')""")
        kurzor.close() 
        conn.commit()
        conn.close()
        return "Úkol " + nazev_ukolu + " byl přidán."
    

def zobrazit_ukoly():
    conn=pripojeni()
    kurzor=conn.cursor()
    print("Seznam úkolů:")
    kurzor.execute("SELECT id, nazev, popis_ukolu, stav FROM ukoly WHERE stav IN ('Nezahájeno', 'Probíhá')")
    myresult = kurzor.fetchall()
    for x in myresult:
        print(x)
    conn.close()
    return myresult
def odstranit_ukol_input():
    co_smazat = input("Zadej ID úkolu, který chceš smazat: ")
    odstranit_ukol(co_smazat)

def odstranit_ukol(co_smazat = None):
    zobrazit_ukoly()
    if co_smazat.isnumeric():
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
DELETE FROM ukoly.ukoly
WHERE id="""+ co_smazat)
        kurzor.close() 
        conn.commit()
        conn.close()
        return "Úkol byl úspěšně smazán."
    else:
        return "Neplatná volba."
    

def aktualizovat_ukol_input():
    co_aktualizovat = input("Zadej ID úkolu, který chceš aktualizovat: ")
    akce = input("Zadej 1 pro Probíhá nebo zadej 2 pro Hotovo: ")
    return aktualizovat_ukol(co_aktualizovat, akce)

def aktualizovat_ukol(co_aktualizovat = None, akce = None):
    zobrazit_ukoly()
    if akce=="1":
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
UPDATE ukoly.ukoly SET stav='Probíhá' WHERE id="""+ co_aktualizovat)
        kurzor.close() 
        conn.commit()
        conn.close()
        return("Úkol byl úspěšně aktualizován.")
    elif akce == "2":
        conn=pripojeni()
        kurzor=conn.cursor()
        kurzor.execute("""
UPDATE ukoly.ukoly SET stav='Hotovo' WHERE id="""+ co_aktualizovat)
        kurzor.close() 
        conn.commit()
        conn.close()
        return "Úkol byl úspěšně aktualizován."
    else:
        return "Chybná akce."

if __name__ == "__main__":
    tvorba_tabulky()
# Oddělená TEST DB je označeno jako volitelné
    while True:    
        hlavni_menu()
    

