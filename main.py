def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    # Base Case:
    if n <= 1:
        return n
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    # if nth fibonaci value in fibs, search it up
    if fibs[n] != -1:
        return fibs[n]
    # Base Case:
    if n <= 1:
        result = n
    else:
        result = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    # Save result in fibs
    fibs[n] = result
    # Return result
    return result



def fib_bottom_up(n):
    # Base Case:
    if n < 2:
        return n

    # Create list of fibonaci value
    fibs =[-1]*(n+1)

    # Initialize base case values
    fibs[0] = 0
    fibs[1] = 1
    # loop through fibonaci values starting from the n=2 one, n=1 and n=0 are accounted for
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    # return the final value and print final fib table
    print(fibs)
    return fibs[n]




