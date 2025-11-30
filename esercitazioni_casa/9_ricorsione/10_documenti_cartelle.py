class Node:
    def __init__(self, name):
        self._name = name


class Document(Node):
    def __init__(self, name, data):
        self._name = name
        self._data = data
        
class Folder(Node):
    def __init__(self, name, children: list[Node]):
        self._name = name
        self._children = children
        
def main():
    a1 = Document("a1.txt", None)
    prod = Document("prod.csv", None)
    a2 = Document("a1.txt", None)
    data = Folder("data", [prod])
    work = Folder("Work", [a1, data])
    personal = Folder("Personal", [a2])
    desktop = Folder("Desktop", [work, personal])
    
if __name__ == "__main__":
    main()