num = int(input())

for i in range(1, num+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A, "+", B, "=", A+B)