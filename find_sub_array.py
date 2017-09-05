def find_subarray():
    flag=0
    size=int(input("Enter size of array: "))
    array=[]
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    total_price=int(input("Enter the total_price: "))
    sub_array=[]
    flag=0
    for i in range(size):
        total=array[i]
        sub_array.append(array[i])
        for j in range(i+1,size):
            total=total+array[j]
            sub_array.append(array[j])
            if(total>total_price):
                total=total-array[j]
                sub_array.remove(array[j])
            elif(total==total_price):
                print(sub_array)
                flag=1
        sub_array=[]


    if(flag==1):
        print("True")
    else:
        print("False")
find_subarray()
