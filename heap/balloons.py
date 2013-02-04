"""
filename: balloons.py
language: python3
author: collin hotchkiss hotchkiss@rit.edu
date created: 2013-01-30
"""
from array_heap import *
import math

class Balloon( object ):
    """
        Balloon object to be stored in a heap
    """
    __slots__ = ( 'name', 'x', 'y', 'z' )
    
    def __init__( self, color, x, y, z ):
        """
            Initializes a balloon object
        """
        self.name = color
        self.x = int( x ) 
        self.y = int( y )
        self.z = int( z )
    
    def __str__( self ):
        """
            Returns balloon object represented as a string
        """
        return ( str( self.name ) + " at " + self.x + ", " + self.y + ", " + self.z )

class BalloonPair( object ):
    """
        Pair of balloon objects that includes their distance
    """
    __slots__ = ( 'first', 'second', 'dist' )
    
    def __init__( self, first, second ):
        """
        
        """
        self.first = first
        self.second = second
        dx = first.x - second.x
        dy = first.y - second.y
        dz = first.z - second.z
        sum = ( dx * dx ) + ( dy * dy ) + ( dz * dz )
        self.dist = math.sqrt( sum )
    
    def __str__( self ):
        """
            Returns pair represented as a string
        """
        return( "First balloon: " + self.first.name + "\; Second balloon: " + self.second.name + "\; Distance: " + str( self.dist ) )
    
    def cmp( self, other ):
        """
            Compares distance values and returns true if its distance is less than other's distance
        """
        if self.dist < other.dist:
            return -1
        elif self.dist > other.dist:
            return 1
        else: return 0

"""
class BalloonHeap( Heap ):
    __slots__ = ( 'popped' )
    
    def __init__( self, size ):
        Heap.__init__( self, size, min )
        self.popped = 
    
    def __str__( self ):
        pass
"""

"""def compareFunc( a, b ):
    
        Returns true if a's dist is less than b's
        Preconditions: a and b are both BalloonPair objects
    
   return a.dist < b.dist
"""
def dist( a, b ):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    sum = ( x * x ) + ( y * y ) + ( z * z )
    return math.sqrt( sum )

def main():
    f = open( input( "What is the file containing balloons? " ) )
    lines = [ ]
    for line in f:
        line = line.split()
        lines.append( line )
    size = int( lines[ 0 ][ 0 ] )
    lst = [ ]
    size = len( lst )
    size *= size
    for n in range( 1, len( lines ) ):
        print( lines[ n ][ 0 ]  + str( lines[ n ][ 1 ] ) )
        lst.append( Balloon( lines[ n ][ 0 ], lines[ n ][ 1 ], lines[ n ][ 2 ], lines[ n ][ 3 ] ) )
    allPairs = dict()
    for i in range( len( lst ) ):
        for n in range( i + 1, len( lst ) ):
            allPairs.[ dist( lst[ i ].dist, lst[ n ].dist ) ] += ( [ lst[ i ], lst[ n ],  )
    popped = { }
    myHeap = Heap( size + 1, less )
    for item in allPairs:
        add( myHeap, [ item.key, item.value ] )
    while len( myHeap.array ) > 1:
        if myHeap.array[ 0 ][ 0 ] not in popped:
            nextPop = removeMin( myHeap )
            myHeap.popped.add( nextPop.first )
            myHeap.popped.add( nextPop.second )
        else:
            removeMin( myHeap )
            siftUp( myHeap, 1)

main()