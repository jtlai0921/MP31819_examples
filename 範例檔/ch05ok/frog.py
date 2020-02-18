def JumpStep(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return JumpStep(n-1)+JumpStep(n-2)
for i in range(1,10):
    print(i,'階共有',JumpStep(i),'種跳法')
