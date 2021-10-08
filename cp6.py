try:
    n = int(input('введите количество элементов массива: '))
except ValueError:
    print('проверка на дурака не пройдена, попробуйте в другой раз =)')
else:
    array = [0]*n
    try:
        for i in range(0,n):
            array[i] = int(input('введите элемент: '))
    except ValueError:
        print('проверка на дурака не пройдена, попробуйте в другой раз =)')
    else:
        try:
            delta = int(input('введите delta: '))
        except ValueError:
            print('проверка на дурака не пройдена, попробуйте в другой раз =)')
        else:
            result1 = array.count(min(array) + delta)
            result2 = array.count(min(array) - delta)
            print(result1+result2) 
