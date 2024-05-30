'''Greatest Common Divisor (GCD)
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder. For example, the GCD of 8 and 12 is 4, because 4 is the largest number that can divide both 8 and 12 exactly.

Least Common Multiple (LCM)
The Least Common Multiple (LCM) of two integers is the smallest positive integer that is evenly divisible by both numbers. For example, the LCM of 4 and 5 is 20, because 20 is the smallest number that both 4 and 5 can divide into without leaving a remainder.'''

'''Steps of the Euclidean Algorithm
Start with two numbers, a and b.
Compute the remainder of a divided by b.
Replace a with b and b with the remainder.
Repeat the process until b becomes zero.
When b is zero, a contains the GCD.'''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

#Example usage
a,b=map(int,input().split())
gcd_value=gcd(a,b)
lcm_value=lcm(a,b)
print(gcd_value)
print(lcm_value)    
