
import time

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def eval_(formula_string):

    def precheck(stroka):
        stack=[]
        bool1=True
        while bool1:

            indexmax=stroka.find('max')




            if indexmax>=0:
                i=indexmax

                bool=True
                while bool:


                    if stroka[i+3]=='(':

                        stack.append('(')
                    if stroka[i+3]==')':

                        stack.pop()

                    i+=1
                    if not stack:
                        bool=False

                strokachange=stroka[indexmax+4:i+2]

                stroka = stroka[:indexmax+1] + stroka[i+3:]
                strokachange=precheck(strokachange)


                strokachange=strokachange.split(',')
                array=[]

                for y in strokachange:

                    array.append(eval_(y))



                stroka = stroka[:indexmax] + str(max(array)) + stroka[indexmax+1:]


            indexmin=stroka.find('min')


            if indexmin>=0:
                i=indexmin

                bool=True
                while bool:


                    if stroka[i+3]=='(':

                        stack.append('(')
                    if stroka[i+3]==')':

                        stack.pop()

                    i+=1
                    if not stack:
                        bool=False

                strokachange=stroka[indexmin+4:i+2]

                stroka = stroka[:indexmin+1] + stroka[i+3:]
                strokachange=precheck(strokachange)


                strokachange=strokachange.split(',')
                array=[]

                for y in strokachange:

                    array.append(eval_(y))



                stroka = stroka[:indexmin] + str(min(array)) + stroka[indexmin+1:]



            indexround=stroka.find('round')
            if indexround>=0:
                i=indexround

                bool=True
                while bool:


                    if stroka[i+5]=='(':
                        stack.append('(')
                    if stroka[i+5]==')':

                        stack.pop()

                    i+=1
                    if not stack:
                        bool=False

                strokachange=stroka[indexround+6:i+4]
                stroka = stroka[:indexround+1] + stroka[i+5:]
                strokachange=precheck(strokachange)



                strokachange=strokachange.split(',')
                array=[]

                for y in strokachange:


                    array.append(eval_(y))



                stroka = stroka[:indexround] + str(round(array[0],int(array[1]))) + stroka[indexround+1:]




            if indexmax==-1 and indexmin==-1 and indexround==-1: bool1=False






        return stroka



    formula_string=precheck(formula_string)






    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.': # если символ - цифра, то собираем число
                number += s
            elif number: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()" : # если символ - оператор или скобка, то выдаём как есть
                yield s
        if number:  # если в конце строки есть число, выдаём его
            yield float(number)



    def shunting_yard(parsed_formula):
        stack = []  # в качестве стэка используем список
        for token in parsed_formula:
            # если элемент - оператор, то отправляем дальше все операторы из стека,
            # чей приоритет больше или равен пришедшему,
            # до открывающей скобки или опустошения стека.
            # здесь мы пользуемся тем, что все операторы право-ассоциативны
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                # а открывающую скобку выкидываем из стека.
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                # если элемент - открывающая скобка, просто положим её в стек
                stack.append(token)
            else:
                # если элемент - число, отправим его сразу на выход
                yield token
        while stack:
            yield stack.pop()






    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:  # если приходящий элемент - оператор,
                y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                stack.append(OPERATORS[token][1](x, y)) # вычисляем оператор, возвращаем в стек
            else:
                stack.append(token)
        return stack[0] # результат вычисления - единственный элемент в стеке




    return calc(shunting_yard(parse(formula_string)))



stack=[]
#eval_('max(1234)')
print(eval_('round(1.1253,round(3.4,01))'))
