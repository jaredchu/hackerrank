def diff(a, b):
    x = a.copy()
    y = b.copy()
    for i in x:
        if i in y:
            y.remove(i)
    return y

def ransom_note(magazine, ransom):
    return len(diff(magazine,ransom)) == 0

def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False