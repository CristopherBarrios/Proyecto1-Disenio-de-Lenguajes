######################################################
# Cristopher Jose Rodolfo Barrios Solis - 18207
######################################################
# main.py
######################################################
# Proyecto 1 - Diseño de Lenguajes de Programación.
######################################################

class NodeD:
#Este programa contendra el valor de cada nodo, en especial, los siguientes
    def __init__(self):
        self.nodeId = ""  # es el id del nodo. if not epsilon -> letter
        self.character = ""  
        self.nextPos = ""

        #Relacionados a la tabla magica
        self.annullable = True  
        self.firstPos = []
        self.lastPos = []  

    #gets
    def getNodeId(self):
        return self.nodeId

    def getAnnullable(self):
        return self.annullable

    def getFirstPos(self):
        return self.firstPos

    def getLastPos(self):
        return self.lastPos

    def getNodeChar(self):
        return self.character

    #sets
    def setCaracterNodo(self, character):
        self.character = character

    def setNodoId(self, nodeId):
        self.nodeId = nodeId

    def setAnnullable(self, annullable):
        self.annullable = annullable

    def setFirstPos(self, firstPos):
        self.firstPos = firstPos

    def setLastPos(self, lastPos):
        self.lastPos = lastPos