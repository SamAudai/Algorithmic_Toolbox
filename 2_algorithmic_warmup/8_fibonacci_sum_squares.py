# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    if(n >= 60):
        n = n % 60;
            
    currentValue = 1;
    previousValue = 0;
    sum = 0;
    if (n <= 1):
        return n;  

    while(n):
        currentValue = (currentValue + previousValue);
        previousValue = (currentValue - previousValue);
        sum += previousValue*previousValue;        
        n -= 1;    
    return sum %10;

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))