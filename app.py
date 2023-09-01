from pympler.asizeof import asizeof
import zlib
import sys
from math import log

from pprint import pprint

MAX_STRING_LENGTH=1000000

MAX_ARRAY_SIZE=1000

from pympler.asizeof import asizeof

def byte_length(i):
    if i == 0:
         return 1
    return (i.bit_length() + 7) // 8

def encode_int32(stream: bytearray, value: int, value_pointer=3):
    #pprint(value)
    #pprint(value_pointer)
    if value > sys.maxsize:
        raise Exception('value > sys.maxsize') 
    int_length_in_bytes_= byte_length(value)
    #pprint(int_length_in_bytes_)
    stream.extend(bytes(2 + int_length_in_bytes_ ))
    #pprint(stream)
    stream_raw= memoryview(stream)
    stream_raw[value_pointer:value_pointer+1]= b'i'
    value_pointer= value_pointer + 1
    #pprint(stream)
    stream_raw[value_pointer:value_pointer+1]= int_length_in_bytes_.to_bytes()
    # should be one byte for int32 length in bytes
    #pprint(stream)
    value_pointer= value_pointer + 1
    stream_raw[value_pointer:value_pointer + int_length_in_bytes_]= value.to_bytes(int_length_in_bytes_, signed=True)
    value_pointer= value_pointer + int_length_in_bytes_
    return stream, value_pointer # return pointer to next byte after the value bytes

def decode_int32(stream_bytes: bytearray, i_marker_pointer=3):
    #pprint(stream_bytes)
    stream_raw= memoryview(stream_bytes)
    length_in_bytes= stream_raw[i_marker_pointer+1:i_marker_pointer+2]
    of_bytes_of_length= int.from_bytes(length_in_bytes, 'big')
    #pprint(of_bytes_of_length)
    value_in_bytes= stream_raw[i_marker_pointer+2:i_marker_pointer+2+of_bytes_of_length]
    #pprint(value_in_bytes.tobytes())
    return int.from_bytes(value_in_bytes, 'big', signed=True), i_marker_pointer+2+of_bytes_of_length # pointer to next marker



buf_ = bytearray(b'V1[')
integers= [-1,1,sys.maxsize,65536,-109870879,-sys.maxsize]
pprint(integers)
pprint("Memory size of list:")
pprint(asizeof(integers))
pointer_to_the_end_of_stream=3
for an_int32 in integers:
    buf_, pointer_to_the_end_of_stream= encode_int32(buf_,an_int32,value_pointer=pointer_to_the_end_of_stream)
    #pprint('stream')
    #pprint(buf_)
    #pprint(pointer_to_the_end_of_stream)
#buf_, pointer_to_the_end_of_stream= encode_int32(buf_,1,value_pointer=pointer_to_the_end_of_stream)
#pprint(pointer_to_the_end_of_stream)
#pprint('stream')
#pprint(buf_)
#buf_, pointer_to_the_end_of_stream= encode_int32(buf_,sys.maxsize,value_pointer=pointer_to_the_end_of_stream)
#pprint(pointer_to_the_end_of_stream)
#pprint('stream')
#pprint(buf_)
#buf_, pointer_to_the_end_of_stream= encode_int32(buf_,65536,value_pointer=pointer_to_the_end_of_stream)
#pprint(pointer_to_the_end_of_stream)
#pprint('stream')
#pprint(buf_)
#buf_, pointer_to_the_end_of_stream= encode_int32(buf_, -109870879, value_pointer=pointer_to_the_end_of_stream)
#pprint(pointer_to_the_end_of_stream)
#pprint('stream')
#pprint(buf_)
#buf_, pointer_to_the_end_of_stream= encode_int32(buf_,-sys.maxsize, value_pointer=pointer_to_the_end_of_stream)
#pprint(pointer_to_the_end_of_stream)
#pprint('stream final..')

m = memoryview(buf_)
b= m.tobytes()
pprint("Memory size of encoded buffer ")
pprint(asizeof(b))
pprint(b)

unpacked_int23z= []
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=3)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=next_marker_pointer)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=next_marker_pointer)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=next_marker_pointer)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=next_marker_pointer)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
an_int32, next_marker_pointer= decode_int32(b, i_marker_pointer=next_marker_pointer)
unpacked_int23z.append(an_int32)
#pprint({"an_int32":an_int32})
#pprint({"next_marker_pointer":next_marker_pointer})
pprint(unpacked_int23z)

same= integers == unpacked_int23z
pprint("are lists the same?")
pprint(same)
#b= b'V1[i\x01\xffi\x01\x01i\x08\x7f\xff\xff\xff\xff\xff\xff\xffi\x03\x01\x00\x00i\x04\xf9s\x80\xe1i\x08\x80\x00\x00\x00\x00\x00\x00\x01'
