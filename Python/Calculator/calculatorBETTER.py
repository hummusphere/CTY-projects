while 1 < 2:
    equation = str(input('Enter Equation : '))
    num = 0
    numlist = [ ]
    operationlist = [ ]
    while num != len(equation):
        number = ''
        while equation[num] != '+'  and equation[num] != '-' and equation[num] != '*'  and equation[num] != '/' and equation[num] != '^':
            number = number + str(equation[num])
            if num + 1 != len(equation):
                num = num + 1
            else:
                break
        if equation[num] == '+' or equation[num] == '-' or equation[num] == '*' or equation[num] == '+' or equation[num] == '/' or equation[num] == '^':
            operationlist.append(equation[num])
        num = num+1
        numlist.append(number)
        total = 0
    for count in range(0, len(numlist)-1):
        operation = operationlist[count]
        if operation == '+':
            if count > 0:
                total = total + float(numlist[count+1])
            else:
                total = total + (float(numlist[count]) + float(numlist[count+1]))
        if operation == '-':
            if count > 0:
                total = total - float(numlist[count+1])
            else:
                total = total + (float(numlist[count]) - float(numlist[count+1]))
        if operation == '*':
            if count > 0:
                total = total * float(numlist[count+1])
            else:
                total = total + (float(numlist[count]) * float(numlist[count+1]))
        if operation == '/':
            if count > 0:
                total = total / float(numlist[count+1])
            else:
                total = total + (float(numlist[count]) / float(numlist[count+1]))
        if operation == '^':
                if float(numlist[count+1]) != 0:
                    for numb in range(0, (int(numlist[count])-1)):
                        total = total ** float(numlist[count+1])
                else:
                    total = 1
    print('The answer is : %s' % total)
    

            
