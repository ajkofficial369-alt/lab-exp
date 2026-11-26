# Function to generate Fibonacci series

def fibonacci(n):
    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# Main program

n = int(input("Enter the number of terms for Fibonacci series: "))

series = fibonacci(n)

print("Fibonacci series up to", n, "terms:")
print(series)
