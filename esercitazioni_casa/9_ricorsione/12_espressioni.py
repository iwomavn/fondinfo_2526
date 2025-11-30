class Expression:
    def __init__(self, value=None):
        self._value = value
        
    def eval(self):
        raise NotImplementedError("metodo astratto")

class Literal(Expression):
    def __init__(self, value: float):
        super().__init__(value)
        
    def eval(self):
        return self._value

class Product(Expression):
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right
        
    def eval(self):
        return self._left.eval() * self._right.eval()

class Sum(Expression):
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right
        
    def eval(self):
        return self._left.eval() + self._right.eval()
 
def main():
    tre = Literal(3)
    due = Literal(2)
    quattro = Literal(4)
    cinque = Literal(5)
    
    tre_per_due = Product(tre, due)
    somma = Sum(tre_per_due, quattro)
    finale = Product(cinque, somma)
    print(finale.eval())
    
if __name__ == "__main__":
    main()