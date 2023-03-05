# python3


import numpy



def compute_height(n, parents):
    masivs1 = []

    for i in range (n):
        masivs1.append(0)
    masivs2 = masivs1
    counter = 0



    # Write this function
    max_height = 0
    for i in range (0, n,1):

#and parents[i]!=parents[i-1]
            
        if (masivs2[i] == 0):
            counter+=1

            masivs2[i] = 1
            masivs3 = []
            masivs3.append(i)
            value = int(parents[i])

            
  
        
            while (True):
                
                masivs3.append(value)

                if value != -1:
                    
                    masivs2[value] = 1
                    value = int(parents[value])


                    for j in range (len(masivs3)):

                        masivs1[masivs3[j]] +=1

                else:
                    break
        

    print (counter , "ppp")

                
                
            
        
    max_height = max(masivs1)

        
    # Your code here
    return max_height


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
            number_amount = int(f.readline().strip())
            numbers = f.readline()
            split_numbers = numbers.split()

            maximum = (compute_height(number_amount,split_numbers))
            print (maximum)


            

 
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

main()

# print(numpy.array([1,2,3]))
