info = [eval(i) for i in input().split(" ")]
cows = [eval(i) for i in input().split(" ")]
candy = [eval(i) for i in input().split(" ")]

for i in candy:
    height = 0
    for z in range(info[0]):
        if cows[z] >= i:
            cows[z] += i - height
            break
        if cows[z] >= height:
            gain = cows[z] - height
            cows[z] += gain
            height += gain

for i in cows:
    print(i)
