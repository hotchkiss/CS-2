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
        for i in range( len( self.table ) ):
            self.table[ i ] = []
        self.size = 0

    def __str__( self ):
        """
           Return the entire contents of this hash table,
           one chain of entries per line.
        """
        result = ""
        for i in range( len( self.table ) ):
            for n in range( len( self.table[ i ] ) ):
                result += str( i ) + ", " + str( n ) + ": "
                result += str( self.table[ i ][ n ][ 0 ] ) + str( self.table[ i ][ n ][ 1 ] ) + "\n"
        return result

    class _Entry( object ):
        """
           A nested class used to hold key/value pairs.
           
           NEW IMPLEMENTATION DOES NOT USE THIS
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
    hashcode = hash( val ) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def keys( hTable ):
    """
       Return a list of keys in the given hashTable.
    """
    result = []
    for item in range( len( hTable.table ) ):
        if len( hTable.table[ item ]) != None:
            for n in hTable.table[ item ]:
                result.append( n )
            #result.append( entry.key )
    return result

def contains( hTable, key ):
    """
       Return True if hTable has an entry with the given key.
    """
    index = hash_function( key, len( hTable.table ) )
    for item in hTable.table[ index ]:
        for n in range( len( item ) ):
            if item[ n ] == key:
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
    if hTable.table[ index ] == [ ]:
        #If the hash table's index of key's hash is empty, make
        hTable.table[ index ].append( [ key, value ] )
    if hTable.table[ index ] != [ ]:
        for item in hTable.table[ index ]:
            if item[ 0 ] == key:
                item[ 1 ] = value
                return True
        hTable.table[ index ].append( [ key, value ] )

def get( hTable, key ):
    """
       Return the value associated with the given key in
       the given hash table.
       Precondition: contains(hTable, key)
    """
    index = hash_function( key, len( hTable.table ) )
    if hTable.table[ index ] == [ ]:
        raise Exception( "Hash table does not contain key." )
    else:
        for item in hTable.table[ index ]:
            if item[ 0 ] == key:
                return item[ 1 ]
        raise Exception( "Hash table does not contain key." )