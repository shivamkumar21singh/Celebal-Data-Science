def lower_triangular(n):
    for i in range(1, n + 1):
        print('* ' * i)

def upper_triangular(n):
    for i in range(n, 0, -1):
        print('  ' * (n - i) + '* ' * i)

def pyramid(n):
    for i in range(1, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

n=int(input("Enter the number of lines a pattern should contain: "))
print("Lower Triangular Matrix:")
lower_triangular(n)
print("\nUpper Triangular Matrix:")
upper_triangular(n)
print("\nPyramid:")
pyramid(n)