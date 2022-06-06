
import random
import pandas as pd
import numpy as np
import cv2 
from skimage import img_as_ubyte
my_img = cv2.imread('apple.jpeg')
from block_distortion import distort_image

def power(a,d,n):
  ans=1
  while d!=0:
    if d%2==1:
      ans=((ans%n)*(a%n))%n
    a=((a%n)*(a%n))%n
    d>>=1
  return ans

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = (int)(temp_phi/e)
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q, r):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pqr
    n = p * q * r

    #Phi is the totient of n
    phi = (p-1) * (q-1) * (r-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)    
        
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n), phi)

row,col=my_img.shape[0],my_img.shape[1]
enc = [[0 for x in range(3000)] for y in range(3000)]

def encrypt():
    data1 = pd.read_csv("data1.csv") 
    data2 = pd.read_csv("data2.csv")

    key = int(data2['0'][1]) # e
    n = int(data1['0'][3])


    for i in range(100,900):
        for j in range(100,1000):
            r,g,b=my_img[i,j]
            C1=power(r,key,n)
            C2=power(g,key,n)
            C3=power(b,key,n)
            enc[i][j]=[C1,C2,C3]
            C1=C1%256
            C2=C2%256
            C3=C3%256
            my_img[i,j]=[C1,C2,C3]
    distorted = distort_image(my_img)
    cv2.imwrite('encrypted_img.png',img_as_ubyte(distorted))

def decrypt():
    data1 = pd.read_csv("data1.csv")
    data2 = pd.read_csv("data2.csv")

    key = int(data2['0'][2]) # d
    n = int(data1['0'][3])

    for i in range(100,900):
        for j in range(100,1000):
            r,g,b=enc[i][j]
            M1=power(r,key,n)
            M2=power(g,key,n)
            M3=power(b,key,n)
            my_img[i,j]=[M1,M2,M3]
    cv2.imwrite('decrypted_img.png', my_img)
    
if __name__ == '__main__':
    primes=[]
    total_no_primes = 0
    with open('primes.txt') as pfile:
        for line in pfile:
            primes.append(int(line)) 
            total_no_primes += 1
    p = primes[random.randint(1, total_no_primes-1)]
    q = primes[random.randint(1, total_no_primes-1)]
    r = primes[random.randint(1, total_no_primes-1)]


    print("Generating your public/private keypairs now . . .")
    public, private, phi = generate_keypair(p, q, r)
    print("\nYour public key is ", public ," and your private key is ", private)

    data1 = [p, q, phi, public[1]]  #  p, q, phi, n
    df = pd.DataFrame(data1)
    df.to_csv('data1.csv') # offline storage of p, q, phi, n in table 1

    data2 = [r, public[0], private[0]] #  r, e, d
    df = pd.DataFrame(data2)
    df.to_csv('data2.csv') #offline storage of r, e, d in table 2

    
    encrypt()
    print("\nEncryption done")
    print("\nDecrypting message with private key ", private ," . . .")
    decrypt()
    print("\nDecryption Done:")
    
