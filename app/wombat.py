import random  
from math import gcd
  
p = None
key = None
q = None
pt = None
ct = None
# Generates a random key 
def genKey(q): 
  
    key = random.randint(pow(10, 20), q) 
    while gcd(q, key) != 1: 
        key = random.randint(pow(10, 20), q) 
  
    return key 
  
def auditVote():
    '''
    Auditing of votes (decryption of ElGamal)
        -Function that takes both plaintext and ciphertext
        and decrypts the ciphertext using ElGamal to verify
        that plaintext and ciphertext match
    '''
    h = pow(p, key, q) 
    plaintext = [chr(int(i/h)) for i in ct] 

    voteTest = ''
    for i in pt:
        voteTest += i

    if pt != voteTest:
        return False
         
    return True 

def encryptVote(vote):
    '''
    Encryption of votes (ElGamal)
        -Function that takes vote and encrypts using ElGamal -> returns
        (plaintext, ciphertext)
    '''
    #Recieve vote from user

    global p
    global key
    global q
    global pt
    global ct

    pt = vote

    cipher = [vote[i] for i in range(len(vote))]

    q = random.randint(pow(10, 20), pow(10, 50)) 
    g = random.randint(2, q)
    key = genKey(q)
    p = pow(g, key, q)
    s = pow(p, key, q)
    
    #encrypt each character in the vote 
    for i in range(len(cipher)): 
        cipher[i] = s * ord(cipher[i]) 
    
    ciphertext = ''
    for i in cipher:
        ciphertext += str(i) 
    ct = cipher

    return vote, ciphertext
