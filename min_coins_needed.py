import sys
def coin_change(totalAmount,coins,coin_list):
    table=[]
    table.append(0)
    for i in range(1,totalAmount+1):
        table.append(sys.maxsize)
    for i in range(0,totalAmount+1):
        for j in range(0,coins):
            if(coin_list[j]<=i):
                temp_result=table[i-coin_list[j]]
                if(temp_result!=sys.maxsize and temp_result+1<table[i]):
                    table[i]=temp_result+1
    
    return table[totalAmount]
def main():
    totalAmount=int(input("Enter the amount to make change for: "))
    coins=int(input("enter the number of denominations available: "))
    coin_list=[]
    for i in range(0,coins):
        coin_list.append(int(input("enter coin: ")))
    minimumcoins=coin_change(totalAmount,coins,coin_list)
    print("Minimum Coins required are",minimumcoins)

main()
