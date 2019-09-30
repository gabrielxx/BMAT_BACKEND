class AncestorClass():

    def setItemQuestion(self, params):
        data = params.split(' ');
        try:
            self.items = int(data[0])
            self.question = int(data[1])
        except:
            print('Formato de datos invalidos, verifique.')

    def setRoot(self, root):
        self.root = root
        self.setNodo(root,None)

    def setNodo(self, parent, child):
        if parent not in self.nodos.keys():
            self.nodos[parent] = []
        if(child != None):
            self.nodos[parent].append(child)

    def setItems(self, item):
        data = item.split(" ")
        self.setNodo(data[0],data[1])

    def setQuestions(self,question):
        data = question.split(' ')
        self.findAncestor(data[0] , data[1])

    def findAncestor(self, genreA, genreB):
        ancestor = ''
        if(genreA == self.root or genreB == self.root):
            ancestor = self.root;

        elif(self.isParent(genreA)):
            parents = self.getParents(genreB)
            if( genreA in parents):
                ancestor = genreA
            else:
                bucle = True
                while(bucle):
                    genreA = self.getLastParent(genreA)
                    if( genreA in parents):
                        ancestor = genreA    
                        bucle = False

        elif(self.isParent(genreB)):
            parents = self.getParents(genreA)
            if( genreB in parents):
                ancestor = genreB
            else:
                bucle = True
                while(bucle):
                    genreB = self.getLastParent(genreB)
                    if( genreB in parents):
                        ancestor = genreB    
                        bucle = False
        else:
            parents = self.getParents(genreB)
            bucle = True
            while(bucle):
                genreA = self.getLastParent(genreA)
                if( genreA in parents):
                    ancestor = genreA    
                    bucle = False

        self.questions.append(ancestor)

    def __init__(self):
        self.questions = []
        self.nodos = {}

    def isParent(self,nodo):
        return nodo in self.nodos.keys()

    def getParents(self, nodo):
        bucle = True
        parents = []
        while(bucle):
            for i in self.nodos:
                if nodo in self.nodos[i]:
                    parents.append(i)
                    nodo = i
            if(self.root == nodo):
                bucle = False
        return parents

    def getLastParent(self, nodo):
        for i in self.nodos:
            if nodo in self.nodos[i]:
                nodo = i
        return nodo