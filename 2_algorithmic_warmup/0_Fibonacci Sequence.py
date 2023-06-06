#Fibonacci sequence.
def fibonacci(n):
    fibSequence = [0];
    currentValue = 1;
    previousValue = 0;

    if(n <= 1):
        return n;            
    counter = n;
    while(counter):
        currentValue += previousValue;
        previousValue = currentValue - previousValue;
        fibSequence.append(previousValue%10)
        counter -= 1;
    return fibSequence;

n = int(input("Enter your number: "));
print(fibonacci(n));