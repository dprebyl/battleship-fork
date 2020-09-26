class ShipNode:
    def __init__(self, x, y): #self is like using 'this' to access the base class from the initalization function. W3 defn: "A reference to the current instance of the class, and is used to access variables that belongs to the class."

        """
        @pre none
        @post ShipNode is created
        @param x,y values of this node
        """

        self.x = x
        self.y = y
        self.hit = False

class Ship:
    def __init__(self): #W3 defn: "A reference to the current instance of the class, and is used to access variables that belongs to the class."

        """
        @pre none
        @post Ship is created
        @param none
        """

        self.shipSquares = [] #The squares that the ships occupy.
        self.sunk = False

    def checkSunk(self):
        
        """
        @pre none
        @post returns true if all ShipNodes are hit, else false
        @param none
        @author Daniel
        """

        for square in self.shipSquares:
            if square.hit == False:
                return False
        self.sunk = True
        return True

    def addSquare(self, x, y):

        """
        @pre none
        @post a ShipNode is added to this Ship's shipSquares list
        @param x,y position of the new ShipNode to add
        """

        self.shipSquares.append(ShipNode(x,y))