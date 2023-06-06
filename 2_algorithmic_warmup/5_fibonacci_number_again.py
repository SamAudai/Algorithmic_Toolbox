# Uses python3
import sys

def pisanoPeriod (m):    
    # Calculate and return Pisano Period   
    previous, current = 0, 1;    
    for i in  range (0, m*m):
        previous, current = current, (previous + current) % m;

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1;  

def fibonacci_Number_Again(n, m):    
    # period length
    n = n % pisanoPeriod(m);
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current = current, previous + current;

    return current % m;

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_Number_Again(n, m))
#print(fibonacci_Number_Again(213588, 512));

