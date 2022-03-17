######################################################
# Cristopher Jose Rodolfo Barrios Solis - 18207
######################################################
# main.py
######################################################
# Proyecto 1 - Diseño de Lenguajes de Programación.
######################################################

class NodeT:
    '''
    Clase para representar a un nodo tomando en cuenta el algoritmo de 
    thompson.

    Atributos:
     - relations = arreglo de relaciones tipo Relacion()
     - isInitial = es inicial
     - isAccepting = es final o de aceptacion
    '''
    def __init__(self,isInitial=False,isAccepting=False):
        self.relations = []
        self.isInitial = isInitial
        self.isAccepting = isAccepting

    #gets
    def getRelations(self):
        rels = []
        for i in self.relations:
            rels.append(i)
        return rels

    def getIsInitial(self):
        return self.isInitial

    def getIsAccepting(self):
        return self.isAccepting

    #others
    def addRelation(self,relation):
        self.relations.append(relation)

    def updateRelations(self,updatedDict):
        '''
        Funcion que actualiza las relaciones de cada nodo en base a un diccionario con los
        estados actualizados.
        '''
        for rel in self.relations:
            rel.updateRelation(updatedDict)

    def clearStates(self):
        self.isInitial = False
        self.isAccepting = False
        
# useful functions
def getAFNRelations(AFN):
    '''
    Funcion que retorna las relaciones de un afn
    '''
    rels = []
    for id, node in AFN.items():
        node_rels = node.getRelations()
        if(len(node_rels) > 0):
            rels.append(node_rels)
    return rels

def getAcceptingStates(AFN):
    '''
    Funcion que retorna los estados de aceptacion o finales de un afn
    '''
    acceptingStates = []
    for id, node in AFN.items():
        if(node.getIsAccepting()):
            acceptingStates.append(id)
    return acceptingStates

def getInitialStates(AFN):
    '''
    Funcion que retorna los estados de iniciales de un afn
    '''
    initialStates = []
    for id, node in AFN.items():
        if(node.getIsInitial()):
            initialStates.append(id)
    return initialStates

def updateNodesId(statesCounter,AFN):
    '''
    Funcion que centraliza las actualizaciones de los estados de los nodos en primer lugar y luego
    las actualizacion de las relaciones de cada nodo.
    '''
    updatedAFN = {}
    oldRelationsId = {}
    for id, node in AFN.items():
        #actualizamos la relacion antigua
        oldRelationsId[id] = statesCounter+1
        #colocamos la relacion actualizada en el adn a retornar
        updatedAFN[oldRelationsId[id]] = node
        #aumentamos el contador
        statesCounter = statesCounter+1

    for id, node in updatedAFN.items():
        node.updateRelations(oldRelationsId)

    return statesCounter, updatedAFN

# get node ids
def getInitialNodeId(AFN):
    '''
    Devuelve el id del nodo inicial de un afn cualquiera
    '''
    for id, node in AFN.items():
        if(node.getIsInitial()):
            node.clearStates()
            return id, AFN

def getAcceptingNodeId(AFN):
    '''
    Devuelve el id del nodo de aceptacion o final de un afn cualquiera
    '''
    for id, node in AFN.items():
        if(node.getIsAccepting()):
            node.clearStates()
            return id, AFN