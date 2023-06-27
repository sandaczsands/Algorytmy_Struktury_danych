import random
import time

def dynamiczny(Waga, przedmioty, n): 
    wartosci = [wartosc for wartosc, _ in przedmioty]
    wagap = [waga for _, waga in przedmioty]

    P = [[0 for x in range(Waga + 1)] for x in range(n + 1)]
    #macierz o wymiarze(n+1)x(W+1)
    
    for i in range(n + 1): #rozpatrujemy przedmioty
        for j in range(Waga + 1): #rozpatrujemy plecak o wadze j
            if i == 0 or j == 0:
                P[i][j] = 0
            elif wagap[i-1] > j: #jesli przedmiot nie miesci się
                P[i][j] = P[i-1][j] #bierzemy powyższy wynik
            else:
                P[i][j] = max(P[i-1][j], P[i-1][j-wagap[i-1]] + wartosci[i-1])
                #wieksza wartosc z plecakiem z przedmiotem czy bez niego
                
    #for i in range(len(P)):
        #print(P[i])
    return P[n][Waga]  # ostatni element macierzy

def zachlanny(Waga, przedmioty):
    wybraneprzedmioty=[]
    # sort wedlug wartosc na wage (najwieksza oplacalnosc)
    przedmioty.sort(key=lambda x: x[0]/x[1], reverse=True)
    i = 0
    wynik = 0

    #dopoki jest miejsce w plecaku i nie obejrzelismy wszystkich przedmiotow
    while Waga > 0 and i < len(przedmioty):
        wartosc, waga = przedmioty[i]
        if waga <= Waga:
            Waga -= waga
            wynik += wartosc
            wybraneprzedmioty.append((wartosc,waga))
        i += 1
    return wynik, wybraneprzedmioty

def silowy(wartosci, wagap, Waga):
    n = len(wartosci)
    max = 0
    rozwiazanie = []

    #wszystkie mozliwe kombinacje
    for i in range(2 ** n):
        kombinacja = []
        wag = 0
        fx = 0
        for j in range(n):
            if (i >> j) & 1:
                kombinacja.append(j)
                wag += wagap[j]
                fx += wartosci[j]

        if wag <= Waga and fx > max:
            max = fx
            rozwiazanie = kombinacja
    
    wybraneprzedmioty=[(przedmioty[i][0],przedmioty[i][1])for i in rozwiazanie]
    return max, wybraneprzedmioty
'''
Waga = 8
przedmioty = [(4, 2), (3, 1), (6, 4), (8,4)]
n = len(przedmioty)
Wag = 7
inny = [(5,2),(4,1),(12,4),(2,1),(10,3)]
n1 = len(inny)
'''

def generator(n, waga):
    items = []
    for _ in range(n):
        size = random.randint(1, 10)
        value = random.randint(1, 200)
        items.append((size, value))

    with open("itemy.txt", "w") as file:
        file.write(f"{n} {waga}\n")
        for item in items:
            file.write(f"{item[0]} {item[1]}\n")
            
for j in range(1000,5000,500):#liczba elementow
    for i in range(50,200,10): #pojemnosc
        ilosc_elementow = j
        pojemnosc = i
        generator(ilosc_elementow, pojemnosc)

        with open("itemy.txt",'r') as plik:
            n, Waga=map(int, plik.readline().split())

            przedmioty=[]
            for x in range(n):
                wartosc, wagp =map(int, plik.readline().split())
                przedmioty.append((wartosc, wagp))

            print("ile ele",ilosc_elementow, "waga",pojemnosc)
            #print(przedmioty)
            #start=time.time()
            #wynikd= dynamiczny(Waga, przedmioty, n)
            #koniec=time.time()
            #print("Wynik dla plecaka(dynamiczny):", wynikd)

            #start=time.time()
            #wynikz = zachlanny(Waga, przedmioty)
            #koniec=time.time()
            #print("Wynik dla plecaka(zachlanny):", wynikz)
                
            wartosci = [x[0] for x in przedmioty]
            wagi = [x[1] for x in przedmioty]
            
            #start=time.time()
            #wyniks = silowy(wartosci, wagi, Waga)
            #koniec=time.time()
            #print("Wynik dla plecaka(silowy):", wyniks)
            #print(koniec-start)