#using python3
import sys
def compute_min_refills(distance, tank, stops):
    refills = 0;
    position = 0;
    newPosition = 0;
    fuel = tank;
    
    if(distance <= fuel):
        return 0;
    
    while(position < len(stops)):
        fuel -= (stops[position] - newPosition); 
                      
        if(fuel >= stops[position] - newPosition):           
            newPosition = stops[position];
        else: 
            fuel = tank;
            if(fuel >= stops[position] - newPosition):
               newPosition = stops[position];
            else:
                return -1;
            refills += 1;        
        position +=1;        

    if (fuel < distance - newPosition): 
        fuel = tank;
        refills += 1;
        if(fuel >= distance - newPosition):
            newPosition = distance;
        else:
            return -1;      
    
    return refills

if __name__ == '__main__':
    d, m, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
