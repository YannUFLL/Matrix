from matrix import Vector

def norm_vec_2d_zeros():
    v1 = Vector([0,0])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_2d_ones():
    v1 = Vector([1,1])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_2d_twos():
    v1 = Vector([2,2])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_1d_value():
    v1 = Vector([42])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_3d_mixed():
    v1 = Vector([10,2,42])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_3d_negative():
    v1 = Vector([-10,-5,-2])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_1d_small():
    v1 = Vector([0.0000001])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_1d_complex():
    v1 = Vector([3 + 4j])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

def norm_vec_2d_complex():
    v1 = Vector([3 + 4j, 2 + 6j])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

if __name__=="__main__":
    print("\ntest: norm_vec_2d_zeros")
    norm_vec_2d_zeros()
    print("\ntest: norm_vec_2d_ones")
    norm_vec_2d_ones()
    print("\ntest: norm_vec_2d_twos")
    norm_vec_2d_twos()
    print("\ntest: norm_vec_1d_value")
    norm_vec_1d_value()
    print("\ntest: norm_vec_3d_mixed")
    norm_vec_3d_mixed()
    print("\ntest: norm_vec_3d_negative")
    norm_vec_3d_negative()
    print("\ntest: norm_vec_1d_small")
    norm_vec_1d_small()
    print("\ntest: norm_vec_1d_complex")
    norm_vec_1d_complex()
    print("\ntest: norm_vec_2d_complex")
    norm_vec_2d_complex()