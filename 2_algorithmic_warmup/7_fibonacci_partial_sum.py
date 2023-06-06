# Uses python3
import sys
def fibonacci(n):    
    currentValue = 1;
    previousValue = 0;
    if(n <= 1):
        return n;

    while(n):
        currentValue += previousValue;
        previousValue = currentValue - previousValue; 
        n -= 1;       
    return previousValue %10;
       
def fibonacci_partial_sum(n, m):
    count = 0;
    n = n % 60;
    m = m % 60;
    
    if(n > m):
        while(n <= 60):
            count += fibonacci(n);
            n += 1;
        while(m >= 0):
            count += fibonacci(m);
            m -= 1;
        return count %10;
     
    while(n <= m):
        count += fibonacci(n);
        n += 1;       
    return count %10;                   

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to));