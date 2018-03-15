def getBy(list,even=True):
    newList = []
    for i in range(len(list)):
        if even and i%2 == 0:
            newList.append(list[i])
        elif not even and i%2 != 0:
            newList.append(list[i])
    return newList

number = int(input().strip())
for i in range(number):
    list = input().strip()
    print(''.join(getBy(list)) + ' ' + ''.join(getBy(list, False)))




