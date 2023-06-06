# Uses python3
import sys 

def fibonacci_sum_last_digit(n):
    
    if(n >= 60):
        n = n % 60;
        
    currentValue = 1;
    previousValue = 0;
    count = 0;
    if(n <= 1):
        return n;           
    
    while(n):
        currentValue = (currentValue + previousValue);
        previousValue = (currentValue - previousValue);
        count += previousValue;
        n -= 1;
    return count %10;

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))