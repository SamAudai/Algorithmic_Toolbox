# Uses python3
import sys

def lcm(n,m):    
    current_gcd = 0;
    current_lcm = n*m;
    if(n == m):
        return m;
    while(n != m):
        if(n > m):
            n = n - m;
        else:
            m = m - n;
        current_gcd = n;
    return int(current_lcm / current_gcd);

n = int(input("Enter number 1: "));
m = int(input("Enter number 2: "));
print(lcm(n, m));

#if __name__ == "__main__":
    #input = sys.stdin.read()
    #a, b = map(int, input.split())
    #print(lcm(a, b))