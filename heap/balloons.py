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

def main():
    f = open( input( "What is the file containing balloons? " ) )
    size = f[ 0 ]
    lst = [ ]
    for n in range( 1, len( f ) ):
        lst.append( Balloon( f[ n ][ 0 ], f[ n ][ 1 ], f[ n ][ 2 ], f[ n ][ 3 ] ) )
    

main()