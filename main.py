######################################################
# Cristopher Jose Rodolfo Barrios Solis - 18207
######################################################
# main.py
######################################################
# Proyecto 1 - Diseño de Lenguajes de Programación.
######################################################

# imports
import sys
sys.path.append(".")
from RegexToPostFix.RegexToPostFix import RegexToPostfix
from functions import functions
from Thompson.AFNT import AFNT
from Subsets.Subsets import Subsets
from DirectAFD.DirectAFD import DirectAFD

# functions
def welcome():
    print("________________________________________BIENVENIDO_________________________________________")
    print("Implementación de los algoritmos básicos de autómatas finitos y expresiones regulares.")
    print()

def menu():
    #os.system('cls')
    print("Seleccione una opcion.")
    print("\t1. Metodo de Conversion por Thompson y Subconjuntos")
    print("\t2. Metodo de Conversion Directa")
    print("\t3. Salir")

def userInteraction():
    expresion = input('Ingrese una expresion regular: ')
    expresion = expresion.replace(' ','')
    chain = input('Ingrese la cadena a evaluar: ')
    chain = chain.replace(' ','')

    obj = RegexToPostfix()
    postfix = obj.infix_to_postfix(expresion)

    return postfix, chain

def userInteractionDirect():
    '''Esta funcion se agrega el caracter '#' para las operaciones relacionados a la conversion directa.'''
    expresion = input('Ingrese una expresion regular: ')
    expresion = expresion.replace(' ','')
    chain = input('Ingrese la cadena a evaluar: ')
    chain = chain.replace(' ','')

    obj = RegexToPostfix()
    expresion = '('+expresion+')#'
    postfix = obj.infix_to_postfix(expresion)

    return postfix, chain

# Executions
welcome()
functions = functions()
while True:

    menu()
    option = input('Ingrese una opcion: ')

    if(option == '1'):
        chain = ''

        postfixRegex,chain = userInteraction()
        if(postfixRegex == 'ERROR_POSTFIX_)'):
            print('\n ")" faltante en la expresion regular ingresada. Vuelva a intentar. \n')
        else:
            print(' - postfix     = '+ postfixRegex)
            tokens = functions.getRegExUniqueTokens(postfixRegex)
            postfixRegex = functions.stringToArray(postfixRegex)

            print(' - alfabeto (tokens): '+str(tokens))

            obj_afn = AFNT(tokens,chain)
            AFN = obj_afn.generateAFN(postfixRegex)
            
            obj_afd = Subsets(tokens,chain,AFN)
            AFD = obj_afd.afn_to_afd_process()

    elif(option == '2'):
        postfixRegex,chain = userInteractionDirect()
        if(postfixRegex == 'ERROR_POSTFIX_)'):
            print('\n ")" faltante en la expresion regular ingresada. Vuelva a intentar. \n')
        else:
            print(' - postfix     = '+ postfixRegex)
            tokens = functions.getRegExUniqueTokens(postfixRegex)
            postfixRegex = functions.stringToArray(postfixRegex)

            print(' - alfabeto (tokens): '+str(tokens))
        
            objdirect = DirectAFD(tokens,chain,postfixRegex)
            AFD = objdirect.generateDirectAFD()

    elif(option == '3'):
        print('\nGracias por utilizar nuestro programa! ')
        break
    else:
        input('No se ha elejido ninguna opcion valida en el menu. Intentalo otra vez! Presiona Enter!')