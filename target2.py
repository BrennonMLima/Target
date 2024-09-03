def verify(string):
    string_lower = string.lower()
    contador = string_lower.count('a')
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

def main():
    string = input("Digite uma string: ")
    
    verify(string)

if __name__ == "__main__":
    main()
