def linear_search(container, item, index=0):
    if index >= len(container): #base case 1:
        return -1
    if container[index] == item: #base case 2: When we found item
        return index
    
    return linear_search(container, item, index+1)

print(linear_search([4,5,8,2,1,4,7], 2))