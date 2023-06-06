# Uses python3
import sys

def money_change(n):
    count = 0;    
    while(n>=1):
        if(n>=10):            
            n = n-10;
            count +=1;
        if(n<10 and n>=5):
            n = n-5;
            count+=1
        if(n<5 and n>0):
            n = n-1;
            count+=1;    
     
    return count;

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(money_change(m))

