arr0 = '-1 1 -1 0 0 0'.split(' ')
arr1 = '0 -1 0 0 0 0'.split(' ')
arr2 = '-1 -1 -1 0 0 0'.split(' ')
arr3 = '0 -9 2 -4 -4 0'.split(' ')
arr4 = '-7 0 0 -2 0 0'.split(' ')
arr5 = '0 0 -1 -2 -4 0'.split(' ')

arr = [arr0, arr1, arr2, arr3, arr4, arr5]
def get_sum_hg(x,y,arr):
    hg = []
    try:
        hg.append(int(arr[x][y]))
        hg.append(int(arr[x][y+1]))
        hg.append(int(arr[x][y+2]))
        hg.append(int(arr[x+1][y+1]))
        hg.append(int(arr[x+2][y]))
        hg.append(int(arr[x+2][y+1]))
        hg.append(int(arr[x+2][y+2]))
    except:
        return False
    return sum(hg)

max = None
for x in range(len(arr)):
    for y in range(len(arr)):
        sum_hg = get_sum_hg(x, y, arr)
        if sum_hg is not False and (max is None or sum_hg > max):
            max = sum_hg

print(max)