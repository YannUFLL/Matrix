from matrix import Vector, linear_combination


def linear_combination_real_small():
    v1 = [Vector([1,2]), Vector([2,1])]
    s1 = [2,4]
    print(linear_combination(v1, s1))

def linear_combination_real_large():
    v2 = [Vector([1,2,3]), Vector([2,1,3]), Vector([2,1,3])]
    s2 = [2,4,5]
    print(linear_combination(v2, s2))

def linear_combination_complexe():
    v3 = [
        Vector([1 + 3j, 2 + 6j, 3 + 4j]),
        Vector([2 + 4j, 1 + 6j, 3 + 1j]),
        Vector([2 + 8j, 1 + 2j, 3 + 4j]),
    ]
    s3 = [2 + 3j, 1 + 0j, 5 + 2j]
    print(linear_combination(v3, s3))

def linear_combination_error():
    v1 = [Vector([1,2]), Vector([2,1])]
    s2 = [2,4,5]
    try:
        linear_combination(v1, s2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("\ntest: linear_combination_real_small")
    linear_combination_real_small()
    print("\ntest: linear_combination_real_large")
    linear_combination_real_large()
    print("\ntest: linear_combination_complexe")
    linear_combination_complexe()
    print("\ntest: linear_combination_error")
    linear_combination_error()
