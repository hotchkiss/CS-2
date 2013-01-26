""" 
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout 
author: jeh@cs.rit.edu James Heliotis 
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: hotchkiss@rit.edu Collin Hotchkiss
description: open addressing Hash Table for CS 242 Lecture
"""

class HashTable( object ):
    """
       The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
    """

    __slots__ = ( "table", "size" )

    def __init__( self, capacity=100 ):
        """
           Create a hash table.
           The capacity parameter determines its initial size.
        """
        self.table = [ None ] * capacity
        for i in range( capacity ):
            self.table[ i ] = []
        self.size = 0

    def __str__( self ):
        """
           Return the entire contents of this hash table,
           one chain of entries per line.
        """
        result = ""
        for i in range( len( self.table ) ):
            result += str( i ) + ": "
            result += str( self.table[i] ) + "\n"
        return result

    class _Entry( object ):
        """
           A nested class used to hold key/value pairs.
        """

        __slots__ = ( "key", "value" )

        def __init__( self, entryKey, entryValue ):
            self.key = entryKey
            self.value = entryValue

        def __str__( self ):
            return "(" + str( self.key ) + ", " + str( self.value ) + ")"

def hash_function( val, n ):
    """
       Compute a hash of the val string that is in [0 ... n).
    """
    #hashcode = ( len( val ) % n )
    num = len( val )
    hashcode = ( ( num + 23 ) * ( num + 29 ) ) % n
    return hashcode

def keys( hTable ):
    """
       Return a list of keys in the given hashTable.
    """
    result = []
    for item in hTable.table:
        if item != []:
            for entry in item:
                result.append( entry.key )
    return result

def contains( hTable, key ):
    """
       Return True iff hTable has an entry with the given key.
    """
    index = hash_function( key, len( hTable.table ) )
    lst = hTable.table[ index ]
    for i in lst:
        if i.key == key:
            return True
    return False

def put( hTable, key, value ):
    """
       Using the given hash table, set the given key to the
       given value. If the key already exists, the given value
       will replace the previous one already in the table.
       If the table is full, an Exception is raised.
    """
    index = hash_function( key, len( hTable.table ) )
    if hTable.table[ index ] == []:
        hTable.table[ index ] = [ HashTable._Entry( key, value ) ]
        hTable.size += 1
    else:
        for i in range( len( hTable.table[ index ] ) ):
            if hTable.table[ index ][ i ].key == key:
                hTable.table[ index ][ i ].value = value
                return True
        hTable.table[ index ].append( HashTable._Entry( key, value ) )
    return True

def get( hTable, key ):
    """
       Return the value associated with the given key in
       the given hash table.
       Precondition: contains(hTable, key)
    """
    index = hash_function( key, len( hTable.table ) )
    if hTable.table[ index ] == []:
        raise Exception( "Hash table does not contain key." )
    else:
        lst = hTable.table[ index ]
        for i in lst:
            if i.key == key:
                return i.value
        raise Exception( "Hash table does not contain key." )

def imbalance( hTable ):
    """
        Compute average length of all non-empty chains
        preconditions: none
    """
    numOfChains = 0
    sum = 0
    for i in range( len( hTable.table ) ):
        if hTable.table[ i ] != []:
            sum += len( hTable.table[ i ] )
            #print( sum )
            numOfChains += 1
            #print( numOfChains )
            #print( len( hTable.table[ i ] ) )
    avg =  sum / numOfChains
    return ( avg - 1 )