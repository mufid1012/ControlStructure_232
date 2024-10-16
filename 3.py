n = int(input("Masukan nilai n untuk deret Fibonacci "))

a, b = 0, 1
print(f"Berikut adalah deret Fibonacci hingga {n}:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b