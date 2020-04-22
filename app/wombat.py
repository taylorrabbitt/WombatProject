import random  
from math import gcd

#global variables
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
    Auditing of votes (decryption of ElGamal) -
    decrypts the ciphertext using ElGamal to verify that plaintext 
    and ciphertext match.
    '''
    h = pow(p, key, q)

    #get individual characters of plaintext 
    plaintext = [chr(int(i/h)) for i in ct] 

    voteTest = ''
    for i in pt:
        voteTest += i

    #returns False if plaintext and unencrypted vote do not match
    if pt != voteTest:
        return False
         
    return True 

def encryptVote(vote):
    '''
    Encryption of votes (ElGamal) -
    encrypts the plaintext using ElGamal encryption
    '''
    #Recieve vote from user

    global p
    global key
    global q
    global pt
    global ct

    #update global variables
    pt = vote

    #separate vote into individual characters
    cipher = [vote[i] for i in range(len(vote))]

    q = random.randint(pow(10, 20), pow(10, 50)) 
    g = random.randint(2, q)
    key = genKey(q)
    p = pow(g, key, q)
    s = pow(p, key, q)
    
    #encrypt each character in the vote according to El Gamal Encryption
    for i in range(len(cipher)): 
        cipher[i] = s * ord(cipher[i]) 
    
    #join encrypted characters
    ciphertext = ''
    for i in cipher:
        ciphertext += str(i) 

    #update global variable
    ct = cipher

    return vote, ciphertext
