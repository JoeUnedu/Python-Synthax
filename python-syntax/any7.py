def any7(num):

    """Are any of these numbers a 7? (True/False)"""  
    for seven in  num: 
        if seven == 7: 
            return True  
    else:
       return False
    

 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

