p = int(input('Enter the principal amount = '))
r = int(input('Enter the rate of interest per annum = '))
y = int(input('Enter the number of years = '))
c = int(input('Enter conversion period per year = '))

i = (r/100)/c
n = (y*c)

ci = p*(((1+i)**n)-1)
print('Compound Interest = ')
print(ci)
