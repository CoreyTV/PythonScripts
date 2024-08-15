def have_same_digits(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

x = 1000

while True:
    if all(have_same_digits(x, i * x) for i in range(2, 7)):
        print("Smallest positive integer:", x)
        break
    x += 1
