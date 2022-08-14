m = 2
c = 5
x_values = list(range(1, 9))

# y_values = [m * x + c for x in x_values if x%2 == 0]
results = [(x, m * x + c) for x in x_values if x%2 == 0]
print(results)
# [(2, 9), (4, 13), (6, 17), (8, 21)]

m = 2
c1 = 5   # for all odd
c2 = 10   # for all even
x_values = list(range(1, 9))

results = [(x, m * x + (c2 if x%2==0 else c1)) for x in x_values]
print(results)
# [(1, 7), (2, 14), (3, 11), (4, 18), (5, 15), (6, 22), (7, 19), (8, 26)]