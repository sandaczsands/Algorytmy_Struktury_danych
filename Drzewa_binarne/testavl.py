import time, sys
sys.setrecursionlimit(10**8)

#fragment drzewa
class node(object):
    def __init__(self, key):
        self.key = key #klucz do zindetyfikowania liścia
        self.left = None
        self.right = None
        self.height = 1


class avl(object):
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
        balance=self.balans(root) 

        #jesli lewe drzewo jest wyzsze i wstawiany klucz jest mniejscy od lewego podrzwa
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        #jesli prawe drzewo jest wyzsze i klucz jest wiekszy od prawego roota
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        #jesli lewe drzewo jest wyzsze ale klucz jest wiekszy od lewego poddrzewa
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
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
            #znajdz najmniejszą wartosc w prawym poddrzewie
            temp=self.nowyrodzic(root.right)
            root.key = temp.key
            root.right = self.usuń(root.right, temp.key)
        if not root:
            return root
        root.height = 1 + max(self.wysokosc(root.left),self.wysokosc(root.right)) #zmiana wysokosci
        
        balance=self.balans(root) 

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    def nowyrodzic(self, root):
        if not root.left:
            return root
        return self.nowyrodzic(root.left)
 
    def minimum(self, root):
        if root is None or root.left is None:
            print(root.key)
            return root
        else:
            print(root.key, "->",end=" ") 
            return self.minimum(root.left)

    def maksimum(self, root):
        if root is None or root.right is None:
            print(root.key)
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
  
    def usuńwezly(self):
        n = int(input("Podaj ilość węzłów do usunięcia: "))
        for i in range(n):
            wartosc = int(input("Podaj wartość węzła do usunięcia: "))
            self.usuń(root, wartosc)
             
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
    
    def balans(self, root):
        if not root:
            return 0
        return self.wysokosc(root.left) - self.wysokosc(root.right)

    def isBalanced(self,root):
        if root is None:
            return True
    
        lw = self.wysokosc(root.left)
        rw = self.wysokosc(root.right)
    
        if (abs(lw - rw) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True: return True
        else:
            return False
       
               
    def usuńpostorder(self,root):
        if root:
            self.usuńpostorder(root.left)
            self.usuńpostorder(root.right)
            print(root.key)
            del root
       
    def wysokosc(self, root):
        if not root:
            return 0
        return root.height
    
    
struktura = avl()
root = None
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in a:
    root=struktura.wstaw(root,i)
 
print("wstawione") 

if (struktura.isBalanced(root) == 0):
        print("Not Balanced")
else:
        print("Balanced")

struktura.maksimum(root)
print("")
struktura.minimum(root)  
print("") 
struktura.inorder(root)
print("") 
struktura.preorder(root)
print("") 
struktura.postorder(root)
print("") 
struktura.preorder_key(root,4)
print("")
struktura.usuńwezly( )



