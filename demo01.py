"""
    字节串和字符串之间的转换
"""
while True:
    s = input("输入一个字符串")

    # str -> bytes
    s1 = s.encode()
    print("对应的字节串为:", s1)
    #所有的字符串都能转换为字节串,但是所有的字节串不能转换为字符串
    # bytes -> str
    s = s1.decode()
    print("对应的字符串为:", s)
