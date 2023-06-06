# Uses python3
#Time Complexity O(n log n)
#Item Value DataClass
import sys
class Item():
     def __init__(self, weights, values, index):
            self.weights = weights
            self.values = values
            self.ratio = values/weights
            self.index = index

     def __lt__(self, other):
            return self.ratio < other.ratio

# Greedy Approach
def get_optimal_value(capacity, weights, values):
    value = 0
    
    #function to get maximum value
    items = [];
    for i in range(len(weights)):
         items.append(Item(weights[i], values[i], i))

    # sorting items by value
    items.sort(reverse=True)

    for i in items:
          currWt = int(i.weights)
          currVal = int(i.values)
          if capacity - currWt >= 0:
                capacity -= currWt
                value += currVal
          else:
                fr = capacity / currWt
                value += currVal * fr
                capacity = int(capacity - (currWt * fr))
                break

    return value;

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
