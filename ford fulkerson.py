import queue

przeplyw_max=0

# zawartość grafu {"numer": INDEX, "polaczenia": [ [CEL, PRZEPLYW, POJEMNOSC] ]}
graf=[]

def ile_jeszcze_moze_plynac(skad, dokad):
    polaczenia=graf[skad]["polaczenia"]
    for indeks, przeplyw, pojemnosc in polaczenia:
        if indeks==dokad:
            return pojemnosc-przeplyw
    return -1


# znajduje ścieżkę do każdego wierzchołka od startu
# tak że nie przechodzi przez krawędzie którymi już 
# nic nie może przepłynąć
def bfs(start):
    kolejka=queue.Queue()
    odwiedzony=[False]*len(graf)
    skad_przyszedlem=[-1]*len(graf) # -1 - nie da się, -2 - jestem początkiem
    skad_przyszedlem[start]=-2

    kolejka.put(start)
    odwiedzony[start]=True

    while not kolejka.empty():
        obecny=kolejka.get()
        polaczenia=graf[obecny]["polaczenia"]
        for indeks_sasiada, przeplyw, pojemnosc in polaczenia:
                if odwiedzony[indeks_sasiada]==False and (pojemnosc-przeplyw)>0:
                    kolejka.put(indeks_sasiada)
                    odwiedzony[indeks_sasiada]=True
                    skad_przyszedlem[indeks_sasiada]=obecny
    return skad_przyszedlem


def daj_sciezke(skad_przyszedlem, koniec):
    sciezka=[]
    obecny=koniec
    while obecny!=-2:
        sciezka.append(obecny)
        obecny=skad_przyszedlem[obecny]
    sciezka=list(reversed(sciezka))
    return sciezka


def znajdz_minimum(sciezka):
    minimum=2**31-1
    for i in range(len(sciezka)-1):
        obecny, nastepny=sciezka[i], sciezka[i+1]
        przeplyw=ile_jeszcze_moze_plynac(obecny, nastepny)
        minimum=min(minimum, przeplyw)
    return minimum


def aktualizuj_przeplywy_na_sciezce(sciezka, dodaj_przeplyw):
    global przeplyw_max
    przeplyw_max+=dodaj_przeplyw

    for i in range(len(sciezka)-1):
        obecny, nastepny=sciezka[i], sciezka[i+1]
        
        polaczenia_obecnego=graf[obecny]["polaczenia"]
        for i in range(len(polaczenia_obecnego)):
            if polaczenia_obecnego[i][0]==nastepny:
                polaczenia_obecnego[i][1]+=dodaj_przeplyw
                break
        

        polaczenia_nastepnego=graf[nastepny]["polaczenia"]
        for i in range(len(polaczenia_nastepnego)):
            if polaczenia_nastepnego[i][0]==obecny:
                polaczenia_nastepnego[i][1]-=dodaj_przeplyw
                break
        else:  # jeśli nie ma połączenia wstecz to dodaj takowe 
            polaczenia_nastepnego.append([obecny, -dodaj_przeplyw, 0])


def fordfulkerson(zrodlo, ujscie):
    skad_przyszedlem=bfs(zrodlo)
    
    #dopóki istnieje przejście
    while skad_przyszedlem[ujscie]!=-1:
        sciezka=daj_sciezke(skad_przyszedlem, ujscie)
        ile_przeplynie_przez_sciezke=znajdz_minimum(sciezka)
        aktualizuj_przeplywy_na_sciezce(sciezka,ile_przeplynie_przez_sciezke)
        skad_przyszedlem=bfs(zrodlo)  # znajdź nową ścieżkę




print("WIERZCHOLKI SA NUMEROWANE OD 0\n\n")
n=int(input("Podaj ilosc wierzcholkow: "))
for i in range(n):
    graf.append({"numer": i, "polaczenia": []})


m=int(input("Podaj ilosc krawedzi: "))
for i in range(m):
    skad, dokad, pojemnosc=input("Podaj wierzcholek poczatkowy, koncowy i pojemnosc tej krawedzi: ").split()
    skad, dokad, pojemnosc = int(skad), int(dokad), int(pojemnosc)
    graf[skad]["polaczenia"].append([dokad, 0, pojemnosc])

zrodlo = int(input("Podaj zrodlo: "))
ujscie = int(input("Podaj ujscie: "))

fordfulkerson(zrodlo, ujscie)

print(przeplyw_max)