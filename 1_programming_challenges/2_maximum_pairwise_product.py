#python3
import sys
def max_pairwise_product(numbers):         
    n = len(numbers);
    numbers.sort();        
    return(numbers[n-1] * numbers[n-2]);

if __name__ == '__main__':
    print("Enter elements of Array: ")
    input_numbers = list(map(int, sys.stdin.read().split()))
    print(max_pairwise_product(input_numbers))

