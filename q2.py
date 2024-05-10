#coding:UTF-8

def check_brackets(str):
    stack = []
    result = list(len(str) * ' ')
    for index, char in enumerate(str):
        if char == '(':
            stack.append((char, index))
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[index] = '?'
        else:
            result[index] = ' '

    
    while stack:
        pair = stack.pop()
        position = pair[1]
        result[position] = 'x'
    
    return str + '\n' + ''.join(result)

# 测试用例
test_cases = [
    'bge)))))))))',
    '((IIII))))))',
    '()()()()(uuu',
    '))))UUUU((()'
]

for case in test_cases:
    print(check_brackets(case))

