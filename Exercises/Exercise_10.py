def merge_list(list1, list2):
    list_result =[]
    for num in list1:
        if num % 2 != 0:
            list_result.append(num)
    for num in list2:
        if num % 2 == 0:
            list_result.append(num)
    print(list_result)  

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
                
merge_list(list1, list2)