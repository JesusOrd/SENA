def menu():
    while True:
        print("-----SELECCIONE UNA OPCIÓN-----")
        print("1. Ingresar datos")
        print("2. Realizar operaciones")
        print("3. Salir")
        opcion=int(input())
        if opcion==1:
            ingresar_datos()
        if opcion==2:
            realizar_operaciones()
        else:

            break

def ingresar_datos():
    print("Ingrese el primer número")
    num1=int(input())
    print("Ingrese el Segundo número")
    num2=int(input())
    print("Ingrese un nombre")
    nombre=str(input())
    print("El primer numero, segundo numero y el nombre son",num1,",",num2,"y",nombre, "respectivamente")
    

def realizar_operaciones():
    print("Ingrese el número 1")
    num1=int(input())
    print("Ingrese el número 2")
    num2=int(input())
    print("-----------------------------------------------")
    operacion_suma(num1,num2)
    operacion_resta(num1,num2)
    operacion_multiplicacion(num1,num2)
    operacion_division(num1,num2)
    return num1,num2

def operacion_suma(n1,n2):
    sum=n1+n2
    print(f"La suma de los valores {n1} y {n2} es {sum} ")
    eval_sum(sum)
    eval_cero_sum(sum)
    return sum

def operacion_resta(n1,n2):
    res=n1-n2
    print(f"La resta de los valores {n1} y {n2} es {res} ")
    eval_res(res)
    eval_cero_res(res)
    return res

def operacion_multiplicacion(n1,n2):
    mul=n1*n2
    print(f"La multiplicacion de los valores {n1} y {n2} es {mul} ")
    eval_mul(mul)
    eval_cero_mul(mul)
    return mul

def operacion_division(n1,n2):
    div=n1/n2
    print(f"La division de los valores {n1} y {n2} es {div} ")
    eval_div(div)
    eval_cero_div(div)
    return div

def eval_sum(valor):
    if valor%2==0:
        print("Es par")
    else:
        print("Es impar")

def eval_res(valor2):    
    if valor2%2==0:
        print("Es par")
    else:
        print("Es impar")

def eval_mul(valor):
    if valor%2==0:
       print("Es par")
    else:
       print("Es impar")

def eval_div(valor):
    if valor%2==0:
        print("Es par")
    else: 
        print("Es impar")

def eval_cero_sum(valor):
    if valor==0:
        print("-------EL VALOR NO SERÁ GUARDADO!!!-------")
    else:
        print("-------EL VALOR HA SIDO GUARDADO!!!-------")

def eval_cero_res(valor):    
    if valor==0:
        print("-------EL VALOR NO SERÁ GUARDADO!!!-------")
    else:
        print("-------EL VALOR HA SIDO GUARDADO!!!-------")

def eval_cero_mul(valor):    
    if valor==0:
        print("-------EL VALOR NO SERÁ GUARDADO!!!-------")
    else:
        print("-------EL VALOR HA SIDO GUARDADO!!!-------")

def eval_cero_div(valor):    
    if valor==0:
        print("-------EL VALOR NO SERÁ GUARDADO!!!-------")
    else:
        print("-------EL VALOR HA SIDO GUARDADO!!!-------")


#******************Codigo principal********************
menu()