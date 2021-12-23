m_1 = [[2, 3], [4, 2], [5, 7]]
m_2 = [[3, 1], [9, 2], [3, 8]]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '{0[0]}\n{0[1]}\n{0[2]}'.format(self.matrix)
        # return '{0[0][0]} {0[0][1]}\n{0[1][0]} {0[1][1]}'.format(self.matrix)

    def __add__(self, other):
        """  Честно, подсмотрел реализацию в разборе дз, но зато разобрался в данной реализации и глубже
        понял работу цикла for и фунций range и len в нем.
        """
        list_r = []
        for i in range(len(self.matrix)):
            list_r.append([])  # Вот это не понял до конца, видимо подставляется результат из след. цикла?
            for j in range(len(self.matrix[0])):
                list_r[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(list_r)
        # return '\n'.join(map(str, list_r))


mtrx_1 = Matrix(m_1)
mtrx_1_str = str(mtrx_1)
print(mtrx_1_str)
mtrx_2 = Matrix(m_2)
print()
print(mtrx_1 + mtrx_2 + mtrx_1)