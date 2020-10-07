#eating_cookies/eating_cookies.py



'''
Input: an integer
Returns: an integer
'''
def fib3(n):
    # Fibonacci-3 Calculator
    a, b, c = 1, 1, 2
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


def eating_cookies(n, *args):
    # W(n) = W(n - 1) + W(n - 2) + W(n - 3)
    return fib3(n)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    #num_cookies = 5
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
