# Integer Varaible Lengh Encoding Decoding


The solution uses as little memory as possible dynamically adding space to the buffer as needed
Reliably package only significant bytes of integers, uses 'i' as separator followed directly by the number of bytes occupied by the value of integer. Next are significant bytes of an integer value encoded:


```python3

[-1, 1, 9223372036854775807, 65536, -109870879, -9223372036854775807]
```

encodes into:

```python3
b'V1[i\x01\xffi\x01\x01i\x08\x7f\xff\xff\xff\xff\xff\xff\xffi\x03\x01\x00\x00i\x04\xf9s\x80\xe1i\x08\x80\x00\x00\x00\x00\x00\x00\x01'
 ```

- Inspired by https://medium.com/@niamtokik/serialization-series-do-you-speak-erlang-etf-or-bert-part-1-ff70096b50c0

- Compiled from ideas described here: https://www.erlang.org/doc/man/ei

Install deps:

`pip3 install -r deps`

Start python interpreter and import the `app`:

```
io@Igors-MacBook:~/projects/ch-code-test$ python3
Python 3.11.5 (main, Aug 24 2023, 15:23:14) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import app
[-1, 1, 9223372036854775807, 65536, -109870879, -9223372036854775807]
'Memory size of list:'
312
'Memory size of encoded buffer '
80
[-1, 1, 9223372036854775807, 65536, -109870879, -9223372036854775807]
'are lists the same?'
True
>>> 
```



## WIP

type Data = Array<string | int32 | Data>

Yes, it's OR
both are valid inputs 

```erlang

[ entry, [ key, 24], 33, flat, [k2,99], nine,[ in, [  inner , 44 ]]].

[11, foo, [foo, 11], [in, [ deeper, [ even_deeper , 9999 ]]]].

[boo, 11, [bar ,32], [fa,233],]

```
