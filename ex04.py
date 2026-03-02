from matrix import Vector

def norm():
    v1 = Vector([0,0])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([1,1])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([2,2])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([42])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([10,2,42])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([-10,-5,-2])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")
    v1 = Vector([0.0000001])
    print(f"l1: {v1.norm_1()} l2: {v1.norm()} l_inf: {v1.norm_inf()}")

if __name__=="__main__":
    norm()