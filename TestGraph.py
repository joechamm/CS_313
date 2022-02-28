class Vertex (object):
    # creates a vertex with specific label 
    # and the vertex is initially unmarked
    def __init__ (self, label):
        self.label = label
        self.edgeList = []
        self.mark = False

    # unmark the vertex
    def clearMark (self):
        self.mark = False

    # mark the vertex
    def setMark (self):
        self.mark = True

    # returns True if the vertex is marked and False otherwise
    def isMarked (self):
        return self.mark

    # returns the label of the vertex
    def getLabel (self):
        return self.label

    # changes the label of the vertex in the graph g to given label
    def setLabel (self, label, g):
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label

    # adds an edge with the given weight from this vertex to the toVertex
    def addEdgeTo (self, toVertex, weight = 1):
        newEdge = Edge(self, toVertex, weight)
        self.edgeList.append(newEdge)
        
    # returns the edge from this vertex to the toVertex or 
    # returns None if the edge does not exist
    def getEdgeTo (self, toVertex):
        for edge in self.edgeList:
            if edge.vertex1 == toVertex:
                return edge
        return None

    # returns a list of the incident edges of this vertex
    def incidentEdges (self):
        return self.edgeList

    # returns a list of vertices that are adjacent to this vertex
    def neighboringVertices (self):
        temp = []
        for edge in self.edgeList:
            temp.append(edge.getOtherVertex(self))
        return temp

    # returns a string representation of the vertex
    def __str__ (self):
        st = 'Vertex: %s \n' % (str(self.label))
        if len(self.edgeList) > 0:
            st += 'Edges: '
            for edg in self.edgeList:
                st += '%s \n' % (str(edg))
        return st

class Edge (object):
    # creates an edge with specified vertices and weight
    # it is inially unmarked
    def __init__ (self, fromVertex, toVertex, weight = 1):
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
        self.mark = False

    # unmarks the edge
    def clearMark (self):
        self.mark = False

    # marks the edge 
    def setMark (self):
        self.mark = True

    # returns True if the edge is marked and False otherwise
    def isMarked (self):
        return self.mark

    # returns the weight of the edge
    def getWeight (self):
        return self.weight

    # sets the edge's weight
    def setWeight (self, weight):
        self.weight = weight

    # returns the edge's other vertex
    def getOtherVertex (self, vertex):
        if vertex == self.vertex1:
            return self.vertex2
        else:
            return self.vertex1


    # returns the edge's destination vertex
    def getToVertex (self):
        return self.vertex2

    # returns the string representation of the edge
    def __str__(self):
        st = 'From Vertex: %s \n' % (str(self.vertex1))
        st += 'To Vertex: %s \n' % (str(self.vertex2))
        st += 'Weight: %s \n' % (str(self.weight))

