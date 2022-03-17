######################################################
# Cristopher Jose Rodolfo Barrios Solis - 18207
######################################################
# main.py
######################################################
# Proyecto 1 - Diseño de Lenguajes de Programación.
# Libreria de utilidades.
######################################################

class functions:

    def getRegExUniqueTokens(self,postfix_regex,words=False):
        '''
        Funcion que obtiene los tokens unicos o el lenguaje de una expresion regular en formato postfix.
        '''
        ops = '*|.#'
        tokens = []
        for i in range(len(postfix_regex)):
            token = postfix_regex[i]
            op_exist = token in ops
            if(op_exist == False):
                tokens.append(token)

        return list(dict.fromkeys(tokens))

    def stringToArray(self,string):
        result = string.replace('',' ').split(' ')
        result.pop(0)
        result.pop()
        return result

    def isOperand(self,character):
        """
        Retorna TRUE si el caracter ingresado es un alfanumerico, FALSE de lo contrario
        *@param ch: el caracter a ser probado
        """
        if character.isalnum() or character == "ε" or character == "#":
            return True
        return False