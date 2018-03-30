from collections import defaultdict

N = int(input().strip())
database = defaultdict(list)
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    database[firstName].append(emailID)

for name in sorted(database.keys()):
    for email in database[name]:
        if email.endswith('@gmail.com'):
            print(name)
