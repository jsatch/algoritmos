def merge(arr1, arr2):
    i = 0
    j = 0
    arr_resp = []
    tam = len(arr1) + len(arr2)
    for k in range(0,tam):
        if i >= len(arr1):
            arr_resp.append(arr2[j])
            j = j + 1
        elif j >= len(arr2):
            arr_resp.append(arr1[i])
            i = i + 1
        elif i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr_resp.append(arr1[i])
                i = i + 1
            else:
                arr_resp.append(arr2[j])
                j = j + 1
    return arr_resp

def order(arr):
    if len(arr) == 1:
        return arr
    else:
        tam = int(len(arr) / 2)
        arr_a = arr[:tam]
        arr_b = arr[tam:]

        return merge(order(arr_a), order(arr_b))

def main():
    arr = [1,5,3,7,8,2,4,9,6]

    print(order(arr))

if __name__ == '__main__':
    main()
