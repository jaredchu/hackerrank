n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

m_sum = 0
for i in range(n):
    m_sum += (a[i] * b[i])
print("{0:.1f}".format(m_sum/sum(b)))