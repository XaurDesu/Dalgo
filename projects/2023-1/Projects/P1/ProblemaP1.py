import sys

def abrir_archivo(file: str) -> list:
    content = open(file, "r")
    content = content.readlines()
    ret = []
    for i in content:
        i = i.replace('\n', "")
        i = list(i.split(" "))
        if '' in i:
            i.remove('')
        ret.append(i)
    return ret[1:]


def beneficiarios(k:int, m: int, nums: list[int]):
    """
    
    Uno de los principales retos de la reforma a la salud 2023 propuesta por el gobierno actual son los
    denominados Centros de Atención Primaria (CAD). A cada CAD en el país serán asignados los
    beneficiarios y sus familias según cercanía y disponibilidad. Para que las finanzas de estos centros
    no se vean afectadas por una mala distribución de beneficiarios y para garantizar el mejor servicio,
    es necesario diseñar una estrategia de asignación equitativa de beneficiarios.
    
    ---------------------------

    Asumimos por el enunciado que: 

    2 <= k <= 3
    2 <= m <= 10**4
    1 <= fi <= 50
    
    """

    selected = [False]*m

    def backtracker(i: int, k: int, subset: int):
        """
        Implementacion anidada del backtracking, hacerlo así nos 
        debería permitir hacer menor el tiempo de ejecucion (NO la complejidad)
        y permitirnos pasar mas facilmente valores por referencia (véase el
        uso de un 'selected' no local)
        """
        
        #Passes selected list
        nonlocal selected
        nonlocal ret
        if k == 0:
            return True
        if sum(ret[subset]) == target_sum:
            return backtracker(0, k-1, subset+1)
        for j in range(i, len(nums)):
            if selected[j] == True or sum(ret[subset]) + nums[j] > target_sum:
                continue
            selected[j] = True
            ret[subset].append(nums[j])
            if backtracker(j+1, k, subset):
                return True
            selected[j] = False
            ret[subset].remove(nums[j])
        return False
    sum_nums = sum(nums)
    
    target_sum = sum_nums / k

    #Revisa si es un entero o decimal, si es decimal ya sabemos que no es posible.
    if target_sum != int(target_sum):
        return False

    ret = []
    for i in range(k):
        ret.append([])

    is_possible = backtracker(0, k, 0)
    
    if is_possible:
        print(is_possible, [tuple(i) for i in ret])
    else:
        print(False)


def main():
    filename = sys.argv[-1]
    cases = abrir_archivo(filename)
    for i in cases:
        case = [int(j) for j in i]
        beneficiarios(case[0],case[1],case[2:])
    pass

if __name__ == "__main__":
    main()