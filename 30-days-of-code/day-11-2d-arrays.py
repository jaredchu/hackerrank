arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

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