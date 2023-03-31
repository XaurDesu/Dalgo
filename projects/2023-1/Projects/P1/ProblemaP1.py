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

def beneficiarios(k:int, i: int, nums: list[int]) -> None:

    #Formateo de salida.
    print("- - - - - - - - - - - - - - - - - - - - -")
    print("CASO A EVALUAR: ", nums)
    print("k =",k)
    print("i =",i)
    
    is_possible = False
    subs = []
    for position in range(k):
        subs.append([0]*i)
    

    print(subs)


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
