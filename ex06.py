from matrix import Vector, cross_product


def cross_product_test():
    v1 = Vector([0,2,0])
    v2 = Vector([2,0,0])
    print(cross_product(v1, v2))

    # two colinear vector
    v1 = Vector([1,2,3])
    v2 = Vector([2,4,6])
    print(cross_product(v1, v2))
    
    # anti commutativity test
    v1 = Vector([1,2,3])
    v2 = Vector([2,4,6])
    print(cross_product(v1, v2))
    print(cross_product(v2, v1))

    v1 = Vector([1,2,3])
    v2 = Vector([4,5,6])
    print(cross_product(v1, v2))


    v1 = Vector([18,-14,2])
    v2 = Vector([32,7,51])
    print(cross_product(v1, v2))

if __name__ == "__main__":
    cross_product_test()
