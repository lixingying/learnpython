#利用切片操作，实现一个trim()函数，去除字符串首尾的所有空格
def trim(s):
    if s=='':
        return s
    while s[0]== ' ':
        s=s[1:len(s)]
        if s=='':
            return s
    while s[len(s)-1]==' ':
        s=s[0:len(s)-1]
    return s
