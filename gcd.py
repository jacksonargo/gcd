#!/usr/bin/env python3
#
# Outputs the GCD of two integers
# by Jackson Argo 20120819 <jargo@uga.edu>

import sys

# Lets define a format for printing out results
def print_results (a, b, c, d, e) :
    print ("(", a, ") = (", b, ")(", c, ") + (", d, ")(", e, ")", sep = '')


# Fist we'll check syntax
if (len (sys.argv) != 3) :
    print ("Usage:", sys.argv[0], "INTEGER INTEGER")
    print ("List the GCD of two integers as a combination of those two integers.")
    exit (1)

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

# Print the numbers back to the user
print ("Using", n1, "and", n2)

# Check that none of the numbers are 0
if (n1 == 0) or (n2 == 0) :
    print_results (0, 0, n1, 0, n2)
    exit (0)

# Check if n1 divides n2
if (n1 % n2 == 0) :
    gcd = abs(n2)
    print_results (gcd, 0, n1, n2//gcd, n2)
    exit (0)

# Check if n2 divides n1
if (n2 % n1 == 0) :
    gcd = abs(n1)
    print_results (gcd, n1//gcd, n1, 0, n2)
    exit (0)

# Now we'll define some more variables
a = [0, 1, 1] # We'll use this array to calculate the coefficients of the integers
x = n1 # This will be our divisor
y = n2 # This will be our dividend
q = x // y # This will be our quotient
r = x % y # This will be our remainder

# Now loop through the Euclidean Algorithm
while True :
    # Print the current step
    print ("(", x, ") = (", q, ")(", y, ") + (", r, ")", sep = '')
    print (end = ("\t"))
    print_results (r, a[2], n1, (r - (a[2] * n1)) // n2, n2)

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
print ("\nResults")
print_results (gcd, c1, n1, c2, n2)

# Check for sanity
if (gcd != ((c1 * n1) + (c2 * n2))) :
    print ("\tError! Insane results returned!")
    print ("Try using smaller numbers.")
    exit(1)

# Otherwise, exit true to operating system
else :
    exit (0)
