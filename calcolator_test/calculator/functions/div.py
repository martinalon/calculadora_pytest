def division(a:str, b:str) -> float:
    try:
        my_a = float(a)
        my_b = float(b)
        return(my_a/my_b)
    except Exception as e:
        return("you have the follow error: " + str(e))
    
#print(division('3', '4'))