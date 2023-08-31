import zlib
import sys
from math import log
from pprint import pprint

MAX_STRING_LENGTH=1000000

MAX_ARRAY_SIZE=1000


from math import log

def bytes_needed(an_integer: int):
     if an_integer == 0:
         return 1
     return int(log(an_integer, 256)) + 1

def byte_length(i):
    return (i.bit_length() + 7) // 8

def encode_int32(stream: bytearray, value: int, value_pointer=3):
    pprint(value)
    if value > sys.maxsize:
        raise Exception('value > sys.maxsize') 
    int_length_in_bytes_= byte_length(value)
    pprint(int_length_in_bytes_)
    # bytes_of_lenth =int_length_in_bytes_.to_bytes(signed=False)
    # append bytes of marker of int in the form of "i=<int_lenth_in_bytes_>|<bytes of value>|"
    stream.extend(bytes(5 + int_length_in_bytes_ ))
    stream_raw= memoryview(stream)
    # value_pointer value: int,
    stream_raw[value_pointer:value_pointer+2]= b'i='
    value_pointer= value_pointer + 2
    pprint(stream)
    # stream.append(int_length_in_bytes_)
    stream_raw[value_pointer:value_pointer+1]= int_length_in_bytes_.to_bytes()
    # should be one byte for int32 length in bytes
    value_pointer= value_pointer + 1
    pprint(stream)
    stream_raw[value_pointer:value_pointer+1]= b'|'
    # should be one byte for int32 length in bytes
    value_pointer= value_pointer + 1
    pprint(stream)
    #pprint(int_length_in_bytes_)
    stream_raw[value_pointer:value_pointer + int_length_in_bytes_]= value.to_bytes(int_length_in_bytes_, signed=True)
    pprint(stream)
    value_pointer= value_pointer + int_length_in_bytes_
    stream_raw[value_pointer:value_pointer + 1]= b'|'
    # should be one byte for int32 length in bytes
    value_pointer= value_pointer + 1

    pprint(stream)

    #stream.append(bytes_of_lenth)
    #stream.append(b'|')
    #stream.append(int.to_bytes(int_length_in_bytes_, signed=True))
    #stream.append(b'|')
    #pprint(stream)
    return stream


buf_ = bytearray(b'V1|')
buf_= encode_int32(buf_,-1)
buf_ = bytearray(b'V1|')
buf_= encode_int32(buf_,0)
buf_ = bytearray(b'V1|')
buf_= encode_int32(buf_,1)
buf_ = bytearray(b'V1|')
#pprint(buf_)
buf_= encode_int32(buf_,sys.maxsize)
#pprint(buf_)
buf_ = bytearray(b'V1|')
buf_= encode_int32(buf_,65536)
#pprint(buf_)
buf_ = bytearray(b'V1|')
buf_= encode_int32(buf_, -109870879)
#pprint(buf_)
