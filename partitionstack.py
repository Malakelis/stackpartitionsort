
List = [5,8,3,2,9,7,6]
#List = [7,6,5,4,3,2,1]
#List = [4,5,7,6,2,3,1]
#List = [3,2]

def Partition(List):
    L = []
    U = []
    a = []
    for i in range(1, len(List)):
        
        if (len(List) == 2):
            if List[0] < List[1]:
                L.append(List[0])
                U.append(List[1])
            else:
                L.append(List[1])
                U.append(List[0])
            
            return [L, None, U]

        if List[0] > List[i]:
            L.append(List[i])
        else:
            U.append(List[i])
    a.append(List[0])

    if len(L) == 0 and len(U) == 0:
        return [None, a, None]
    elif len(L) == 0:
        return [None, a, U]
    elif len(U) == 0:
        return [L, a, None]

    return [L, a, U]
   # print(x)
    #a = x.pop()

   # return x

#print(Partition(List))


#print(list)



def StackPartitionSort(List):
    count = 0
    output = []
    X = List

    print("X is " + str(X))

    A = X.copy()
    X = []

    print("A is " + str(A))

    L,a,U = Partition(A)

    if (U is not None):
        X.insert(0, U)
    if (a is not None):
        X.insert(0, a)           
    if (L is not None):
        X.insert(0, L)
    
    count += 1

    #print("X is " + str(X))

    while len(X) > 0:
        print("X is " + str(X))
        A = X[0]                                    
        if isinstance(A, list) and len(A) > 1:
            #print("gay")
            print("A is " + str(A))
            L, a, U = Partition(A)
            #print(L,a,U)

            count += 1
            X = X[1:]                       #pop
            if (U is not None):
                X.insert(0, U)
            if (a is not None):
                X.insert(0, a)           
            if (L is not None):
                X.insert(0, L)
            

        else:
            count += 1                  #pop
            X = X[1:]
            #print("output is " + str(output))
            output.append(A)
    return output, count

print(StackPartitionSort(List))