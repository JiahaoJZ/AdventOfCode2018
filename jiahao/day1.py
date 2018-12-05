def partOne():
    with open("day1input.txt") as f:
        ans = sum(int(x) for x in f)
        print("El desplazamiento total es: " + str(ans))

numbers = {0}
ans = 0

def partTwo():
    with open("day1input.txt") as f:
        text = f.read()
        found = 0
        while found is 0:
            found = iteration(text)

def iteration(file):
    global ans
    for i in file.splitlines():
        ans += int(i)
        if ans in numbers:
            print("\nParte dos..")
            print("El primer valor repetido es: " + str(ans))
            return 1
        numbers.add(ans)
    return 0

partOne()
partTwo()
