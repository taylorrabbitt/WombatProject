import random  
from math import pow


def encryptVote(msg):
    '''
    Encryption of votes (ElGamal)
        -Function that takes vote and encrypts using ElGamal -> returns
        (plaintext, ciphertext)
    '''

    a = random.randint(2, 10) 
  
    def gcd(a, b): 
        if a < b: 
            return gcd(b, a) 
        elif a % b == 0: 
            return b; 
        else: 
            return gcd(b, a % b) 
  
    # Generating large random numbers 
    def gen_key(q): 
  
        key = random.randint(pow(10, 20), q) 
        while gcd(q, key) != 1: 
            key = random.randint(pow(10, 20), q) 
  
        return key 
  
    # Modular exponentiation 
    def power(a, b, c): 
        x = 1
        y = a 
  
        while b > 0: 
            if b % 2 == 0: 
                x = (x * y) % c; 
            y = (y * y) % c 
            b = int(b / 2) 
  
        return x % c  
  
    en_msg = []
    q = random.randint(pow(10, 20), pow(10, 50)) 
    g = random.randint(2, q)
    key = gen_key(q)
    h = power(g, key, q)
  
     
    s = power(h, key, q)
    p = power(g, key, q) 
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
   
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p



def auditVote():
    '''
    Auditing of votes (decryption of ElGamal)
        -Function that takes both plaintext and ciphertext
        and decrypts the ciphertext using ElGamal to verify
        that plaintext and ciphertext match, if not throw error
    '''
    pass



def tallyProcess():
    '''
    Tallying Process
        -Verifiable mix-net  -> shuffle votes and reencrypt 
        -Decrypt all mixed votes 
        -Count for winner
    '''
    pass



#Test code  
if __name__ == '__main__': 
    msg = 'encryption'
    print(encryptVote(msg)) 
