#uses python 3
import sys

def lastDigit_Fibonacci(n):    
    currentValue = 1;
    previousValue = 0;           
    counter = n;

    while(counter):
        currentValue += previousValue;
        previousValue = (currentValue - previousValue) % 10;       
        counter -= 1;
    return previousValue;


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(lastDigit_Fibonacci(n))