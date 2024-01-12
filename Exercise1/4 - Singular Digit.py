n = int(input())

while n > 9:


    '''
        First converts the number to a string using `str` function
        Then converts the string to array of characters (there is no need for a function python does that automatically)
        Then converts the array of characters to an array of integers where each element is one digit using the `map` function.
        Then sums all the integers using the `sum` function
    '''
    n = sum(map(int, str(n)))

print(n)
