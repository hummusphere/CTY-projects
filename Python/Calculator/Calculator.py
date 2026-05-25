print('Humdan\'s Calculator')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

num = input('Enter Number To Continue :')

def add(a,b):

    add1 = a
    add2 = b

    int(add1)
    int(add2)
    
    var = add1 + add2
    return(var)

def sub(a,b):

    sub1 = a
    sub2 = b

    int(sub1)
    int(sub2)

    var = sub1 - sub2
    return(var)

def mul(a,b):
   
    mul1 = a
    mul2 = b

    int(mul1)
    int(mul2)

    var = mul1 * mul2
    return(var)

def div(a, b):

    div1 = a
    div2 = b

    int(div1)
    int(div2)

    var = div1 / div2
    return(var)

num1 = input('Enter Number :')
num2 = input('Enter Number :')

if num == '1':
    addedfinal = add(int(num1), int(num2))

    num1 = str(num1)
    num2 = str(num2)
    addedfinal = str(addedfinal)

    print(num1 + ' + ' + num2 + ' = ' + addedfinal)

if num == '2':
    subfinal = sub(int(num1), int(num2))

    num1 = str(num1)
    num2 = str(num2)
    subfinal = str(subfinal)

    print(num1 + ' - ' + num2 + ' = ' + subfinal)

if num == '3':
    mulfinal = mul(int(num1), int(num2))

    num1 = str(num1)
    num2 = str(num2)
    mulfinal = str(mulfinal)

    print(num1 + ' * ' + num2 + ' = ' + mulfinal)

if num == '4':
    divfinal = div(int(num1), int(num2))

    num1 = str(num1)
    num2 = str(num2)
    divfinal = str(divfinal)

    print(num1 + ' / ' + num2 + ' = ' + divfinal)
    


    
