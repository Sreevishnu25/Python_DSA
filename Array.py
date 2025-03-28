def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
        
    return -1

index = linear_search([12, 23, 34, 45, 56, 67, 78, 89], 67)
print(index) 
