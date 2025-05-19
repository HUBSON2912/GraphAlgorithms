# ALGORYTM KRUSKALA


# krawędz -> (waga, skąd, dokąd)
def wybierz_krawedzie_z_grafu(graf):
    wszystkie_krawedzie=[]
    for wierz in graf:  
        for krawedz in wierz["sasiedzi"]:  
            skad=min(krawedz[0], wierz["numer"])  
            dokad=max(krawedz[0], wierz["numer"])
            waga=krawedz[1]
            wszystkie_krawedzie.append((waga, skad, dokad))   
    wszystkie_krawedzie=list(set(wszystkie_krawedzie))  #usuń duplikaty krawędzi
    wszystkie_krawedzie.sort()  
    return wszystkie_krawedzie

# wybiera wszystkie wierzcholki ale zostawia puste połączenia
def wez_wierzcholki(graf):
    wierzcholki=[]
    for wierz in graf:   
        wierzcholki.append( {"numer":wierz["numer"], "sasiedzi":[]} )   
    return wierzcholki

def daj_las_z_pojedynczymi_drzewami(graf):
    wierzcholki=wez_wierzcholki(graf)  
    las=[]
    for wierz in wierzcholki:  
        las.append([wierz]) # dodaj graf z jednym wierzcholkiem
    return las

# zwraca pozycję w lesie lub -1 jeśli nie ma takiego wierzchołka
def w_ktorym_drzewie_jest_wierzcholek_o_numerze(las, numer):
    ktoro_drzewo=0
    for drzewo in las:  
        for wierz in drzewo:   
            if wierz["numer"]==numer:   
                return ktoro_drzewo
        ktoro_drzewo+=1   
    return -1   


def polacz_dwa_wierzcholki_w_grafie(graf, numerWierz1, numerWierz2, waga):
    for wierz in graf:   
        if wierz["numer"]==numerWierz1:   
            wierz["sasiedzi"].append((numerWierz2,waga))   
        elif wierz["numer"]==numerWierz2:   
            wierz["sasiedzi"].append((numerWierz1,waga))   

# lista z wierzchołkami (słowniki), pole numer i lista z sąsiadami
oryginalny_graf=[
    {"numer": 1,"sasiedzi": [(2,3),(5,1)]},
    {"numer": 2,"sasiedzi": [(1,3),(3,5),(5,4)]},
    {"numer": 3,"sasiedzi": [(2,5), (4,2), (5,6)]},
    {"numer": 4,"sasiedzi": [(3,2), (5,7)]},
    {"numer": 5,"sasiedzi": [(1,1),(2,4),(3,6),(4,7)]}
]

wszystkie_krawedzie=wybierz_krawedzie_z_grafu(oryginalny_graf)
las=daj_las_z_pojedynczymi_drzewami(oryginalny_graf) # lista z grafami, początkowo mamy drzewa jednoelementowe


while len(wszystkie_krawedzie)!=0 and len(las)!=1:
    krawedz=wszystkie_krawedzie.pop(0)   
    waga=krawedz[0]   
    numer_wierzcholka1=krawedz[1]   
    numer_wierzcholka2=krawedz[2]   

    numer_drzewa_dla1=w_ktorym_drzewie_jest_wierzcholek_o_numerze(las,numer_wierzcholka1)   
    numer_drzewa_dla2=w_ktorym_drzewie_jest_wierzcholek_o_numerze(las,numer_wierzcholka2)   

    # jeśli należą do różnych drzew    
    if numer_drzewa_dla1 != numer_drzewa_dla2 and numer_drzewa_dla1!=-1 and numer_drzewa_dla2!=-1:
        las[numer_drzewa_dla1]= las[numer_drzewa_dla1]+las[numer_drzewa_dla2]   
        las.pop(numer_drzewa_dla2)   
        polacz_dwa_wierzcholki_w_grafie(las[numer_drzewa_dla1], numer_wierzcholka1, numer_wierzcholka2, waga)   


# las zawiera wszyskie drzewa
print("POLACZENIA W DRZEWIE SPINAJACYM")
for drzewo in las:
    for wierz in drzewo:
        for sasiad in wierz["sasiedzi"]:   
            print(f"{wierz["numer"]} <--> {sasiad[0]}, waga: {sasiad[1]}")   