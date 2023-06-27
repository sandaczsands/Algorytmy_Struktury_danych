import random, time
import sys
sys. setrecursionlimit(10000000)

class m_sasiedzstwa:  
    def __init__(self, wierzcholki):
        self.V = wierzcholki
        self.graph = [[0 for kol in range(wierzcholki)]
                      for wiersz in range(wierzcholki)] 

    def add(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def print_(self):
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print("")

    def euler(self,v): 
        cykl=[]
        def dfs_euler(node,cykl):
            for neighbour in range(self.V):     #przegladamy sasiasdow
                if self.graph[node][neighbour]==1:
                    self.graph[node][neighbour]=0
                    self.graph[neighbour][node]=0      #usuwamy krawedz
                    dfs_euler(neighbour,cykl)
            cykl.append(node)       #dodajemy do tablicy

        dfs_euler(v,cykl)       
        if cykl[0]!=cykl[-1]:
            print("Graf wejściowy nie zawiera cyklu Eulera.")

        else:
            print("Cykl Eulera dla macierzy sąsiedztwa: ")
            print(cykl[::-1])
     
    def hamilton(self):
        def dfs(v, visited, cykl, point):
            cykl[point] = v
            point += 1
            if point == self.V and self.graph[v][0] == 1:
                cykl[point] = 0
                return cykl
            
            visited.add(v)
            for neighbour in range(self.V):
                if self.graph[v][neighbour] == 1 and neighbour not in visited:
                    cykl1 = dfs(neighbour, visited, cykl, point)
                    if cykl1 is not None:
                        return cykl1
            point -= 1
            visited.remove(v) #wycofujemy wierzcholek
            return None
        visited = set()
        cykl = [0] * (self.V + 1) #plus jeden żeby na ostatnim miejscu był pierwszy wierzcholek
        point = 0
        v = 0
        cycle = dfs(v, visited, cykl, point)
        if cycle is not None:
            print("Cykl Hamiltona dla macierzy sąsiedztwa: ")
            print(cycle)
       
        else:
            print("Graf wejściowy nie zawiera cyklu Hamiltona.")
     


class lista_nastepnikow:
    def __init__(self, wierzcholki):
        self.V = wierzcholki
        self.lista=[[] for i in range(wierzcholki)]
    
    def add(self,u,v):
        self.lista[u].append(v)
                
    def print_(self):
        print(self.lista)
        
    def euler(self, v):
        def dfs_euler(node, cykl):
            while visited[node]: #przechodzimy przez nastepniki node'a
                neighbour = visited[node].pop(0) #usuwamy krawedz
                dfs_euler(neighbour, cykl)
            cykl.append(node)
        
       
        cykl = []
        visited = []
        for node in range(self.V):
            visited.append(list(self.lista[node]))  #dodajemy wszystkie nastepniki do tablicy
                                                    #np visited [0] = nastepniki zera
        dfs_euler(v, cykl)

        if cykl[0] != cykl[-1]:
    
            print("Graf wejściowy nie zawiera cyklu Eulera.")
        else:
            print("Cykl Eulera dla listy następników: ")
            print(cykl[::-1])
        

    def hamilton(self):
        def dfs(v, visited, cykl, point):
            cykl[point] = v
            point += 1
            if point == self.V and 0 in self.lista[v] :
                cykl[point] = 0
                return cykl
            
            visited.add(v)
            for neighbour in self.lista[v]:
                if neighbour not in visited:
                    cykl1 = dfs(neighbour, visited, cykl, point)
                    if cykl1 is not None:
                        return cykl1
            point -= 1
            visited.remove(v)
            return None

        visited = set()
        cykl = [0] * (self.V + 1)
        point = 0
        v = 0
        cycle = dfs(v, visited, cykl, point)
        if cycle is not None:
            print("Cykl Hamiltona dla listy następników: ")
            print(cycle)
        else:
            print("Graf wejściowy nie zawiera cyklu Hamiltona.")


def generator(ilosc_w, ilosc_k, plik):
    with open(plik, 'w') as f:
        f.write(str(ilosc_w) + ' ' + str(ilosc_k) + '\n')
        edges = set()
        while len(edges) < ilosc_k:
            u, v = random.randint(0, ilosc_w-1), random.randint(0, ilosc_w-1)
            if u != v and (u, v) not in edges and (v, u) not in edges:
                edges.add((u, v))
        for edge in edges:
            f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')

for i in range(1,11):
    n=10*i #100, 200, ... , 1000
    #print(n)
    for j in range(1,10):
        #ustawianie ilosci krawedzi
        procent=j*10
        #print(j)
        m = int(((n*(n-1)) * (procent/ 100)) / 2)  # nieskierowany
        #m= int((n*(n-1)) * (procent/ 100))   #skierowany

        #print(m)
        generator(n, m, 'graph.txt')
        with open('graph.txt') as f:
            v, e = map(int, f.readline().split()) #pierwszy wiersz to liczba wierzcholkow i krawedzi
            g1 = m_sasiedzstwa(v)
            #g2 = lista_nastepnikow(v)
            for i in range(e):
                    u, v = map(int, f.readline().split())
                    g1.add(u,v)
                    #g2.add(u,v)
            start=time.time()
            #g2.hamilton()
            g1.euler(0)
            #g1.cykl_hamiltona()
            kon=time.time()
            print(kon-start)
        
