def rCn(r, n):
    if n==0:
        return 1
    else:
        return rCn(r, n - 1) * (r - n + 1) // n
	
height = 4
for h in range(1,height+1):
    c = [[rCn(r, n) for n in range(r + 1)] for r in range(h)]
    print('第',h,'列巴斯卡三角形的求值過程')
    print('=============================')
    for r in range(len(c)):
        print(("%" + str((len(c) - r) * 3) + "s") % "", end = "")
        for n in range(len(c[r])):
            print("%6d" % c[r][n], end = "")
        print()
    print('=============================\n')
