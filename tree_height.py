# python3

import sys
import threading
import numpy



def compute_height(n, parents):
    # Write this function
    max_height = 0
    for i in range (0, n,1):
        current_height = 0
        value = int(parents[i])
        if value != -1:
            while (True):
                value = int(parents[value])
                if value == -1:
                    break
                current_height+=1
            
        if current_height > max_height:
            max_height = current_height

        
    # Your code here
    return max_height + 2


def main():
    input_method = input()
    print("Ievadita metode")
    if input_method == 'i':
        number_amount = int(input())
        print("Ievadits skaitlu daudzums")
        numbers = str(input())
        split_numbers = numbers.split()
        maximum = (compute_height(number_amount,split_numbers))
        print (maximum)
        # implement input form keyboard and from files
    
        # let user input file name to use, don't allow file names with letter a
        # account for github input inprecision
    
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        # call the function and output it's result
        pass
 
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
