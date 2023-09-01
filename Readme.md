type Data = Array<string | int32 | Data>

Yes, it's OR
both are valid inputs 

```erlang

[ entry, [ key, 24], 33, flat, [k2,99], nine,[ in, [  inner , 44 ]]].

[11, foo, [foo, 11], [in, [ deeper, [ even_deeper , 9999 ]]]].

```

[boo, 11, [bar ,32], [fa,233],]

Inspired by https://medium.com/@niamtokik/serialization-series-do-you-speak-erlang-etf-or-bert-part-1-ff70096b50c0

Compiled from ideas described here: https://www.erlang.org/doc/man/ei


```
>>> b =b'\xff'
>>> int.from_bytes(b, 'big', signed=True)
-1
>>> b =b'\x01\x00\x00'
>>> int.from_bytes(b, 'big', signed=True)
65536
>>> b =b'\xf9s\x80\xe1'
>>> int.from_bytes(b, 'big', signed=True)
-109870879
>>> b =b'\x80\x00\x00\x00\x00\x00\x00\x01'
>>> int.from_bytes(b, 'big', signed=True)
-9223372036854775807
>>> 
```
