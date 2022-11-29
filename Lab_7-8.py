#author NDO 11/28/22

# create 2 separate functions within the same document 
def find_sum(num1,num2) :
    '''Finds the sum of two numbers'''
    num_sum = num1 + num2 
    return(num_sum)

def div2_sum(option1, option2):
    '''Divides the result by two'''
    new_sum = find_sum(option1, option2)
    div_sum = new_sum // 2 
    return(div_sum)
#create a 3rd function which requires both the first two functions 
def square_sum(var1,var2):
    ''' Squares the result of the two previous funcitons'''
    square = div2_sum(var1,var2)
    square_var = square ** 2 
    return (square_var)

# create 4 test cases for the 3rd function 
print(square_sum(10,30) == 400)
print(square_sum(50,100) == 5625)
print(square_sum(2,6) == 16)
print(square_sum(42,58) == 2500)
