import random as rnd
import statistics as st
evaluacion1 = 'a'
evaluacion2 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
evaluacion3 = [rnd.randint(-999, 999) for i in range(1000)]

def validarLista(lista):
    if isinstance(lista, list):
        return True
    else:
        return False

def validarNumeros(lista):
    for x in lista:
        if isinstance(x, int):
            if x>=-999 and x<=999:
                pass
            else:
                return False
        else:
            return False
    return True

def Solucion(lista):
    if validarLista(lista):
        if validarNumeros(lista):
            #Agrupamiento de los elementos de la lista
            # ****************Solucion 1****************
            punto1 = st.mean(lista)

            # ****************Solucion 2****************
            punto2 = st.variance(lista)

            # ****************Solucion 3****************
            q1, q2, q3, q4 = [], [], [], []
            for i in lista:
                if i > 500:
                    q1.append(i)
                elif i > 0:
                    q2.append(i)
                elif i > -500:
                    q3.append(i)
                else:
                    q4.append(i)
            punto3 = [len(q1), len(q2), len(q3), len(q4)]
            # ****************Solucion 4****************
            prom37 = []
            for j in lista:
                if j%3 == 0 and j%7==0:
                    prom37.append(j)
            punto4 = st.mean(prom37)
            # ****************Solucion 5****************
            finparimpar = []
            for k in lista:
                x = str(k)
                x = x[-2:]
                par = [str(i) for i in range(0, 10, 2)]
                impar = [str(i) for i in range(1, 10, 2)]
                if len(x) == 2:
                    if x[0] in par or x[0] in impar and x[1] in par or x[1] in impar:
                        finparimpar.append(k)
                punto5 = len(finparimpar)
            # ****************Solucion 6****************
            punto6 = []
            p6 = [punto2]
            p6.extend(punto3)
            punto6.append(st.mean(p6))
            punto6.append(st.variance(p6))
            punto6.append(st.stdev(p6))
            # ****************Solucion 7****************
            numerosdiferentes = []
            for l in lista:
                x = str(l)
                if len(x) == 3:
                    if x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
                        numerosdiferentes.append(l)
            punto7 = len(numerosdiferentes)
            # ****************Solucion 8****************
            numerosiguales = []
            for m in lista:
                x = str(m)
                if len(x) == 3:
                    if x[0] == x[1] and x[1] == x[2]:
                        numerosiguales.append(m)
            punto8 = len(numerosiguales)
            # ****************Solucion 9****************
            datapromedio = []
            promedio = round(st.mean(lista))
            mayor = max(lista)
            menor = min(lista)
            menorb = menor*-1
            if mayor > menorb:
                mayor = mayor
            else:
                mayor = menor
            for n in lista:
                datapromedio.append(abs(promedio-n))
            idmaxmin = [min(datapromedio), max(datapromedio)]
            mascerca = datapromedio.index(idmaxmin[0])
            maslejos = datapromedio.index(idmaxmin[1])
            mcml = [mascerca, maslejos]
            punto9 = [lista[mcml[0]], lista[mcml[1]]]
        else:
            return 'Error: La lista no contiene numeros enteros entre -999 y 999'
    else:
        return 'Error: El argumento no es una lista'
    return punto1, punto2, punto3, punto4, punto5, punto6, punto7, punto8, punto9

a = Solucion(evaluacion1)
b = Solucion(evaluacion2)
c = Solucion(evaluacion3)
print('*'*100)
print('Solucion a', a)
print('*'*100)
print('Solucion a', b)
print('*'*100)
for i,j in enumerate(c, start=1):print(f'Solucion {i}: \t {j}')
for i in c:
    print(i)
