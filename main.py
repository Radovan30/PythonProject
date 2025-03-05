"""
Představ si, že vám uživatelé zadávají jména a příjmení a vy si je ukládáte do seznamu pro další použití např.
v evidenci studentů. Ne všichni jsou ale pořádní, a tak se v seznamu sem tam objeví i jméno s nesprávně zadanými velkými písmeny. Například:

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
Úkolem je:

Napsat funkci, která vybere jen ty správně zadané záznamy, které mají správně jméno i příjmení s velkým počátečním písmenem.
Napsat funkci, která vybere naopak jen ty nesprávně zadané záznamy.
(Nepovinný) – Napsat funkci, která vrátí seznam s opravenými záznamy.
Výsledné funkce by měly fungovat takto:

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']
spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy) # → ['Jiří Sládek']
opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy) # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']
Návod
Snadný způsob jak zjistit, zda je řetězec složen jen z malých písmen, je metoda islower(), která vrací True, pokud řetězec obsahuje jen malá písmena, jinak vrací False. Například 'abc'.islower() == True ale 'aBc'.islower() == False.
Snadný způsob jak převést první písmenko na velké je metoda capitalize(): např. 'abc'.capitalize() == 'Abc'
"""

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']