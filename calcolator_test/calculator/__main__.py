from calculator.functions.sum import suma
from calculator.functions.prod import producto
from calculator.functions.div import division

def oprations_list(operacion:str) -> list:
    operaciones = []
    n =''
    for i in operacion:
    
        if i not in ["(", ")"]:
            n = n + i
        else:# i == '(' or i == ')':
            operaciones.append(n)
            n = ''
    operaciones.append(n)
    operaciones = list(filter(None, operaciones))
    return(operaciones)

def calculadora(operaciones:list) -> list:
    new_term = ""
    for terminos in operaciones:
        if len(terminos) == 3:
            if "+" in  terminos or "-" in  terminos:
                operandos = []
                m = ''
                for j in terminos:
                    if j not in ["-", "+"]:
                        m = m + j
                    else:
                        operandos.append(m)
                        m = j
                operandos.append(m)
                new_term = new_term +  str(suma(operandos[0], operandos[1])) 
            elif "/" in terminos:
                my_div = division(terminos[0], terminos[2])
                new_term = new_term  + str(my_div)
            elif "*" in terminos:
                mult = producto(terminos[0], terminos[2])
                new_term = new_term +  str(mult) 
        elif terminos in ['/', '*']:
            new_term = new_term  +  terminos
        else:
            new_term = new_term  + "+"+ terminos
    my_results = new_term.split('+')
    my_results = list(filter(None, my_results))
    if "*" in my_results[0]:
        numbers = my_results[0].split('*')
        result = producto(numbers[0], numbers[1])
    if '/' in my_results[0]:
        numbers = my_results[0].split('/')
        result = producto(numbers[0], numbers[1])
    
    return(result)
    
    



if __name__ == "__main__":
    operacion ='(3/5)*(4-1)' 
    operaciones = oprations_list(operacion)
    calculo = calculadora(operaciones)
    print(calculo)

