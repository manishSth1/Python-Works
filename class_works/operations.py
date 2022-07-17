a1 = 5 + 6  # integer and integer
a2 = 5.5 + 2.3  # float and float
a3 = 4.7 + 2  # integer and float
a4 = "Hello " + "world"  # string and string
a5 = (5 + 4j) + (6 + 5j)  # complex and complexc

print(a1, a2, a3, a4, a5, sep = '\n')



b1 = 5 - 6  # integer and integer
b2 = 5.5 - 2.3  # float and float
b3 = 4.7 - 2  # integer and float
# b4 = "Hello " - "world"  # string subtraction not supported
b5 = (5 + 4j) - (6 + 5j)  # complex and complex

print(b1, b2, b3, b5, sep = '\n')


c1 = 5 * 6  # integer and integer
c2 = 5.5 * 2.3  # float and float
c3 = 4.7 * 2  # integer and float
c4 = "Hello " * 5  # string and int
c5 = (5 + 4j) * (6 + 5j)  # complex and complex

print(c1, c2, c3, c4, c5, sep='\n')

d1 = 5 / 6  # integer and integer
d2 = 5.5 / 2.3  # float and float
d3 = 4.7 / 2  # integer and float
d4 = (5 + 4j) / (6 + 5j)  # complex and complex

print(d1, d2, d3, d4, sep='\n')

#%%
paper_width = 30
print('-' * paper_width)
print(' ABC Mart'.center(paper_width))
print('='* paper_width)
print('1 chocolate $10')
print('1 chocolate $10')
print('1 chocolate $10')
print('-' * paper_width)

print('Thank you, ', end ='')
print('Visit us again.')
print('-' * paper_width)
#%%