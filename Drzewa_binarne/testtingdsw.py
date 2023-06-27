import time, sys, random, math
sys.setrecursionlimit(10**8)
#fragment drzewa
class node(object):
    def __init__(self, key):
        self.key = key #klucz do zindetyfikowania liścia
        self.left = None
        self.right = None
        self.height = 1


class bst(object):
    def __init__(self):
        self.root = None # odniesienie do korzenia

    def wstaw(self, root, key):
        if not root: #jesli drzewo nie istnieje to powstaje pierwszy root
            return node(key) 
        elif key < root.key:
            root.left = self.wstaw(root.left, key)
        else:
            root.right = self.wstaw(root.right, key)
            
        root.height = 1 + max(self.wysokosc(root.left),self.wysokosc(root.right)) #nadajemy wysokosc       
        return root
    
    def usuń(self, root, key):
        if not root:
            return None
        elif key < root.key:
            root.left = self.usuń(root.left, key)    
        elif key > root.key: 
            root.right = self.usuń(root.right, key)
        else: #kiedy znajdziemy wezel
            if not root.left:
                temp = root.right
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp
            temp=self.nowyrodzic(root.right)
            root.key = temp.key
            root.right = self.usuń(root.right, temp.key)
        if not root:
            return root
        root.height = 1 + max(self.wysokosc(root.left),self.wysokosc(root.right)) #zmiana wysokosci
        return root
    
    def nowyrodzic(self, root):
        if root.left is None or root is None:
            return root
        return self.nowyrodzic(root.left) 
    
    def usuńwezly(self):
        n = int(input("Podaj ilość węzłów do usunięcia: "))
        for i in range(n):
            wartosc = int(input("Podaj wartość węzła do usunięcia: "))
            self.usuń(root, wartosc)

    def minimum(self, root):
        if root is None or root.left is None:
            return root
        else:
            print(root.key, "->",end=" ") 
            return self.minimum(root.left)

    def maksimum(self, root):
        if root is None or root.right is None:
            return root
        else:
            print(root.key, "->",end=" ")
            return self.maksimum(root.right)

    def preorder(self,root):
        if root is not None:
            print(root.key,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key,end=" ")
        
    def inorder(self,root):
        if root is None: 
            return
        if root is not None:
            self.inorder(root.left)
            print(root.key,end=" ")
            self.inorder(root.right)
                  
    def preorder_key(self, root, key):
        if root is None:
            return
        if root.key == key:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            return
        self.preorder_key(root.left, key)
        self.preorder_key(root.right, key)
    
    
    def usuńpostorder(self,root):
        if not root:
            return 
        self.usuńpostorder(root.left)
        self.usuńpostorder(root.right)
        print(root.key)
        del root
    
    def wysokosc(self, root):
        if not root:
            return 0
        return root.height
    
    def rightRotate(self, y):
 
        x = y.left
        T2 = x.right
 
        #rotacja w prawo
        x.right = y
        y.left = T2
 
        # wysokosci
        y.height = 1 + max(self.wysokosc(y.left),
                          self.wysokosc(y.right))
        x.height = 1 + max(self.wysokosc(x.left),
                          self.wysokosc(x.right))
 
        # nowy root 
        return x
    
    def leftRotate(self, x):
 
        y = x.right
        T2 = y.left
 
        # rotacja
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self.wysokosc(x.left),
                          self.wysokosc(x.right))
        y.height = 1 + max(self.wysokosc(y.left),
                          self.wysokosc(y.right))
 
        return y
 

    def isBalanced(self,root):
        if root is None:
            return True
    
        lw = self.wysokosc(root.left)
        rw = self.wysokosc(root.right)
    
        if (abs(lw - rw) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True: return True
        else:
            return False
    
    
def backbone(grand: node):
    count = 0 #ilosc wezlow
    tmp = grand.right
    #pointer do przechodzenia przez drzewo
    
    # dopoki nie przejdziemy do konca drzewa
    while tmp:
        # jesli istnieje lewy wezel to dokonujemy rotacji w prawo
        if tmp.left:
            oldTmp = tmp
            tmp = tmp.left
            oldTmp.left = tmp.right
            tmp.right = oldTmp
            grand.right = tmp
 
        # jak lewe wezly sie skonczyly to przechodzimy do nastepnego prawego wezla
        else:
            count += 1
            grand = tmp
            tmp = tmp.right
 
    return count
 

def compress(grand: node, m: int):
    #m ilosc wezlow do skompresowania
    tmp = grand.right
 
    # Począwszy od korzenia szukamy pierwszego węzła który ma lewe poddrzewo.
    #rotacja w lewo
    for i in range(m):
        oldTmp = tmp
        tmp = tmp.right
        grand.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        grand = tmp
        tmp = tmp.right
 

def balanceBST(root: node):
    grand = node(0) #korzeń
    grand.right = root
 
    # ilosc wezlow w liscie
    count = backbone(grand)
 
    # wysokosc pelnego drzewa
    h = int(math.log2(count + 1))
 
    # ilosc wezlow do wstawienia do drzewa o wysokosci h
    m = pow(2, h) - 1
 
    compress(grand, count - m)
    # rotacja w lewo 
    # od gory do osiagniecia dolu drzewa
    for m in [m // 2**i for i in range(1, h + 1)]:
        compress(grand, m)
 
    return grand.right   

struktura=bst()
root=None
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    root=struktura.wstaw(root,i)
    
struktura.Dsw()

for i in range(1,11):
    x=[]
    n=1000*i
    for j in range(10,n):
        x.append(j)
    x=x[::-1]
    random.shuffle(x)
    for j in x:
        root=struktura.wstaw(root,j)   
    #struktura.preorder(root)
    #struktura.preorder(root)
    #struktura.postorder(root)
    start=time.time()
    struktura.DSW(root)
    end=time.time()
    print(end-start)
    #struktura.preorder(root)