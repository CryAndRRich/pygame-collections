import math

def Calculate(text, isRadian):
    nums = '0123456789.'
    ops = '+-x/%^()E'
    tri_log = 'cglts' 
    
    text += 'E'
    stack = []
    temp = ''
    for i in range(len(text)):
        char = text[i]
        if char in nums:
            temp += char

        elif char in ops:
            if temp:
                prev = stack.pop() if stack else '+'
                num = float(temp)
                if prev == '+':
                    stack.append(num)
                elif prev == '-':
                    stack.append(-num)
                elif prev == 'x':
                    stack[-1] *= num
                elif prev == '/':
                    stack[-1] /= num
                elif prev == '%':
                    stack[-1] %= num
                elif prev == '^':
                    stack[-1] **= num
                elif prev == '(':
                    stack.append(prev)
                    stack.append(num)

            temp = ''
            if char != 'E':
                stack.append(char)

        elif char in tri_log:
            if char == 's' and stack and stack[-1] == 'c':
                continue
            if char == 'g' and stack[-1] == 'l':
                stack.pop()

            stack.append(char)
        
        elif char == '!':
            try:
                temp = str(math.factorial(int(temp)))
            except:
                return "ERROR"
        
        elif char == 'e':
            temp = '2.71828182846'

        if stack and stack[-1] == ')':
            stack.pop()
            num = 0
            while stack[-1] != '(':
                num += stack.pop()
            stack.pop()
            if stack[-1] in tri_log:
                prev = stack.pop()
                if prev == 's':
                    num = math.sin(num * math.pi / 180 if not isRadian else num)
                elif prev == 'c':
                    num = math.cos(num * math.pi / 180 if not isRadian else num)
                elif prev == 't':
                    num = math.tan(num * math.pi / 180 if not isRadian else num)
                elif prev == 'l':
                    num = math.log(num)
                else:
                    num = math.log10(num)
            
            temp = str(num)
        
        #print(stack)
    
    ans = sum(stack)
    return ans if ans != int(ans) else int(ans)
