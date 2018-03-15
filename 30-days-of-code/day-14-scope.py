class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        max_diff = 0
        for elm in self.__elements:
            for elm1 in self.__elements:
                diff = abs(elm - elm1)
                if diff > max_diff:
                    max_diff = diff
        self.maximumDifference = max_diff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)