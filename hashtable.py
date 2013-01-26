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
    hashcode = hash( val ) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def keys( hTable ):
    """
       Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append( entry.key )
    return result

def contains( hTable, key ):
    """
       Return True iff hTable has an entry with the given key.
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            return False
    return hTable.table[ index ] != None

def put( hTable, key, value ):
    """
       Using the given hash table, set the given key to the
       given value. If the key already exists, the given value
       will replace the previous one already in the table.
       If the table is full, an Exception is raised.
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            raise Exception( "Hash table is full." )
    if hTable.table[ index ] == None:
        hTable.table[ index ] = HashTable._Entry( key, value )
        hTable.size += 1
    else:
        hTable.table[ index ].value = value
    return True

def get( hTable, key ):
    """
       Return the value associated with the given key in
       the given hash table.
       Precondition: contains(hTable, key)
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            raise Exception( "Hash table does not contain key." )
    if hTable.table[ index ] == None:
        raise Exception( "Hash table does not contain key." )
    else:
        return hTable.table[ index ].value