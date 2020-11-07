#!/usr/bin/python3

# code shell adapted from https://en.bitcoin.it/wiki/Block_hashing_algorithm
#  by Steve Cole for cse433s Spring 2019
#  last revised Fall 2020

# NAME: 

# Fill in the code sections marked # YOUR CODE HERE . You may use any of the
#  utility functions contained in this file to help you.

import hashlib
import sys

### UTILITY FUNCTIONS ###

def switch_endian(hex_string):
    '''
    Takes in a string representing hex-encoded bytes (2 chars per byte)
    and returns a copy of the string with the byte ordering reversed.
    Example: converts 'a1b2c3d4' to 'd4c3b2a1' .

    @param hex_string The hex-string-encoded number to be reversed
    @return A bytewise-reversed copy of hex_string
    '''
    hex_val = bytes.fromhex(hex_string)
    rev = hex_val[::-1].hex()
    return rev

def int32_to_little_endian(n):
    '''
    Converts a 4-byte integer value to a hex-encoded string (2 chars per byte)
      in Little Endian order.
    Pads with zeroes if less than 8 chars.
    Example: converts 26 to '1a000000'

    @param n Integer to be converted
    @return Little Endian hex string version of integer
    '''
    return switch_endian('{:08x}'.format(n)) 

def int256_to_hex_str(t):
    '''
    Takes 32-byte numerical value and returns it encoded as 
      a hex-encoded string with 2 chars per byte.
    Example: takes in 33 and returns '00000..21' (64 chars total).
    Useful for printing threshold as a string.
    '''
    return '{:064x}'.format(t)

def extract_threshold(bits):
    '''
    Extracts a numerical threshold from the 'bits' field of a Bitcoin block.
    Note: 'bits' field is assumed to be a string in Little Endian order 
      (as it's shown in the Blockchain viewer for Bitcoin).

    @param bits 'bits' field of a Bitcoin block
    @return Numerical threshold encoded in the 'bits' field
    '''
    # convert hex string and reverse
    bits_be = switch_endian(bits)
    bits_num = int(bits_be, 16) 

    # extract threshold from 4-byte 'bits' field
    # exponent: MSB
    # mantissa: 3 remaining bytes 
    # threshold = mantissa * 2**(8*(exponent-3))
    e = bits_num >> 24
    m = bits_num & 0xFFFFFF
    t = m * (1 << (8 * (e - 3)))

    return t

### CORE FUNCTIONS ###

def hash_block(version, prev_hash, merkle_root, ts, bits, nonce):
    '''
    Computes the hash value for a Bitcoin block with the given parameters.
    See https://en.bitcoin.it/wiki/Block_hashing_algorithm for details
      on the Bitcoin hash algorithm.
    Note that parameters must be in Little Endian format.

    @param version Bitcoin version
    @param prev_hash Hash of previous block 
    @param merkle_root Root of Merkle tree for the block 
    @param ts Timestamp
    @param bits 'bits' field of block; encodes threshold below which hash value must be
    @param nonce 4-byte value that causes hash to be below threshold extracted from bits
    @return String representing Big Endian hex encoding of hash value
    '''
    # YOUR CODE HERE

    # Hint: don't forget to change the return value
    return None

def mine_block(version, prev_hash, merkle_root, ts, bits):
    '''
    Computes a 4-byte nonce value that will yield a valid Bitcoin block given 
      the other header values passed as parameters.
    See https://en.bitcoin.it/wiki/Block_hashing_algorithm for details
      on the Bitcoin hash algorithm.
    Note that parameters must be in Little Endian format.
    
    @param version: Bitcoin version
    @param prev_hash: Hash of previous block 
    @param merkle_root: root of Merkle tree for the block 
    @param ts: timestamp
    @param bits: Bits field of block; encodes threshold below which hash value must be
    
    @return nonce value
    '''
    # YOUR CODE HERE

    # Hint to make problem tractable: the solution nonce is between
    #  0xb0000000 and 0xc0000000.
    # Hint on formatting: depending on how you generate your nonce
    #  guess and work with hash values, you may need to convert the
    #  nonce's endian-ness and reinterpret hash values as ints and/or
    #  strings during the course of this function.

    # Hint: don't forget to change the return value
    return None

if __name__ == "__main__":
    # main function: set up block parameters and call hash_block() or
    #  mine_block()

    # YOUR CODE HERE
    print('Nothing implemented yet.')
