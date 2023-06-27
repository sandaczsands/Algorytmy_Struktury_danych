import random
import sys
import time
from collections import deque
sys.setrecursionlimit(1000000)

class m_sasiedzstwa:  
    def __init__(self, wierzcholki):
        self.V = wierzcholki
        self.graph = [[0 for kol in range(wierzcholki)]
                      for wiersz in range(wierzcholki)] 

    def add(self, u, v):
        self.graph[u][v] = 1

    def print_(self):
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print("")

    def kahn(self):
        in_degree = [0] * self.V
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    in_degree[j] += 1 #stopien wchodzących do j
        kolejka = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                kolejka.append(i)
        sort = []
        while kolejka:
            node = kolejka.popleft()
            sort.append(node)
            for i in range(self.V):
                if self.graph[node][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        kolejka.append(i)
        if len(sort) != self.V:
            print("Graf zawiera cykl!")
        else:
            print(sort)
            return sort


    def dfs(self):
        
        def traverse_dfs(node, visited, sort):
            visited.add(node)
            for neighbor in range(self.V):
                if self.graph[node][neighbor] and neighbor not in visited:
                    traverse_dfs(neighbor, visited, sort)
            sort.append(node)

        visited = set()
        sort = []
        for node in range(self.V):
            if node not in visited:
                traverse_dfs(node, visited, sort)
                
        sort.reverse()
        
        # Sprawdzenie, czy istnieje cykl
        for node in range(self.V):
            for neighbor in range(self.V):
                if self.graph[node][neighbor] and sort.index(neighbor) < sort.index(node):
                    print("Graf zawiera cykl!")
                    return None
                   
        print(sort)
        return sort


class m_grafu:
    def __init__(self, wierzchołki):
        self.V=wierzchołki
        self.graph=[[0 for kol in range(wierzchołki+3)]for wier in range(wierzchołki)]

    def create(self,filename):
        with open('graph.txt') as f:
            w, e = map(int, f.readline().split()) #pierwszy wiersz to liczba wierzcholkow i krawedzi
            nast=[[] for i in range(self.V)]
            poprz=[[] for i in range(self.V)]

            for i in range(e):
                u, v = map(int, f.readline().split()) #u rozpoczyna krawedz v kończy
                nast[u].append(v) 
                poprz[v].append(u)
     
        #tworzenie 1 i 2 dodatkowej kolumny
        for i in range(self.V):
            if nast[i]:
                self.graph[i][self.V]=nast[i][0]
            if poprz[i]:
                x=poprz[i][0]
                x=x+self.V
                self.graph[i][self.V+1]=x

        #3 kol
        for wiersz in range(0,self.V):
            for kol in range(0,self.V+1): #dla i sprawdzamy wszystikie j czy są w nast albo poprzed
                if not(kol in nast[wiersz]) and not(kol in poprz[wiersz]):
                    self.graph[wiersz][self.V+2]= kol*(-1)
                    break 
                
        #wypełnienie macierzy v x v
        for wiersz in range(self.V):
            for kol in range(self.V):
                if kol in nast[wiersz]:
                    index = nast[wiersz].index(kol)
                    if index == len(nast[wiersz])-1:
                        self.graph[wiersz][kol] = nast[wiersz][index]
                    else:
                        self.graph[wiersz][kol] = nast[wiersz][index+1]
          
        for wiersz in range(self.V):
            for kol in range(self.V):
                if kol in poprz[wiersz]:
                    index = poprz[wiersz].index(kol)
                    if index == len(poprz[wiersz])-1:
                        self.graph[wiersz][kol] = poprz[wiersz][index] + self.V
                    else:
                        self.graph[wiersz][kol] = poprz[wiersz][index+1] + self.V
         
        for wiersz in range(0,self.V):
            for kol in range(0,self.V):
                if not(kol in nast[wiersz]) and not(kol in poprz[wiersz]):
                    z=kol
            for kol in range(0,self.V):
                if not(kol in nast[wiersz]) and not(kol in poprz[wiersz]):
                    self.graph[wiersz][kol]=z*(-1)
        #print(nast)
        #print(poprz)

    def add(self, u, v):    
        #informacja o nastepnikach
        if self.graph[u][self.V] == "-":
            self.graph[u][self.V] = v
            self.graph[u][v] = v
        else:
            #y=0
            x=self.graph[u][self.V]
            while self.graph[u][x]!=x: #petla jesli nie ma wiecej
                #y+=1
                #if y==self.V+1:
                    #break
                #else:
                x=self.graph[u][x]
            #if y!=self.V+1:
            self.graph[u][x]=v
            self.graph[u][v]=v
            
        #info o poprzednikach       
        if self.graph[v][self.V+1] == "-":
            self.graph[v][self.V+1] = u+self.V
            #self.graph[v][u] = u+self.V
        else:
            y=0
            x =self.graph[v][self.V+1]
            x=x-self.V 
            while self.graph[v][x]!= "-":
                y+=1
                if y==self.V+1:
                    break
                else:
                    x = self.graph[v][x]
                    x=x-self.V 
            if y!=self.V+1:
                self.graph[v][x]= u+self.V

    def kahn(self):
        # tworzenie tablicy in_degree
        in_degree = [0] * self.V
        for i in range(self.V):
            for j in range(self.V):
                if 0<=self.graph[i][j]<self.V:
                    in_degree[j] += 1
        kolejka = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                kolejka.append(i)
        # sortowanie topologiczne
        sort = []
        while kolejka:
            node = kolejka.popleft()
            sort.append(node)
            for i in range(self.V):
                if 0<=self.graph[node][i]<self.V:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        kolejka.append(i)
        if len(sort) != self.V:
            print("Graf zawiera cykl")
        else:
            print(sort)
            return sort

    def dfs(self):
        def traverse_dfs(node, visited, sort):
            visited.add(node)
            for neighbor in range(self.V):
                if neighbor not in visited and 0<=self.graph[node][neighbor]<self.V:
                    traverse_dfs(neighbor, visited, sort)
            sort.append(node)

        visited = set()
        sort = []
        for node in range(0,self.V):
            if node not in visited:
                traverse_dfs(node, visited, sort)
                
        sort.reverse()

        for node in sort:
              for node2 in sort:
                    if sort.index(node) < sort.index(node2) and 0<=self.graph[node2][node]<self.V:
                        print("Graf zawiera cykl")
                        return None;         
        print(sort)
        return sort
     
    def print_(self):
        for i in range(self.V):
            for j in range(self.V+3):
                print(self.graph[i][j], end=" ")
            print("")   


    
def generator(ilosc_w, ilosc_k, plik):
    with open(plik, 'w') as f:
        f.write(str(ilosc_w) + ' ' + str(ilosc_k) + '\n')
        wierzcholki = list(range(ilosc_w)) #lista od 0 do ilosc_w-1
        edges = set()# [ _, _]
        while len(edges) < ilosc_k:
            u, v = random.sample(wierzcholki, 2)
            if u < v and (u, v) not in edges:
                edges.add((u, v))
            elif u > v and (v, u) not in edges:
                edges.add((v, u))
        for edge in edges:
            f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')



for i in range(1,2):
    n=5
    n=n*i
    m=(n*(n-1))//2
    #generator(n, m, 'graph.txt')
    g=m_grafu(n)
    g.create('graph.txt')
    #g.print_()
    g.dfs()
    #g.kahn()
    #g.print_()
    '''
    with open('graph.txt') as f:
        v, e = map(int, f.readline().split()) #pierwszy wiersz to liczba wierzcholkow i krawedzi
        g1 = m_sasiedzstwa(v)
        for i in range(e):
            u, v = map(int, f.readline().split()) #u rozpoczyna krawedz v kończy
            g1.add(u, v)
        #g1.print_()
        #pocz=time.time()
        g1.dfs()
        g1.kahn()
        #koniec=time.time()
        #print(koniec-pocz)'''
        
