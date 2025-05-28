from src.Projekt_2_Lucie_Brabcova import pridat_ukol, aktualizovat_ukol, odstranit_ukol
import mysql.connector
import uuid



def pripojeni():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= "1234",
        database="ukoly")

def test_pridat_pozitivni():
    tNAZEV = "Test úkol " + str(uuid.uuid4())
    tPOPIS = "Test popis " + str(uuid.uuid4())
    pridat_ukol(tNAZEV, tPOPIS)
    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""SELECT id, nazev, popis_ukolu, stav FROM ukoly WHERE nazev = '""" + tNAZEV + """' AND popis_ukolu = '""" + tPOPIS + """'""")
    myresult = kurzor.fetchall()
    conn.close()
    
    result = len(myresult)

    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""DELETE FROM ukoly.ukoly WHERE nazev = '"""+ tNAZEV+"""' AND popis_ukolu = '"""+ tPOPIS+"""'""")
    kurzor.close() 
    conn.commit()
    conn.close()
    
    assert result >= 1

def test_pridat_negativni():
    result = pridat_ukol("", "")
    assert result == False

def test_aktualizovat_pozitivni():
    tNAZEV = "Test úkol " + str(uuid.uuid4())
    tPOPIS = "Test popis " + str(uuid.uuid4())
    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""INSERT INTO ukoly.ukoly (nazev, popis_ukolu) VALUES('"""+ tNAZEV+"""', '"""+ tPOPIS+"""')""")
    tID = str(kurzor.lastrowid)
    kurzor.close() 
    conn.commit()
    conn.close()
    result = aktualizovat_ukol(tID, "2")

    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""SELECT id FROM ukoly WHERE id = '""" + tID + """' AND stav = 'Hotovo' """)
    myresult = kurzor.fetchall()
    conn.close()
    result = len(myresult)

    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""DELETE FROM ukoly.ukoly WHERE id = '"""+ tID+"""'""")
    kurzor.close() 
    conn.commit()
    conn.close()

    assert result >= 1

def test_aktualizovat_negativni():
    result = aktualizovat_ukol("3", "3")
    assert result =="Chybná akce."

def test_odstranit_pozitivni():
    tNAZEV = "Test úkol " + str(uuid.uuid4())
    tPOPIS = "Test popis " + str(uuid.uuid4())
    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""INSERT INTO ukoly.ukoly (nazev, popis_ukolu) VALUES('"""+ tNAZEV+"""', '"""+ tPOPIS+"""')""")
    tID = str(kurzor.lastrowid)
    kurzor.close() 
    conn.commit()
    conn.close()
    result = odstranit_ukol(tID)

    conn=pripojeni()
    kurzor=conn.cursor()
    kurzor.execute("""SELECT id FROM ukoly WHERE id = '""" + tID + """'""")
    myresult = kurzor.fetchall()
    conn.close()
    
    result = len(myresult)
    assert result == 0

def test_odstranit_negativní():
    result = odstranit_ukol("pes")
    assert result == "Neplatná volba."
    
