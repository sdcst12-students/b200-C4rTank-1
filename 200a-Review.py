#!python3

def getIntegers(INTERGERS_LIST, OTHER_INTEGERS_LIST, NEW_INTERGERS_LIST):
    INTERGERS_LIST = [1,2,3]

    print("List_Old")
    for x in INTERGERS_LIST:
        print(x)

    NEW_INTERGERS_LIST = INTERGERS_LIST

    print("List_New")
    print(NEW_INTERGERS_LIST)

#getIntegers(INTERGERS_LIST=True, OTHER_INTEGERS_LIST=True, NEW_INTERGERS_LIST=True)

#DONE

#-----------------------------------------------------------------------------------------#

def getFactor(FACTORS_LIST,NUMBER):
    NUMBER = 10
    FACTORS_LIST = []
    for x in range(1, NUMBER + 1):
        if NUMBER % x ==0:


            FACTORS_LIST.append (x)
    
    print(FACTORS_LIST)
    
#getFactor(FACTORS_LIST=True,NUMBER=True)

#DONE

#-----------------------------------------------------------------------------------------#

def getNegatives(P_LIST, N_LIST):
    P_LIST = [1,-1 ,2,-2 ,3,-3 ,4,-4 ,5,-5]
    N_LIST = []
    for x in P_LIST:
        if x < 0:
            P_LIST.remove (x)
            N_LIST.append (x)
    print(P_LIST)
    print(N_LIST)

#getNegatives(P_LIST=True, N_LIST=True)

#DONE

#-----------------------------------------------------------------------------------------#

def getIntersection(LIST_1,LIST_2,LIST_3):
    LIST_1 =[3,1,5,4,7,6]
    LIST_2 =[3,9,5,8,2,6]
    LIST_3 =[x for x in LIST_1 if x in LIST_2]
    print(LIST_3)
    
#getIntersection(LIST_1=True ,LIST_2=True, LIST_3=True)

#DONE

#-----------------------------------------------------------------------------------------#

def getUnion(LIST_1,LIST_2):
    LIST_1 =[1,2,2,3,4,5]
    LIST_2 =[4,5,6,7,8,8]
    UNION = []

    UNION = LIST_1 + LIST_2
    UNION = list(dict.fromkeys(UNION))
    print(UNION)

#getUnion(LIST_1=True ,LIST_2=True)

#DONE

#-----------------------------------------------------------------------------------------#

def getMerge(LIST_1,LIST_2,LIST_3):
    LIST_1 = [1,2,3,3,5]
    LIST_2 = [4,2,7,8,9]
    LIST_3 = LIST_1 + LIST_2
    LIST_3.sort()
    print(LIST_3)

#getMerge(LIST_1=True ,LIST_2=True, LIST_3=True)

#DONE

#-----------------------------------------------------------------------------------------#

def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try:
        assert getIntegers([3,4,1.2,1.3,5]) == [3,4,5]
        assert getFactor(range(10),12) == [1,2,3,4,6]
        assert getNegatives([-3,-1,0,1,4]) == [-3,-1]
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert getIntersection(easy1,easy2) == [2,4,6]
        assert getMerge(easy1,easy2) == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()
