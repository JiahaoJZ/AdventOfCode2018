twoRep = 0
threeRep = 0
def partOne():
    with open("day2input.txt") as f:
        for line in f:
            check(line)

def check(line):
    global twoRep, threeRep
    dic = {}
    for ch in line:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    if 2 in dic.values():
        twoRep += 1
    if 3 in dic.values():
        threeRep += 1

partOne()
print("Number of elements with 2 repetitions: " + str(twoRep))
print("Number of elements with 3 repetitions: " + str(threeRep))
print("Checksum: " + str(twoRep*threeRep))

def partTwo():
    with open("day2input.txt") as f:
        text = f.read()
        aux = text.splitlines()
        aux2 = text.splitlines()
        aux2.reverse()
        counter = 0
        for line in aux:
            aux2.pop()
            for line2 in aux2:
                if hammingDistance(line,line2) == 1:
                    print("These two words have a hamming distance of one: " +
                    line + " - " + line2)
                    print("The intersection of the 2 strings are: " +
                    strIntersection(line,line2))

def hammingDistance(a,b):
    assert(len(a) == len(b))
    return sum(c1 != c2 for c1,c2 in zip(a,b))

def strIntersection(a,b):
    ans = ""
    for c1,c2 in zip(a,b):
        if c1 == c2:
            ans += c1
    return ans

print("\nHere goes the part two:")
partTwo()
