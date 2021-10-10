def ngramdistance(n,str1,str2):
    str1 = (n - 1) * '#' + str1 + (n - 1) * '#'
    str2 = (n - 1) * '#' + str2 + (n - 1) * '#'
    set1 = []
    set2 = []
    for i in range(0,len(str1)-n+1):
        set1.append(str1[i:i+n])
    for i in range(0, len(str2)-n+1):
        set2.append(str2[i:i+n])
    print(set2)
    print(set1)
    l1 = len(set1)
    l2 = len(set2)
    count = 0
    for i in set2:
        for j in set1:
            if i == j:
                count += 1
    result = l1 + l2 - (n*count)
    return print("The",n,"-gram distance is:",result)
n = 2
str1 = "cart"
str2 = "crat"
ngramdistance(n,str1,str2)