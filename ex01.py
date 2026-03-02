from matrix import Vector, linear_combination

if __name__ == "__main__":
    v1 = [Vector([1,2]), Vector([2,1])]
    s1 = [2,4]
    print(linear_combination(v1, s1))
    v2 = [Vector([1,2,3]), Vector([2,1,3]), Vector([2,1,3])]
    s2 = [2,4,5]
    print(linear_combination(v2, s2))
    try:
        linear_combination(v1, s2)
    except Exception as e:
        print(e)
