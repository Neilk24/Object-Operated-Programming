class PairElement:

    def two_sum(self, num, target):
        lookup = {}
        for i, n in enumerate(num, start = 1):
            if target - n in lookup:
                return lookup[target-n], i
            lookup[n] = i

value = int(input('Enter a value: '))

print('index1 = %d, index2 = %d', PairElement().two_sum((10,20,30,40,50,60,70), value))