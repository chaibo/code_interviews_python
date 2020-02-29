"""
题目：请实现一个函数用来匹配包含 '.' 和 '*' 的正则表达式。
模式中的字符 '.' 表示任意一个字符，而 '*' 表示它前面的字符可以出现任意次(含 0 次)。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串 "aaa" 与模式 "a.a" 和
"ab*ac*a" 匹配，但与 "aa.a" 和 "ab*a" 均不匹配。
"""

def match(string, pattern):
    if (string is None) or (pattern is None):
        return False

    return match_core(string, pattern, len(string), len(pattern), 0, 0)

def match_core(string, pattern, s_len, p_len, s_pos, p_pos):
    """
    正则匹配的递归调用
    :param string: 待匹配的字符串
    :param pattern: 正则表达式
    :param s_len: 字符串长度
    :param p_len: 正则表达式长度
    :param s_pos: 字符串中当前字符的位置
    :param p_pos: 正则表达式中当前字符的位置
    :return: 是否匹配
    """

    if (s_pos == s_len) and (p_pos == p_len):
        return True

    if (s_pos < s_len) and (p_pos == p_len):
        return False

    if ((p_pos + 1) < p_len) and pattern[p_pos + 1] == '*':
        if ((s_pos < s_len) and (string[s_pos] == pattern[p_pos])) \
                or ((pattern[p_pos] == '.') and (s_pos < s_len)):

                   # 与 'a*' 匹配一次、多次或零次
            return match_core(string, pattern,
                              s_len, p_len, s_pos + 1, p_pos + 2) \
                   or match_core(string, pattern,
                                 s_len, p_len, s_pos + 1, p_pos) \
                   or match_core(string, pattern,
                                 s_len, p_len, s_pos, p_pos + 2)
        else:
            # 与'a*'不匹配, 跳过
            return match_core(string, pattern, s_len, p_len, s_pos, p_pos + 2)

    if ((s_pos < s_len) and (string[s_pos] == pattern[p_pos])) \
            or ((pattern[p_pos] == '.') and (s_pos < s_len)) :
       return match_core(string, pattern, s_len, p_len, s_pos + 1, p_pos + 1)

    return False


print(match(None, None))
print(match(None, 'adf'))
print(match('adfdf', None))
print(match('',''))
print(match('aaa', 'aaa'))
print(match('aaa', 'a.a'))
print(match('aaa', 'ab*ac*a'))
print(match('aaa', 'aa.a'))
print(match('aaa', 'ab*a'))
