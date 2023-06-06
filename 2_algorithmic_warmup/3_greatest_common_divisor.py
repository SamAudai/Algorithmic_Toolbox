# Uses python3
import sys

def gcd(n, m):
    
    if(m == 0):
        return n;    
        
    return gcd(m, n % m);

n = int(input("Enter number 1: "));
m = int(input("Enter number 2: "));
print(gcd(n, m));


#if __name__ == "__main__":
    #input = sys.stdin.read()
    #a, b = map(int, input.split())
    #print(gcd(a, b))