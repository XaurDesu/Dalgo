
def cortar_matrix(mat: list[list]):
    mitad = len(mat) // 2

    top_right = [[mat[i][j] for j in range(mitad, len(mat))] for i in range(mitad)]
    bot_right = [
        [mat[i][j] for j in range(mitad, len(mat))] for i in range(mitad, len(mat))
    ]

    top_left = [[mat[i][j] for j in range(mitad)] for i in range(mitad)]
    bot_left = [[mat[i][j] for j in range(mitad)] for i in range(mitad, len(mat))]

    return top_left, top_right, bot_left, bot_right


def resta_matrix(mat_a: list[list], mat_b: list[list]):
    return [
        [mat_a[lin][col] - mat_b[lin][col] for col in range(len(mat_a[lin]))]
        for lin in range(len(mat_a))
    ]

def suma_matrix(mat_a: list[list], mat_b: list[list]):
    return [
        [mat_a[lin][col] + mat_b[lin][col] for col in range(len(mat_a[lin]))]
        for lin in range(len(mat_a))
    ]

def strassen_matrix_mult(mat_a:list[list[int]],mat_b:list[list[int]]):
    tamano_mat = (len(mat_a),len(mat_a[0]))
    if tamano_mat == (2,2):
        #eventualmente una matriz cuadrada llegará acá, puras operaciones que son rápidas en un computador.
        return [
        [mat_a[0][0] * mat_b[0][0] + mat_a[0][1] * mat_b[1][0], mat_a[0][0] * mat_b[0][1] + mat_a[0][1] * mat_b[1][1]],
        [mat_a[1][0] * mat_b[0][0] + mat_a[1][1] * mat_b[1][0], mat_a[1][0] * mat_b[0][1] + mat_a[1][1] * mat_b[1][1]],
        ]
    
    """
    Dividir acá las matrices nos permitirá hacer O(N/2) operaciones, lo cual sale mas barato
    que multiplicar una matriz directamente. por lo que podremos llegar a una velocidad logaritmica
    en soluciones infinitesimalmente grandes.
    """    
    
    a, b, c, d = cortar_matrix(mat_a)
    e, f, g, h = cortar_matrix(mat_b)

    #llamamos a recurrencia en las submatrices, es decir, en esta solución, la propia
    #función principal es la ecuación que llama recurrencia.
    t1 = strassen_matrix_mult(a, resta_matrix(f,h))
    t2 = strassen_matrix_mult(suma_matrix(a,b),h)
    t3 = strassen_matrix_mult(suma_matrix(c,d),e)
    t4 = strassen_matrix_mult(d, resta_matrix(g,e))
    t5 = strassen_matrix_mult(suma_matrix(a,d),suma_matrix(e,h))
    t6 = strassen_matrix_mult(resta_matrix(b,d),suma_matrix(g,h))
    t7 = strassen_matrix_mult(resta_matrix(a,c),suma_matrix(e,f))

    #
    top_left = suma_matrix(resta_matrix(resta_matrix(t5, t4), t2), t6)
    top_right = suma_matrix(t1, t2)
    bot_left = suma_matrix(t3, t4)
    bot_right = resta_matrix(resta_matrix(suma_matrix(t1, t5), t3), t7)

    ret = []
    for i in range(len(top_right)):
        ret.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        ret.append(bot_left[i] + bot_right[i])

    return ret