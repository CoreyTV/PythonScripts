import numpy as np

MOD = 10 ** 9 + 7


def fft_multiply(poly1, poly2):
    size = 1
    while size < len(poly1) + len(poly2) - 1:
        size <<= 1

    fft1 = np.fft.fft(poly1, size)
    fft2 = np.fft.fft(poly2, size)
    result_fft = fft1 * fft2
    result = np.fft.ifft(result_fft).real.astype(int)

    return result


def calculate_coefficient(n, k):
    coefficients = [0] * (k + 1)
    coefficients[0] = 1

    for i in range(1, n + 1):
        new_coefficients = [0] * (k + 1)
        new_coefficients[0] = 1

        for j in range(1, min(i, k) + 1):
            new_coefficients[j] = (coefficients[j] + (i - j + 1) * coefficients[j - 1]) % MOD

        coefficients = new_coefficients

    result_coefficients = fft_multiply(coefficients, coefficients)

    return result_coefficients[k]


result = calculate_coefficient(10000000, 4000000)
print(result)
