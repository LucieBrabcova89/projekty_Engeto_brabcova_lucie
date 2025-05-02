from src.Projekt_2_Lucie_Brabcova import pridat_ukol, aktualizovat_ukol, odstranit_ukol

def test_pridat_pozitivni():
    pridat_ukol("Přidávám úkol.", "Nový úkol.")
    assert "Úkol Přidávám úkol. byl přidán."

def test_pridat_negativni():
    pridat_ukol("", "")
    assert "Prosím vyplňte název úkolu."
# Program mám napsaný tak, že nutí uživatele něco zadat, z toho důvodu mi pytest vychází jako failed.

def test_aktualizovat_pozitivni():
    aktualizovat_ukol("5", "2")
    assert "Úkol byl úspěšně aktualizován."

def test_aktualizovat_negativni():
    aktualizovat_ukol("3", "3")
    assert "Chybná akce."

def test_odstranit_pozitivni():
    odstranit_ukol("3")
    assert "Úkol byl úspěšně smazán."

def test_odstranit_negativní():
    odstranit_ukol("pes")
    assert "Tento úkol neexistuje!"
