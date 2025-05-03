from src.Projekt_2_Lucie_Brabcova import pridat_ukol, aktualizovat_ukol, odstranit_ukol

def test_pridat_pozitivni():
    result = pridat_ukol("Název", "Popis")
    assert result == "Úkol Název byl přidán."


def test_pridat_negativni():
    result = pridat_ukol("", "")
    assert result == False

def test_aktualizovat_pozitivni():
    result = aktualizovat_ukol("5", "2")
    assert result == "Úkol byl úspěšně aktualizován."

def test_aktualizovat_negativni():
    result = aktualizovat_ukol("3", "3")
    assert result =="Chybná akce."

def test_odstranit_pozitivni():
    result = odstranit_ukol("3")
    assert result == "Úkol byl úspěšně smazán."

def test_odstranit_negativní():
    result = odstranit_ukol("pes")
    assert result == "Neplatná volba."
    
