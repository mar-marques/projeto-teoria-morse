
#Considere K um complexo simplicial e f uma função de Morse discreta tal que f: K -> R. Este algoritmo irá gerar o campo gradiente em K induzido por f.

K = ("1", "2", "3", "4", "5", "3 5", "1 2", "2 3", "3 4", "1 4", "1 3","1 2 3")

f = (["1",3], ["2",8], ["3", 5.1], ["4", 0], ["5", 8], ["3 5", 7],["1 2", 11], 
["2 3", 6], ["3 4",4],["1 4",2],["1 3",7], ["1 2 3", 10])

A = []
B = []
C = []

def EncontrarFaces(simplexo):
    faces = []
    simplexo = simplexo.split()
    if len(simplexo) > 1:
        for c in range(len(simplexo)):
            if c < 2:
                soma = simplexo[c]
                soma = Concatenar(soma, simplexo, c + 1, len(simplexo) - 1 + c)
            else:
                soma = simplexo[0]
                soma = Concatenar(soma, simplexo, 1, c - 1)
                soma = Concatenar(soma, simplexo, c, len(simplexo))
            faces.append(soma)
    return faces


def Concatenar(cont, simplexo,a,b):
    for x in range(a, b):
        cont = cont +" "+ simplexo[x]
    return cont


def EncontrarCofaces(simplexo):
    cofaces = []
    for h in K:
        if simplexo in EncontrarFaces(h):
            cofaces.append(h)
    return cofaces

def Encontrarvalor(simplexo):
    for par in f:
        if simplexo in par:
            return par[1]
           
def alocar():
    for simplexo in K:
        flag = True
        valorsim = Encontrarvalor(simplexo)
        faces = EncontrarFaces(simplexo)
        cofaces = EncontrarCofaces(simplexo)
        for face in faces:
            if Encontrarvalor(face) >= valorsim:
                flag = False
                A.append(face)
                B.append(simplexo)
        if flag:
            for coface in cofaces:
                if Encontrarvalor(coface) <= valorsim:
                    flag = False

            if flag:
                C.append(simplexo)

alocar()

print("A: ",A)
print("B: ",B)
print("C: ",C)
