n = int(input().strip())

phoneBooks = {}
for i in range(0,n):
    data = input().strip().split(' ')
    if len(data) > 1:
        phoneBooks[data[0]] = data[1]

for i in range(0,n):
    name = input().strip()
    if name is not None:
        if name in phoneBooks:
            print(name+"="+phoneBooks[name])
        else:
            print('Not found')