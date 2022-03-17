######################################################
# Cristopher Jose Rodolfo Barrios Solis - 18207
######################################################
# main.py
######################################################
# Proyecto 1 - Diseño de Lenguajes de Programación.
# Clase que evalua una expresion regular.
######################################################

#Classes
class RegexToPostfix:
    '''
    Clase que realiza modificaciones a una expresion infix y luego la convierte a formato postfix

    Atributos:
     - expresion --> la expresion regular en formato infix
    '''
    # Constructor de las variables
    def __init__(self):
        self.operators_precedence = {
        1: '(',
        2: '|',
        3: '.', # operador de concatenacion explicito
        4: '?',
        4: '*',
        4: '+'
        }

    def get_key(self,character):
        '''
        Funcion que retorna la llave para un caracter cualquiera.

        Parametros:
        - character: un caracter o token 
        '''
        for key, value in self.operators_precedence.items():
            if character == value:
                return key
        return None

    def get_precendence(self,character):
        '''
        Funcion que retorna la precedencia del operador ingresado.
        Parametros:
        - character: un caracter o token
        - return - la precedencia correspondiente
        '''
        precedence = self.get_key(character)
        precedence = 5 if precedence == None else precedence
        return precedence

    def replaceQuestionMark(self, exp):
        value = "?" in exp
        if(value == False):
            return exp
        else:
            index = exp.find('?')
            if exp[index-1] == ")":
                inside = ""
                for i in reversed(exp[0:index-1]):
                    inside += i
                    if i == "(":
                        inside = inside[::-1]
                        quantity1 = len(inside)
                        quantity2 = len(exp[0:index-1])
                        ignore = quantity2 - quantity1
                        inside = inside[1:len(inside)]
                        return self.replaceQuestionMark(exp[0:ignore] + "(" + inside + "|ε)" + exp[index+1:len(exp)])
            else:
                return self.replaceQuestionMark(exp[0:index-1] + "(" + exp[index-1] + "|ε)" + exp[index+1:len(exp)])

    def replacePlus(self, exp):
        value = "+" in exp
        if(value == False):
            return exp
        else:
            index = exp.find('+')
            if exp[index-1] == ")":
                inside = ""
                for i in reversed(exp[0:index-1]):
                    inside += i
                    if i == "(":
                        inside = inside[::-1]
                        quantity1 = len(inside)
                        quantity2 = len(exp[0:index-1])
                        ignore = quantity2 - quantity1
                        inside = inside[1:len(inside)]
                        return self.replacePlus(exp[0:ignore] + "(" + inside + "(" + inside + ")*" + ")" + exp[index+1:len(exp)])
            else:
                return self.replacePlus(exp[0:index-1] + "(" + exp[index-1] + exp[index-1] + "*)" + exp[index+1:len(exp)])

    def format_reg_ex(self,regex):
        ''' 
            Funcion que transforma una expresion regular insertando un '.' 
            como indicador/operador explicito de concatenacion.

            Parametros:
            - regex: una cadena (expresion regular)
        '''
        res = ''
        allOperators = ['|','?','+','*']
        binaryOperators = ['|']

        for i in range(0,len(regex)):
            c1 = regex[i]
            if(i+1 < len(regex)):
                c2 = regex[i+1]
                res += c1
                # si c1 no existe en el conjunto de operadores, c2 no existe en el de operadores binarios y tampoco son parentesis
                if(c1 != '(' and c2 != ')' and (c2 in set(allOperators)) == False and (c1 in set(binaryOperators)) == False): 
                    res += '.'

        res += regex[len(regex)-1]

        return res

    def infix_to_postfix(self,expresion):
        '''
        Funcion que convierte una expresion regular en formato infix a formato postfix.
        Esta expresion regular es ingresada al instancia un objeto de esta clase.
        '''
        regex = expresion

        postfix = ''
        stack = []

        
        eqRegexPlus = self.replacePlus(regex)
        eqRegexQuestion = self.replaceQuestionMark(eqRegexPlus)
        formattedRegex = self.format_reg_ex(eqRegexQuestion)
        eqRegex = formattedRegex
      
        for cc in range(len(eqRegex)):
            c = eqRegex[cc]
            if (c == '('):
                stack.append(c)
            elif(c == ')'):
                #si el ultimo elemento de la pila es '(' 
                while (stack[-1] != '('): 
                    postfix += stack.pop()
                stack.pop();
            else:
                while(len(stack) > 0):
                    peekedChar = stack[-1]

                    peekedCharPrecedence = self.get_precendence(peekedChar)
                    currentCharPrecedence = self.get_precendence(c)
      
                    if(peekedCharPrecedence >= currentCharPrecedence):
                        postfix += stack.pop()
                    else:
                        break

                stack.append(c)


        while(len(stack) > 0):
            postfix += stack.pop()

        if(postfix.find('(') != -1):
            postfix = 'ERROR_POSTFIX_)'

        print(' - infix       = '+regex)
        print(' - dottedEq    = '+formattedRegex)
        print(' - substEq     = '+eqRegex)
        return postfix.replace('..','.')