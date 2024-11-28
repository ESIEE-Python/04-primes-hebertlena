""" programme prime"""
from math import sqrt


#### Fonction secondaire


def isprime(p):
    """fonction pour determiner si un nombre est premier"""
    # votre code ici
    premier = True
    if p==1:
        premier =False
    for diviseur in range(2,int(sqrt(p))+1) :
        if p % diviseur == 0 :
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """fonction main"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
