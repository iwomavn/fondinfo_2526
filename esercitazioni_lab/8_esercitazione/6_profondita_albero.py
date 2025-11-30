class Node:
    def __init__(self, name):
        self._name = name
        
    def size(self):
        raise NotImplementedError("metodo astratto")
    
    def print(self, indent):
        raise NotImplementedError("metodo astratto")

    def depth(self):
        raise NotImplementedError("metodo astratto")
    
class Document(Node):
    def __init__(self, name, data):
        self._name = name
        self._data = data
        
    def size(self):
        return len(self._data)
    
    def print(self, indent: int):  
        print(" " * indent + self._name)
    
    def depth(self):
        return 0
        
class Folder(Node):
    def __init__(self, name, children: list[Node]):
        self._name = name
        self._children = children
        
    def size(self):
        size = 0
        for c in self._children:
            size += c.size()
        return size
    
    def print(self, indent: int):  
        print(" " * indent + self._name)
        for n in self._children: 
            n.print(indent + 4)
            
    def depth(self):
        if not self._children:
            return 1
        return 1 + max(n.depth() for n in self._children)

def main():
    a1 = Document("a1.txt", "b")
    prod = Document("prod.csv", "l")
    a2 = Document("a1.txt", "w??????")
    data = Folder("data", [prod])
    work = Folder("Work", [a1, data])
    personal = Folder("Personal", [a2])
    desktop = Folder("Desktop", [work, personal])
    
    print(desktop.size())
    desktop.print(0)  
    print(desktop.depth())
    
if __name__ == "__main__":
    main()