class Graph (object):
    # creates a graph with adjacency list
    def __init__ (self):
        self.numVerts = 0
        self.numEdges = 0
        self.verts = {}

      
    # removes all vertices and edges from the graph
    def clear (self):
        self.numVerts = 0
        self.numEdges = 0
        self.vertices = {}

    # unmark all vertices
    def clearVertexMarks (self):
        for vert in self.vertices():
            vert.clearMark()

    # unmark all edges
    def clearEdgeMarks (self):
        for edge in self.edges():
            edge.clearMark()

    # returns True if the graph is empty and False otherwise
    def isEmpty (self):
        return (self.numVerts == 0)

    # returns the number of edges in the graph
    def numEdges (self):
        return self.numEdges

    # returns the number of vertices in the graph
    def numVertices (self):
        return self.numVerts

    # returns the String representation of the graph
    def __str__ (self):
        st = 'NumVerts: %s \n' % (str(self.numVerts))
        for vert in self.vertices():
            st += '%s \n' % (str(vert))
        return st


    ## vertex related functions ##

    # returns True if the graph contains this vertex and False otherwise
    def containsVertex (self, label):
        return label in self.vertices

    # adds a vertex with the specified label
    def addVertex (self, label):
        self.vertices[label] = Vertex(label)
        self.numVerts += 1

    # returns the vertex with the label or None
    def getVertex (self, label):
        return self.vertices[label]

    # removes the vertex with the label
    def removeVertex (self, label):
        rmVert = self.verts.pop(label, None)
        if rmVert == None:
            return False
        for vert in self.vertices():
            if vert.removeEdgeTo(rmVert):
                self.numEdges -= 1
        self.numVerts -= 1
        return True

    ## edge related functions ##

    # returns True if the graph contains this edge and False otherwise
    def containsEdge (self, fromLabel, toLabel):
        return self.getEdge(fromLabel, toLabel) != None

    # adds an edge with given weight
    def addEdge (self, fromLabel, toLabel, weight = 1):
        fromVert = self.getVertex(fromLabel)
        toVert = self.getVertex(toLabel)
        fromVert.addEdgeTo(toVertex, weight)
        self.numEdges += 1
        
    # returns the edge or None
    def getEdge (self, fromLabel, toLabel):
        fromVert = self.verts[fromLabel]
        toVert = self.verts[toLabel]
        return fromVert.getEdgeTo(toVert)

    # remove and return the edge
    def removeEdge (self, fromLabel, toLabel):
        fromVert = self.getVertex(fromLabel)
        toVert = self.getVertex(toLabel)
        rmEdge = fromVert.removeEdgeTo(toVert)
        if rmEdge:
            self.numEdges -= 1
        return rmEdge

    ## iterators  ##

    # returns a list of edges in the graph
    def edges (self):
        temp = set()
        for vert in self.vertices():
            edgeSet = vert.incidentEdges()
            temp = temp.union(set(edgeSet))
        return iter(temp)        

    # returns a list of vertices in the graph
    def vertices (self):
        return iter(self.verts.values())

    # returns the list of edges from a given vertex
    def incidentEdges (self, label):
        return self.verts[label].incidentEdges()

    # returns the list of vertices adjacent to a given vertex
    def neighboringVertices (self, label):
        return self.verts[label].neighboringVertices()


class Stack (object):
    # create a stack object using a list
    def __init__ (self):
        self.stack = []

    # push an object on the stack
    def push (self, data):
        self.stack.append(data)

    # pop an object off the stack
    def pop (self):
        return self.stack.pop()

    # peek at an object on the top of the stack
    def peek (self):
        return self.stack[len(self.stack) - 1]

    # return True if the Stack is empty or False otherwise
    def isEmpty (self):
        return (len(self.stack) == 0)

class Queue (object):
    # create a queue object using a list
    def __init__ (self):
        self.queue = []

    # add an object from the queue
    def enqueue (self, data):
        self.queue.append(data)

    # remove an object from the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # return True if the Queue is empty or False otherwise
    def isEmpty (self):
        return (len(self.queue) == 0)

def _getCommand(self, high, menu):
    """Obtains and returns a command number."""
    prompt = "Enter a number [1-" + str(high) + "]: "
    commandRange = map(str, range(1, high + 1))
    error = "Error, number must be 1 to " + str(high)
    while True:
        print menu
        command = raw_input(prompt)
        if command in commandRange:
            return int(command)
        else:
            print error

def _getFromKeyboard(self):
    """Inputs a description of the graph from the keyboard
    and creates the graph."""
    rep = ""
    while True:
        edge = raw_input("Enter an edge or return to quit: ")
        if edge == "": break
        rep += edge + " "
    startLabel = raw_input("Enter the start label: ")
    print self._model.createGraph(rep, startLabel)

def _getFromFile(self):
    """Inputs a description of the graph from a file
    and creates the graph."""
    fileName = raw_input("Enter the file name: ")
    theFile = open(fileName, 'r')
    rep = theFile.readline().strip()
    startLabel = theFile.readline().strip()
    print self._model.createGraph(rep, startLabel)



def main():
##    infile = open('graph.txt','r')
    menu = "Main menu\n" + \
               "  1  Input a graph from the keyboard\n" + \
               "  2  Input a graph from a file\n" + \
               "  3  View the current graph\n" \
               "  4  Single source shortest paths\n" \
               "  5  Minimum spanning tree\n" \
               "  6  Topological sort\n" \
               "  7  Exit the program\n"
    while True:
        command = self._getCommand(7, menu)
        if   command == 1: self._getFromKeyboard()
        elif command == 2: self._getFromFile()
        elif command == 3:
            print self._model.getGraph()
        elif command == 4:
            print "Paths:\n", self._model.run(shortestPaths)
        elif command == 5:
            print "Tree:", \
                  " ".join(map(str, self._model.run(spanTree)))
        elif command == 6:
            print "Sort:", \
                  " ".join(map(str, self._model.run(topoSort)))
        else: break

    

    
main()
            
            
        
                         
