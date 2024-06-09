def count_repeat(numbers:list)-> int:
    """this function for get the repeat count of a perticular number"""  
    count = 0 
    for number in numbers:
        if number ==0 :
            count = count + 1           
    return count

print(count_repeat([0,1,2,0,5]))
