"""
Python.:
 1. feladat: Hozzunk létre egy arra alkalmas adatszerkezetet, ami képes arra hogy eltároljon tanulok neveihez érdemjegyet, hozz létre egy olyan adatszerkezetet amelyben 10 tanulo
egy aktualis erdemjegyet tarolja(1-5ig) Függvénnyel!! A függvény gyüjtse ki azoknak a neveit, akik legalább közepes érdemjegyet kaptak! A neveket egymás mellé pontos vesszővel elválasztva!

2. feladat: Felhasználó által töltsünk fel egy listát, tároljunk el benne 10db szöveges értéket. Az eljárásunk ezt paraméterként fogja megkapni ezt a listát. 
megszámoljuk hány karakter van összesen, ebben a listában, és bekérünk a felhasználótól egy stringet, megvizsgáljuk hogy annak a karakter hossza megegyezik e vagy sem, ezzel az értékkel


3.feladat: Függvénnyel: A függvény magjában hozzunk létre egy olyan adatszerkezet, amely nem engedélyezi a duplikációt. Tárolj el ebben 5 egész számot, majd átlagoljuk őket, és az átlag
úgy adja vissza a kiirásnál a valós értéket, hogy egy tizedes pontossággal. 

4.feladat: Függvénnyel: A függvény megkap paraméterként egy egész számot, majd ezt az értéket felhasználva, egy olyan adatszerkezetben tároljuk amely engedélyezi a  duplikációt
a listában szereplő elemek közül hanyadik fizikai helyen áll az az érték amely az utolsó páros. 


5. feladat: Eljárással: Az eljárás megkap 1db stringet, (egy mondatot). egy validálást kellene késziteni, hogy helyes e a mondat. (Nagy kezdőbetüvel kezdődjön, és a végén legyen irásjel. )
szövegesen kell kiértékelni hogy ez egy magyar helyes mondatot reprezental vagy nem. 
Ha valid: akkor pedig számold meg hány db "a" karakter szerepel benne, irjuk ki, és hogy ohajto, felkialto, kerdo, kijelento mondat e . 

"""


# 1. feladat 

def erdemjegy():
    tanulok = {
        "József": 4,
        "László": 2,
        "Sándor": 3,
        "Béla": 4,
        "István": 2,
        "Gáspár": 5,
        "Gábor": 4

    }

    def kozepes_tanulok(tanulok):
        kozepesek = [nev for nev, jegy in tanulok.items() if jegy >= 3] # ha a tanulók jegyei nagyobb-egyenlő mint 3. 
        return ", ".join(kozepesek) #egy vesszőt joinoltatok a nevek közé mint string. 

    print("1. feladat: A következő tanulóknak legalább hármas az érdemjegy. ", kozepes_tanulok(tanulok) )

erdemjegy()

#2. feladat 
print("2. feladat: ")
def karakterek_szama(szovegek):
    ossz_karakter = sum(len(szoveg) for szoveg in szovegek) #megszámlálja a len segitségével az összes karaktereket 
    szoveg2 = input("Kérlek adj meg egy szót az összehasonlításhoz: ")
    karakter2 = len(szoveg2)

    if ossz_karakter == karakter2:
        print("A karakterek száma megegyezik.")
    else:
        print("A karakterek száma nem egyezik meg.")

szovegek = []
for i in range(10):
    szoveg = input(f"Kérlek adj meg egy szót({i+1}/10): ") 
    szovegek.append(szoveg)

karakterek_szama(szovegek)


#3. feladat

print("3. feladat: ")

def atlag():
    szamok = set()
    for i in range(5):
        szam = int(input(f"Kérlek adj meg egy egész számot({i+1}/5):  "))
        szamok.add(szam)
        osszeg = sum(szamok)
        hossz = len(szamok)

    atlag = osszeg / hossz

    print(f"Az átlag: {atlag:.1f}") # az átlagot tizedespontosággal iratjuk ki! 

atlag()


#4. feladat

print("4. feladat: ")

def utolsoparos(szam):
    lista = list(range(1, szam + 1))
    
    for index in range(len(lista) - 1, -1, -1):
        if lista[index] % 2 == 0:
            return index + 1
    

eredmeny = utolsoparos(14)
print("Az utolsó páros szám fizikai helye:", eredmeny)

#5. feladat: 
print("5. feladat: ")
def mondat_validalas(mondat):

    if mondat[0].isupper() and mondat[-1] in ['.', '!', '?']: #Ha a mondat kezdő beztűje nagybetű, és a végén irásbeli jel is található a mondat helyes
        print("A mondat helyes.")
        a_karakterek = mondat.count('a') #Megszámláljuk az "a" karaktereket

        print(f"A mondatban {a_karakterek} db 'a' karakter szerepel.")

        if mondat[-1] == '.':
            print("A mondat kijelentő mondat.") #ha a mondat "."-al végződik akkor a mondat kijelentő mondat

        elif mondat[-1] == '!':
            print("A mondat felkiáltó/óhajtó mondat.")

        elif mondat[-1] == '?':
            print("A mondat kérdő mondat.")
    else:
        print("A mondat nem helyes! .") # Ha ezek közül egyik sem vagy csak az egyik igaz rá, akkor a mondat helytelen! 

mondat = input("Kérlek adj meg egy mondatot! ")
mondat_validalas(mondat)
