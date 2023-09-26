# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


import time

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    p = 0
    # m 0: auto 1: on 2: off
    m = 0
    encStart = "<!encrypt>"
    encEnd = "</encrypt>"
    encSELength = len(encStart)
    print("1: 加密")
    print("2: 解密")
    print("0: 退出")
    while True:
        p = int(input("请输入操作模式: "))
        if p == 0:
            print("Bye")
            break

        if p != 1 and p != 2:
            print("您的输入有误，请重新输入。")
        s = ''
        length = 0
        result = ''

        if p == 1:
            s = input("请输入需要加密的文本: ")
            length = len(s)
            print(f'文本长度: {length}')
            print('正在加密...')
            time.sleep(0.3)
            result = encStart
            for c in s:
                res = chr(ord(c) + 3)
                result += res
                if m == 0 and length <= 300 or m == 1:
                    print(f'{c}: {res}')

            print('加密完成! ')
            result += encEnd
            print(f'结果: {result}')

        elif p == 2:
            s = input("请输入需要解密的文本: ")
            length = len(s)
            if s[:encSELength] != encStart or s[-encSELength:] != encEnd:
                print('注意：这个文本好像没有被加密! ')
                tmp = input('仍然加密请输入 \'continue\' ')
                if tmp != 'continue':
                    continue
            else:
                s = s[encSELength:-encSELength]
            depth = 1
            print(f'文本长度: {length}')
            print('正在解密...')
            time.sleep(0.3)
            result = ""

            for c in s:
                res = chr(ord(c) - 3)
                result += res
                if m == 0 and length <= 300 or m == 1:
                    print(f'{c}: {res}')

            while result[:encSELength] == encStart and result[-encSELength:] == encEnd:
                print('连环加密: 存在')
                depth += 1
                print(f'当前深度: {depth}')
                t = ""
                for c in result:
                    c = chr(ord(c) - 3)
                    t += c
                result = t
                result = result[encSELength:-encSELength]

            print('解密完成! ')
            print(f'结果: {result}')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
