from queue import PriorityQueue

NIESKONCZONOSC=2**31-1

def znajdz_indeks_wierzcholka_o_numerze(graf, numer):
    indeks=0
    for wierz in graf:
        if wierz["numer"]==numer:
            return indeks
        indeks+=1
    return -1

def dijkstra(graf, indeks_start):
    odleglosci=[NIESKONCZONOSC]*len(graf)
    odleglosci[indeks_start]=0
    kolejka_wierzcholki=PriorityQueue()  # w kolejce znajdować się będą pary (obecna_odległość_od_startu, indeks_wierzchołka_w_grafie)

    for wierz in graf:
        indeks=znajdz_indeks_wierzcholka_o_numerze(graf, wierz["numer"])
        kolejka_wierzcholki.put(indeks)

    while not kolejka_wierzcholki.empty():
        indeks_obecnego=kolejka_wierzcholki.get()
        obecny_wierzcholek=graf[indeks_obecnego]

        for krawedz_do_sasiada in obecny_wierzcholek["sasiedzi"]:
            indeks_sasiada=znajdz_indeks_wierzcholka_o_numerze(graf, krawedz_do_sasiada[0])
            if odleglosci[indeks_obecnego]+krawedz_do_sasiada[1]<odleglosci[indeks_sasiada]:
                odleglosci[indeks_sasiada]=odleglosci[indeks_obecnego]+krawedz_do_sasiada[1]
    return odleglosci 




# numer wierzchołka niekoniecznie jest równy indeksowi w grafie
oryginalny_graf=[
    {"numer": 'A',"sasiedzi": [('B',5), ('D',3)]},
    {"numer": 'B',"sasiedzi": [('A',5), ('E',5), ('C',8)]},
    {"numer": 'C',"sasiedzi": [('B',8), ('E',4)]},
    {"numer": 'D',"sasiedzi": [('A',3), ('E',2)]},
    {"numer": 'E',"sasiedzi": [('B',5), ('C',4), ('D',2)]},
]


odleglosci=dijkstra(oryginalny_graf, 0)
print(odleglosci)