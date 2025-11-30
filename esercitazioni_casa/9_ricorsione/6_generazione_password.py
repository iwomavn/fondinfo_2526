def pass_gen(n, simboli):
    passwords = []
    
    if n == 0:
        return ['']
    else:
        for s in simboli:
            password = pass_gen(n-1, simboli)
            
            for p in password:
                passwords.append(s + p)
        
    return passwords

def main():
    print(pass_gen(5, "abcdefg"))
    
if __name__ == "__main__":
    main()