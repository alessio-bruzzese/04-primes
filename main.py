"""module qui vérifie les nombres premiers"""

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """fonction vérifiant que le nombre passé en paramètre est premier"""
    # votre code ici
    prime = True

    if p==1 :
        return False

    for i in range (2, int(sqrt(p))+1):
        if p%i==0:
            prime = False
    return prime

#### Fonction principale

def main():
    """permet le test sur 5 nombres"""
    # vos appels à la fonction secondaire ici

    print(isprime(1))
    print(isprime(2))
    print(isprime(67))
    print(isprime(45))
    print(isprime(60))


if __name__ == "__main__":
    main()
