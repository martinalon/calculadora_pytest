def suma(a:str, b:str)-> float:
    try:
        my_a = float(a)
        my_b = float(b)
        return(my_a + my_b)
    except Exception as e:
        return("this is wrong: " + e)
        

#print(suma("-2", "5"))