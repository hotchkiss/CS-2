"""
filename: balloons.py
language: python3
author: collin hotchkiss hotchkiss@rit.edu
date created: 2013-01-30
"""
import * from array_heap.py

class Balloon( object ):
    """
        Balloon object to be stored in a heap
    """
    __slots__ = ( 'name', 'x', 'y', 'z' )
    
    def __init__( self, 'color', 'x', 'y', 'z' ):
        """
            Initializes a balloon object
        """
        self.name = color
        self.x = x
        self.y = y
        self.z = z
    
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
    
    def __init__( self, 'first', 'second' ):
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

class BalloonHeap( Heap ):
    """
    
    """
    __slots__ = ( 'popped' )
    
    def __init__( self ):
        self.super()
        self.popped = { }
    
    def __str__( self ):
        pass

def main():
    f = open( input( "What is the file containing balloons? " ) )
    size = f[ 0 ]
    lst = [ ]
    size = len( lst )
    size *= size
    for n in range( 1, len( f ) ):
        lst.append( Balloon( f[ n ][ 0 ], f[ n ][ 1 ], f[ n ][ 2 ], f[ n ][ 3 ] ) )
    allPairs = [ ]
    for i in range( len( lst ) ):
        for n in range( i + 1, len( lst ) ):
            allPairs.append( BalloonPair( lst[ i ], lst[ n ] ) )
    balloonHeap = Heap( size, < )
    for item in allPairs:
        add( balloonHeap, item )
    
main()