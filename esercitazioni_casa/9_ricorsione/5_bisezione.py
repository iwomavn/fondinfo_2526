def f(x):
    return x ** 3 - x - 1
        
def bisezione(a, b):
    c = (a + b) / 2
    if abs(f(c)) < 0.001:
        return c
    elif f(a) * f(c) < 0:
        return bisezione(a, c)
    else:
        return bisezione(c, b)

def main():
    print(bisezione(1, 2))
    
if __name__ == "__main__":
    main()