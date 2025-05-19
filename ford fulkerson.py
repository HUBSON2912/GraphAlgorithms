import queue

przeplyw_max=0

# połączenie --> [docelowy, przepływ, pojemność max]
# graf=[
#     {"numer": 0, "polaczenia": [[1,0,10], [2,0,11]]},
#     {"numer": 1, "polaczenia": [[2,0,15], [3,0,7]]},
#     {"numer": 2, "polaczenia": [[3,0,8], [4,0,3]]},
#     {"numer": 3, "polaczenia": [[5,0,9]]},
#     {"numer": 4, "polaczenia": [[5,0,14]]},
#     {"numer": 5, "polaczenia": []},
# ]

graf=[
    {"numer": 0, "polaczenia": [[1,0,4]]},
    {"numer": 1, "polaczenia": [[2,0,1], [3,0,2], [5,0,3]]},
    {"numer": 2, "polaczenia": [[3,0,2], [4,0,6]]},
    {"numer": 3, "polaczenia": [[0,0,1], [6,0,1]]},
    {"numer": 4, "polaczenia": [[6,0,9]]},
    {"numer": 5, "polaczenia": [[2,0,3], [0,0,3]]},
    {"numer": 6, "polaczenia": []}
]

def ile_jeszcze_moze_plynac(skad, dokad):
    polaczenia=graf[skad]["polaczenia"]
    for indeks, przeplyw, pojemnosc in polaczenia:
        # indeks, przeplyw, pojemnosc=
        if indeks==dokad:
            return pojemnosc-przeplyw
    return -1

def bfs(start:int, koniec:int):
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

def daj_przejscie(skad_przyszedlem, koniec):
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
        else:
            polaczenia_nastepnego.append([obecny, -dodaj_przeplyw, 0])

def fordfulkerson(zrodlo: int, ujscie: int):
    skad_przyszedlem=bfs(zrodlo, ujscie)
    
    #dopóki istnieje przejście
    while skad_przyszedlem[ujscie]!=-1:
        sciezka=daj_przejscie(skad_przyszedlem, ujscie)
        ile_przeplynie_przez_sciezke=znajdz_minimum(sciezka)
        aktualizuj_przeplywy_na_sciezce(sciezka,ile_przeplynie_przez_sciezke)
        skad_przyszedlem=bfs(zrodlo, ujscie)

zrodlo=5
ujscie=6

fordfulkerson(zrodlo, ujscie)
# for indeks, przeplyw, pojemnosc in graf[ujscie]["polaczenia"]:
#     przeplyw_max+=(przeplyw if przeplyw>0 else 0)

print(przeplyw_max)