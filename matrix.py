class Vector: 
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        content = " ".join(str(v) for v in self.data)
        return f"[{content}]"

    def __setitem__(self, index, value):
        self.data[index] = value

    def size(self):
        return len(self.data)
    
    def reshape(self, rows, cols):
        if rows * cols > self.size():
            raise ValueError("Dimensions incompatibles")
        new_data = []
        for i in rows:
            new_data.append(self.data[ i * cols : i * cols + cols])
        return Matrix(new_data)

    def copy(self):
        return Vector(self.data.copy())
    
    def add(self, v):
        if v.size() != self.size():
            raise ValueError("Size incompatibles")
        else:
            for i in range(v.size()):
                self.data[i] += v[i]

    def sub(self, v):
        if v.size() != self.size():
            raise ValueError("Size incompatibles")
        else:
            for i in range(v.size()):
                self.data[i] -= v[i]

    def scl(self, a):
        for i in range(self.size()):
            self.data[i] *= a

    def dot(self, v):
        if self.size() != v.size():
            return ValueError("Size incompatibles")
        res = 0
        for i in range(v.size()):
            res += self[ i] * v[i]
        return res

    def norm_1(self):
        n1 = 0
        for i in range(self.size()):
            n1 += abs(self[i])
        return n1 

    def norm(self):
        n1 = 0
        for i in range(self.size()):
            n1 += (self[i] * self[i])
        return n1 ** 0.5

    def norm_inf(self):
        n1 = 0
        for i in range(self.size()):
            n1 = max(n1, abs(self[i]))
        return n1



class Matrix:
    def __init__(self, data):
        self.data = [[x for x in row] for row in data]  

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        res = "[\n"
        for row in self.data:
            res += f"  {row}\n"
        res += "]"
        return res
    
    def shape(self):
        return (len(self.data), len(self.data[0]) if self.data else 0)

    def is_square(self):
        s = self.shape()
        return s[0] == s[1]

    def reshape(self):
        flat = []
        for row in self.data:
            flat.extend(row)
        return Vector(flat)

    def copy(self):
        new_data = [row.copy() for row in self.data]
        return Matrix(new_data)

    def add(self, m):
        if m.shape() != self.shape():
            raise ValueError("Size incompatibles")
        row, col = m.shape()
        for i in range(row):
            for j in range(col):
                self.data[i][j] += m[i][j]

    def sub(self, m):
        if m.shape() != self.shape():
            raise ValueError("Size incompatibles")

        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] -= m[i][j]

    def scl(self, a):
        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] *= a

    def mul_vec(self, vec):
        m_rows, m_cols = self.shape()
        v_rows = vec.size()
        ret = Vector([0.0] * m_rows)
        tmp = 0
        if m_cols != v_rows:
            return ValueError("The number of matrice column must be the same as vector row")
        for i in range(m_rows):
            tmp = 0
            for j in range (m_cols):
                tmp += self[i][j] * vec[j]
            ret[i] = tmp
        return ret

    def mul_mat(self, mat):
        m1_rows, m1_cols = self.shape()
        m2_rows, m2_cols = mat.shape()
        if m1_cols != m2_rows:
            raise ValueError("The number of matrice column must be the same as vector row")
        res_data = [[0.0 for _ in range(m2_cols)] for _ in range(m1_rows)]
        tmp = 0
        for i in range(m1_rows):
            for j in range (m2_cols):
                tmp = 0
                for k in range (m2_rows):
                    tmp += self[i][k] * mat[k][j]
                res_data[i][j] = tmp
        return Matrix(res_data)

    def trace(self):
        m_rows, m_cols = self.shape()
        if (m_rows != m_cols): 
            raise ValueError("Can't compute trace with no square Matrix")
        t = 0
        for i in range(m_rows):
            t += self[i][i]
        return (t)

    def transpose(self):
        m_rows, m_cols = self.shape()
        r = Matrix([[0.0 for _ in range(m_rows)] for _ in range(m_cols)])
        for i in range(m_rows):
            for j in range(m_cols):
                r[j][i] = self[i][j]
        return (r)

    def row_echelon(self):
        m_rows, m_cols = self.shape()
        r = Matrix([[self[i][j] for j in range(m_cols)] for i in range(m_rows)])
        # step find wich line to swap
        for i in range(m_rows):
            tmp = 0 
            line_to_swap = i
            # step 1 find the pivot
            for j in range(i, m_rows):
                if abs(r[j][i]) > tmp and r[j][i] != 0:
                    tmp = abs(r[j][i])
                    line_to_swap = j
            # step 2 swap line
            tmp = r[i]
            r.data[i] = r.data[line_to_swap]
            r.data[line_to_swap] = tmp
            # step 3 : elimination of the others unknow of the same var
            for j in range(i + 1, m_rows):
                if r[i][i] == 0:
                    continue
                factor = r[j][i] / r[i][i] 
                # factorisation of the line
                # elimination of x 
                for k in range(i, m_cols):
                    r[j][k] -= (r[i][k] * factor)
        return(r)


    def determinant(self):
        m_rows, m_cols = self.shape()
        if m_rows != m_cols:
            return (ValueError("Matrix must be square to compute determinant"))
        if m_rows > 4:
            return (ValueError("Determinant for matrices larger than 4x4 is not implemented."))
        if m_rows == 1:
            return self[0][0]
        # Cramer rule
        if m_rows == 2: 
            return ((self[0][0] * self[1][1]) - (self[0][1] * self[1][0]))
        # Saru rule
        if m_rows == 3:
            return (((self[0][0] * self[1][1] * self[2][2]) 
                    + (self[0][1] * self[1][2] * self[2][0])
                    + (self[0][2] * self[1][0] * self[2][1])) - 
                    + (self[0][2] * self[1][1] * self[2][0])
                    + (self[0][0] * self[1][2] * self[2][1])
                    + (self[0][1] * self[1][0] * self[2][1]))
        # Gauss method
        if m_rows == 4:
            m_ech = self.row_echelon()
            return  (m_ech[0][0] * m_ech[1][1] * m_ech[2][2] * m_ech[3][3])

           



            

          

def linear_combination(u : list[Vector], coefs : list):
    if len(u) != len(coefs):
        raise ValueError("Size incompatibles")

    v_size = u[0].size()
    new_vector = Vector([0.0] * v_size)

    for i in range(len(u)):
        temp = Vector(u[i].data.copy())
        temp.scl(coefs[i])
        new_vector.add(temp)

    return new_vector

def lerp(u, v, t):
    if isinstance(u , Vector) or isinstance(u, Matrix):
        res = u.copy()
        res.scl(1-t)
        temp = v.copy()
        temp.scl(t)
        res.add(temp)
        return (res)
    else:
        return (u * (1 - t) + v * t)

def angle_cos(u,v):
    if u.size() != v.size():
        return ValueError("Size incompatibles")
    return (u.dot(v) / (u.norm() * v.norm()))

def cross_product(u, v):
    x = u[1] * v[2] - u[2] * v[1]
    y = - (u[0] *  v[2]- u[2] *v[0])  
    z =  u[0] * v[1]- u[1] * v[0]
    return Vector([x,y,z])

    

    

        




