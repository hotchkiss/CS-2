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
    __slots__ = ( 'name', 'x', 'y', 'z', 'popped' )
    
    def __init__( self, color, x, y, z ):
        """
            Initializes a balloon object
        """
        self.name = color
        self.x = int( x )
        self.y = int( y )
        self.z = int( z )
        self.popped = False
    
    def __str__( self ):
        """
            Returns balloon object represented as a string
        """
        this = str( self.name ) + " at " + str( self.x ) + ", " + str( self.y ) + ", " + str( self.z )
        if self.popped:
            this += ";\ Balloon is popped"
        else:
            this += ";\ Balloon is not popped"
        return this

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
    for n in range( 1, len( lines ) ):
        lst.append( Balloon( lines[ n ][ 0 ], lines[ n ][ 1 ], lines[ n ][ 2 ], lines[ n ][ 3 ] ) )
    size = len( lst )
    size *= size
    allPairs = dict()
    for i in range( len( lst ) ):
        for n in range( i + 1, len( lst ) ):
            distance = dist( lst[ i ], lst[ n ] )
            if distance not in allPairs:
                allPairs[ distance ] = [ ]
            allPairs[ distance ].append( [ lst[ i ], lst[ n ] ] )
    print( len( allPairs ) )
    myHeap = Heap( len( allPairs ) // 2 + 2, less )
    for key in allPairs:
        print( key )
        add( myHeap, key )
    while len( myHeap.array ) > 1:
        #print( len( myHeap.array ) )
        cur = removeMin( myHeap )
        if cur in allPairs:
            for item in allPairs[ cur ]:
                if item[ 0 ].popped or item[ 1 ].popped:
                    ''''''
                    pass
                else:
                    print( item[ 0 ].name + ", " + item[ 1 ].name) 
                    item[ 0 ].popped = True
                    item[ 1 ].popped = True
                allPairs[ cur ] = None
    for balloon in lst:
        if not balloon.popped:
            print( str( balloon ) )
main()