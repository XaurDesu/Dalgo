from functools import lru_cache
import os

ARCHIVOS_PRUEBA = "projects/2023-1/Projects/P1/tests"

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

soluciones = {}

"""
SOLUCION CON SOLO 2 SUBLISTAS (Vease Documento):
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]
"""



def beneficiarios(k:int, i: int, nums: list[int]) -> None:

    #Formateo de salida.
    print("- - - - - - - - - - - - - - - - - - - - -")
    print("CASO A EVALUAR: ", nums)
    print("k =",k)
    print("i =",i)

    subseq = []
    for num in range(k):
        subseq.append([0]*i)

    ret = []
    
    sum_nums = sum(nums)
    # 0 es siempre posible
    

    #Checks if this is a Decimal or an Integer.
    target_sum = sum_nums / k
    if target_sum != int(target_sum):
        return False

    def solve_two():
        dp = [[True, True]] + [[False,False]]*sum_nums
        

    def solve_three():
        pass
    
    if k == 2:
        solve_two()
    if k == 3:
        solve_three()


    print(subseq)
    print(target_sum)



def main():
    tests = list(os.scandir(ARCHIVOS_PRUEBA))
    for entry in tests :
        if entry.is_dir() or entry.is_file():
            print("==========================================")
            print("ARCHIVO: "+ ARCHIVOS_PRUEBA+"/"+entry.name)
            cases = abrir_archivo(ARCHIVOS_PRUEBA+"/"+entry.name)
            for i in cases:
                case = [int(j) for j in i]
                beneficiarios(case[0],case[1],case[2:])

if __name__ == "__main__":
    main()
