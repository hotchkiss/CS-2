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
            this += "; Balloon is popped"
        else:
            this += "; Balloon is not popped"
        return this

def dist( a, b ):
    """
        Computes distance between balloon a and b
    """
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    sum = ( x * x ) + ( y * y ) + ( z * z )
    return math.sqrt( sum )

def main():
    """
        Takes a file full of balloon names and locations and prints the name of the balloon that is not popped, if any.
    """
    f = open( input( "What is the file containing balloons? " ) )
    lines = [ ]
    for line in f:
        line = line.split()
        lines.append( line )
    size = int( lines[ 0 ][ 0 ] )
    lst = [ ]
    for n in range( 1, len( lines ) ):
        lst.append( Balloon( lines[ n ][ 0 ], lines[ n ][ 1 ], lines[ n ][ 2 ], lines[ n ][ 3 ] ) )
    allPairs = dict()
    for i in range( len( lst ) ):
        for n in range( i + 1, len( lst ) ):
            distance = dist( lst[ i ], lst[ n ] )
            if distance not in allPairs:
                allPairs[ distance ] = set()
            allPairs[ distance ].add( lst[ i ] )
            allPairs[ distance ].add( lst[ n ] )
    myHeap = Heap( size, less )
    for key in allPairs:
        add( myHeap, key )
    while myHeap.size > 1:
        cur = removeMin( myHeap )
        if cur in allPairs:
            notPopped = 0
            for item in allPairs[ cur ]:
                if not item.popped:
                    notPopped += 1
            if notPopped > 1:
                '''beingPopped = "" '''
                for balloon in allPairs[ cur ]:
                    if not balloon.popped:
                        balloon.popped = True
            allPairs[ cur ] = [ ]
    nonePopped = True
    for balloon in lst:
        if not balloon.popped:
            nonePopped = False
            print( str( balloon ) )
    if nonePopped == True:
        print( "No balloons left unpopped." )

main()