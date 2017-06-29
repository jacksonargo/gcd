#!/usr/bin/env python3
#
# Outputs the GCD of two integers
# by Jackson Argo 20120819 <jargo@uga.edu>
def gcd(n1, n2):
    reply = ''
    # Lets define a format for printing out results
    def print_results(a, b, c, d, e) :
        return "(%d) = (%d)(%d) + (%d)(%d)\n" % (a, b, c, d, e)
    
    # Print the numbers back to the user
    reply += "Using %d and %d\n" % (n1, n2)
    
    # Check that none of the numbers are 0
    if (n1 == 0) or (n2 == 0) :
        reply += print_results(0, 0, n1, 0, n2)
        return reply
    
    # Check if n1 divides n2
    if (n1 % n2 == 0) :
        gcd = abs(n2)
        reply += print_results(gcd, 0, n1, n2//gcd, n2)
        return reply
    
    # Check if n2 divides n1
    if (n2 % n1 == 0) :
        gcd = abs(n1)
        reply += print_results(gcd, n1//gcd, n1, 0, n2)
        return reply
    
    # Now we'll define some more variables
    a = [0, 1, 1] # We'll use this array to calculate the coefficients of the integers
    x = n1 # This will be our divisor
    y = n2 # This will be our dividend
    q = x // y # This will be our quotient
    r = x % y # This will be our remainder
    
    # Now loop through the Euclidean Algorithm
    while True :
        # Print the current step
        reply += "(%d) = (%d)(%d) + (%d)\n\t" % (x, q, y, r)
        reply += print_results(r, a[2], n1, (r - (a[2] * n1)) // n2, n2)
    
        # Check for sane results
        if (r != a[2] * n1 + ((r - (a[2] * n1)) // n2) * n2) :
            print ("\tError! Insane results returned!")
    
        # Apply another step of the algorithm
        x = y
        y = r
        r = x % y
    
        # If r is 0, the algorithm is finished
        if (r == 0) :
            gcd = y
            break
    
        # Otherwise, we need to keep track of the coefficients
        else :
            q = x // y;
            a[2] = a[0] - q * a[1]
    
            # Now we'll move everything down and start again
            a[0] = a[1]
            a[1] = a[2]
    
    # Now let's calculate the coefficients
    c1 = a[2]
    c2 = ((gcd - (c1 * n1)) // n2)
    
    # Check if the GCD is negative,
    if (gcd < 0) :
        gcd *= -1
        c1 *= -1
        c2 *= -1
    
    # Print the results to the user
    reply += "\nResults"
    reply += print_results(gcd, c1, n1, c2, n2)
    
    # Check for sanity
    if (gcd != ((c1 * n1) + (c2 * n2))) :
        print ("\tError! Insane results returned!")
        print ("Try using smaller numbers.")
    return reply
