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



def beneficiarios(nums: list[int]) -> None:

    #Formateo de salida.
    print("- - - - - - - - - - - - - - - - - - - - -")
    print("CASO A EVALUAR: ", nums)
    if len(nums) == 0:
        print(False," ",[])
        return
    is_possible = False

    if is_possible:
        #TODO
        #poner el print de las listas
        return(True," ",)
        pass
    else:
        print(False)
        return


def main():
    tests = list(os.scandir(ARCHIVOS_PRUEBA))
    for entry in tests :
        if entry.is_dir() or entry.is_file():
            print("==========================================")
            print("ARCHIVO: "+ ARCHIVOS_PRUEBA+"/"+entry.name)
            cases = abrir_archivo(ARCHIVOS_PRUEBA+"/"+entry.name)
            for i in cases:
                case = [int(j) for j in i]
                beneficiarios(case)

if __name__ == "__main__":
    main()
