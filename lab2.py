def is_palindrome(value):
    return value == str(value)[::-1]


def check(ran, sol):
    for value in range(100000, 999999):
        if(is_palindrome(str(value)[ran[0][0]:ran[0][1]]) and
                is_palindrome(str(value + 1)[ran[1][0]:ran[1][1]]) and
                is_palindrome(str(value + 2)[ran[2][0]:ran[2][1]]) and
                is_palindrome(str(value + 3)[ran[3][0]:ran[3][1]])):
            sol.append([value, value + 1, value+2, value + 3])


ran = [[2, 6], [1, 6], [1, 5], [0, 6]]
sol = []


check(ran,sol)


print ("Liczby bez formatowania: ")
print sol

print ("Liczby po sformatowaniu: ")
for pal in sol:
    final = '{0} : (+1) {1}  (+2) {2}   (+3) {3}'.format(pal[0], pal[1], pal[2], pal[3])
    print final


