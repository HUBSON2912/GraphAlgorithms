NIESKONCZONOSC=2**31-1

class Wierzcholek:
    def __init__(self, numer, sasiedzi=[], odleglosc=NIESKONCZONOSC):
        self.numer=numer
        self.sasiedzi=sasiedzi
        self.odleglosc=odleglosc
    
    def __lt__(self, inny):
        return self.odleglosc < inny.odleglosc
    
def znajdz_indeks_wierz_o_numerze(graf, numer):
    index=0
    while index<len(graf):
        if graf[index].numer==numer:
            return index
        index+=1
    return -1

def dijkstra(graf, indeks_start):
    wierzcholki_do_przejscia=[]
    graf[indeks_start].odleglosc=0

    for wierz in graf:
        wierzcholki_do_przejscia.append(wierz)
    
    while  len(wierzcholki_do_przejscia)!=0:
        wierzcholki_do_przejscia.sort()
        
        obecny_wierz=wierzcholki_do_przejscia[0]
        wierzcholki_do_przejscia.pop(0)
        indeks_obecnego=znajdz_indeks_wierz_o_numerze(graf, obecny_wierz.numer)

        for krawedz_do_sasiada in obecny_wierz.sasiedzi:
            indeks_sasiada=znajdz_indeks_wierz_o_numerze(graf, krawedz_do_sasiada[0])
            waga=krawedz_do_sasiada[1]
            if graf[indeks_obecnego].odleglosc+waga < graf[indeks_sasiada].odleglosc:
                graf[indeks_sasiada].odleglosc = graf[indeks_obecnego].odleglosc+waga


oryginalny_graf=[
    Wierzcholek(1, [(9,8), (4,4)]),
    Wierzcholek(2, [(10,1), (7,4), (4,5)]),
    Wierzcholek(3, [(8,4), (7,5), (4,5), (5,8)]),
    Wierzcholek(4, [(1,4),(9,1),(2,5),(7,6),(3,5),(5,2)]),
    Wierzcholek(5, [(4,2), (3,8)]),
    Wierzcholek(6, [(8,1), (7,3), (10,4)]),
    Wierzcholek(7, [(6,3), (2,4), (4,6),(3,5)]),
    Wierzcholek(8, [(6,1), (10,5), (3,4)]),
    Wierzcholek(9, [(1,8), (4,1), (10,7)]),
    Wierzcholek(10, [(6,4), (8,5), (2,1), (9,7)])
]


dijkstra(oryginalny_graf, 0)

for wierz in oryginalny_graf:
    print(wierz.numer, wierz.odleglosc)