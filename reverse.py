def reverse(string):
    '''reverse a string with recursion'''
    if string == '':
        return ''
    else:
        firstSymbol = string[0]
        return reverse(string[1:]) + firstSymbol

print(reverse('hello world!'))
print(reverse('spam'))
print(reverse('Willie wil vir Sannie Raps'))
print(reverse('Sannie soek vir tannie Babs'))