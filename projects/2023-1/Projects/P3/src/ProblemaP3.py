import sys
from itertools import combinations

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
    return ret

#Problema detectado: vertex cover
def solve(n, m, caso):

    politician_graph = {}
    citizen_graph = {}
    #generación primer grafo
    for i in range(n):
        citizen_graph[i+1] = caso[i]
    
    #generación segundo grafo.
    for i in range(1, m+1):
        citizens_into = []
        for j in range(1, n+1):
            check = citizen_graph[j]
            if i in check:
                citizens_into.append(j)
        politician_graph[i] = citizens_into

    i = 1
    while i < m:
        comb = combinations(politician_graph.keys(), i)
        for j in comb:
            voteset = []
            for k in j:
                voteset.extend(politician_graph[k])
            if len(set(voteset)) == n:
                return j
        i += 1


def main():
    filename = sys.argv[-1]
    data = abrir_archivo(filename)
    num_casos = int(data[0][0])
    
    
    i = 1
    while num_casos > 0:
        n = int(data[i][0])
        m = int(data[i][1])
        caso = [data[j] for j in range(i+1, i+n+1)]

        for k in range(len(caso)):
            caso[k] = [int(j) for j in caso[k]]

        solution = solve(n,m,caso)
        ret = ""
        for k in solution:
            ret += str(k)+" "
        print(ret)

        i += n+1
        num_casos -= 1
    
    
    
    

if __name__ == "__main__":
    main()