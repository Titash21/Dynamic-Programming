#A child can climb 1,2,3 steps at a time
# find the number of ways it can climb n steps
def countWays(n):
    if n<=2:
        return n
    elif n==3:
        return 4
    else:
        stepCount=[0 for i in range(0,n+1)]
        stepCount[1]=1
        stepCount[2]=2
        stepCount[3]=4
        for i in range(4,n+1):
            stepCount[i]=stepCount[i-1]+stepCount[i-2]+stepCount[i-3]
    return stepCount[n]

def main():
    n=int(input("Enter the number of stairs to climb: "))
    ways=countWays(n)
    print("The number of ways to climb",n,"steps is",ways)

main()
