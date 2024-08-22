def regscor(uts, uas, prak, *akt):
    aktsum = 0
    for nil in akt:
        aktsum += nil
    avrakt = aktsum / len(akt)

    sum = (.3*uts)+(.35*uas)+(.3*prak)+(.05*avrakt)
    
    print(sum)


def matscor(uts, uas, prak, *akt, **matr):
    aktsum = 0
    for nil in akt:
        aktsum += nil
    avrakt = aktsum / len(akt)

    sum = (.25*uts)+(.25*uas)+(.2*prak)+(.05*avrakt)+(.25*matr['matrikulasi'])
    
    print(sum)
    

inp = input()
splinp = inp.split(", ")


if "matrikulasi" in inp:
    mat = splinp[-1]
    mat = int(mat.split("=")[1].strip())
    splinp.pop()
    splinp = [int(i) for i in splinp]
    matscor(*splinp, matrikulasi = mat)
    
else:
    splinp = [int(i) for i in splinp]
    regscor(*splinp)
