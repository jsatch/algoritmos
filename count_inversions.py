'''
Algoritmo para contar el numero de inversiones dado un arreglo de numeros
enteros (https://www.geeksforgeeks.org/counting-inversions/).

Se utiliza el metodo divide and conquer para pasar de una complejidad O(n2)
a una complejidad O(nlogn).

Util para calcular similitudes entre arreglos para filtrado colaborativo.
'''
def contar(arr):
    if len(arr) == 1:
        return arr,0
    else:
        arr_izq, cant_izq = contar(arr[:int(len(arr)/2)])
        arr_der, cant_der = contar(arr[int(len(arr)/2):])
        arr_ordenado, cant_inv = contar_ordenar(arr_izq, arr_der)
        return arr_ordenado, cant_izq + cant_der + cant_inv

def contar_ordenar(arr_izq, arr_der):
    i = 0
    j = 0
    arr_resp = []
    count_inv = 0
    for k in range(len(arr_izq) + len(arr_der)):
        if i >= len(arr_izq):
            arr_resp = arr_resp + arr_der[j:]
            break
        elif j >= len(arr_der):
            arr_resp = arr_resp + arr_izq[i:]
            break
        elif arr_izq[i] < arr_der[j]:
            arr_resp.append(arr_izq[i])
            i = i + 1
        elif arr_izq[i] >= arr_der[j]:
            arr_resp.append(arr_der[j])
            j = j + 1
            count_inv = count_inv + len(arr_izq) - i
    return arr_resp, count_inv

def main():
    #arr = [1, 3 ,5 , 2, 4 , 6]
    arr = [1,5,3,7,8,2,4,9,6]
    print(contar(arr))

if __name__ == '__main__':
    main()
