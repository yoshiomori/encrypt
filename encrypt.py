from string import printable
from decimal import Decimal

def mdc(a,b):
    return max(i+1 for i in range(min(a,b)) if a%(i+1)==0 and b%(i+1)==0)

def primo(n):
    for i in range(n):
        if (i+1)!=1 and (i+1)!=n and n%(i+1)==0:
            return False
    return True

p = max(ord(c) for c in printable)
while not primo(p):
    p+=1
q=p+1
while not primo(q):
    q+=1
n=p*q
e=2
while primo(e) or mdc(e,(p-1)*(q-1))!=1:
    e+=1
d=2
while primo(d) or (e*d)%((p-1)*(q-1))!=1:
    d+=1
    print(f'\r{d}',end='')
print(f'\r{" "*len(str(d))}\r',end='')

def encrypt(m):
    return [(ord(c)**e)%n for c in m]

def decrypt(i_list):
    return ''.join(chr((i**d)%n) for i in i_list)
