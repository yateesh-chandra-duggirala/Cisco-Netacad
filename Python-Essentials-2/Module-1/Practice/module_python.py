# Define a variable with the name __counter.
__counter = 0

# Define a method "sum" that returns the sum of the elements of the list
def sum(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for ele in the_list:
        the_sum += ele
    return the_sum

# Define a method "product" that returns the product of the elements from the list.
def product(the_list):
    global __counter
    __counter *= 1
    prod = 1
    for ele in the_list:
        prod *= ele
    return prod

# Let us test the module here.
if __name__ == "__main__":
    print("I prefer to be a module, Let us view the tests.")
    my_list = [i+1 for i in range(5)]
    print(sum(my_list))
    print(product(my_list))