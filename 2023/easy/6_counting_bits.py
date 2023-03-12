def countBits(n) :
    counter = [0]
    for i in range(1, n+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter


n = 2
print(countBits(n))

n = 5
print(countBits(n))