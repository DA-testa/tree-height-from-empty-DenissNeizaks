# python3




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
    
    if "I" in input_method:
        number_amount = int(input())

        numbers = str(input())

        split_numbers = numpy.array(numbers.split())
        maximum = (compute_height(number_amount,split_numbers))
        print (maximum)
        # implement input form keyboard and from files
    
        # let user input file name to use, don't allow file names with letter a
        # account for github input inprecision
    
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        # call the function and output it's result
        pass
    
    elif "F" in input_method:
        file = input()
        file = ("test/" + file)
        with open(file,'r') as f:
            number_amount = int(f.readline())
            numbers = str(f.readline())
            split_numbers = numbers.split()
            maximum = (compute_height(number_amount,split_numbers))
            print (maximum)
            
        f.close()

 
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

main()

# print(numpy.array([1,2,3]))
