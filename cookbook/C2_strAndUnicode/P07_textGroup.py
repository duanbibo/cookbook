
import re
from collections import namedtuple

'''
文本分词:对给定的字符串从左到右解析为标记流

比如将给定的字符串做分词处理，需要做的不仅仅只是匹配模式。我们还需要有某种方法来识别出模式的类型。

 例如，我们
'''



def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

    #根据每个词的特性，编译正则表达式，使用?P<group名>将他们分组，
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'

    #编译后的正则表达式，使用管道符进行拼接，使用后还正则表达式,在匹配时根据这个匹配。
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    print(master_pat)

    #使用正则对象的scanner方法扫描，返回对象，这个对象调用scanner.math方法进行完成匹配。
    # 匹配后，仍然返回当前对象，在这个对象基础上能够获取当前匹配的group名【lastgroup】，和group对的值
    # 下次就从剩余的部分开始继续扫描匹配。实现将一个字符串，多次扫描
    scanner = master_pat.scanner('foo = 42')
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)

    # 实际生成器代码

    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)
    # Produces output
    # Token(type='NAME', value='foo')
    # Token(type='WS', value=' ')
    # Token(type='EQ', value='=')
    # Token(type='WS', value=' ')
    # Token(type='NUM', value='42')
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)

    print('*'*40)

    LT = r'(?P<LT><)'
    LE = r'(?P<LE><=)'
    EQ = r'(?P<EQ>=)'
    master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
    # master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect




def generate_tokens(pat, text):
    ''' 使用具名元祖进行接收，将分词后的group和value进行获取，装入具名元祖中的字段汇总'''
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        #这里使用了生成器，每次生成一个具名元祖：组名和组对应的值
        yield Token(m.lastgroup, m.group())


if __name__ == '__main__':
    tokenize_str()


