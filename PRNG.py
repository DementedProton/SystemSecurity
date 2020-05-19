from math import sqrt

import random

def confirmPrime(p):
    # test if n is even
    if p % 2 == 0:
        return False
    for i in range(3, int(sqrt(p)), 2):
        if p % i == 0:
            return False
    return True

def goodPrime(p):
    return p % 4 == 3 and confirmPrime(p)
 
def findGoodPrime(numBits=32):
    # Find a good prime of 16 bits
    candidate = 1
    while not goodPrime(candidate):
        candidate = random.getrandbits(numBits)
    return candidate
 
def makeModulus():
    return findGoodPrime() * findGoodPrime()
 
def parity(n):
    return sum(int(x) for x in bin(n)[2:]) % 2
 
class BlumBlumShub(object):
    def __init__(self, seed=None):
        self.modulus = makeModulus()
        self.state = seed if seed is not None else random.randint(2, self.modulus - 1)
        self.state = self.state % self.modulus
 
    def seed(self, seed):
        self.state = seed
 
    def bitstream(self):
        while True:
            yield parity(self.state)
            self.state = pow(self.state, 2, self.modulus)
 
    def bits(self, n=20):
        outputBits = ''
        for bit in self.bitstream():
            outputBits += str(bit)
            if len(outputBits) == n:
                break
 
        return outputBits

generator = BlumBlumShub()

print(int(generator.bits(6), 2))
