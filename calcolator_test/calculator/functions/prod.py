def producto(a:str, b:str)-> float:
    try:
        my_a = float(a)
        my_b = float(b)
        return(my_a*my_b)
    except Exception as e:
        return("this is wrong: " + e)

#print(producto('3.5', '1.1'))