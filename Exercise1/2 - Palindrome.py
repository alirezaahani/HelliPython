'''
    Since We operate on a list of digits, there is no need to convert to integer
'''

number = input()


'''
    [::-1] Reverses the number

    if the reverse of a number equals itself, them it is palindrome
'''
if number == number[::-1]:
    print("YES")
else:
    print("NO")
