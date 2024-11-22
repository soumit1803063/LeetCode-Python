from fastio import FastIO
from typing import List
class Solution:
    def expression_in_list(self,expr: str)->List[str]:
        number = ''
        expression = ['(']
        prev='('
        for e in expr:
            if e in ['+','-','*','/','(',')']:
                if number:
                    expression.append(number)
                    number = ''
                if prev=='(' and e == '-':
                    expression.append('u')
                else:
                    expression.append(e)
            elif e == ' ':
                continue
            else:
                number += e
            prev = e
        if number:
            expression.append(number)
        expression.append(')')
        return expression
    
    def operation(self,num1,num2,op):
        if op=='u':
            return -num1
        if op=='+':
            return num2+num1
        if op=='-':
            return num2-num1
        if op=='*':
            return num2*num1
        if op=='/':
            return int(num2/num1)
        
    def precedence(self,op):
        if op == ')':
            return 0
        if op in ['+','-']:
            return 1
        if op in ['*','/']:
            return 2
        if op == 'u':
            return 3
        if op == '(':
            return -1
         

    def calculate(self, s: str) -> int:
        expression = self.expression_in_list(expr=s)
        operators =[]
        numbers = []
        for e in expression:
            if e in ['(','u']:
                operators.append(e)
            elif e in [')','+','-','*','/']:
                while(self.precedence(e)<=self.precedence(operators[-1])):
                    op = operators.pop()
                    num1 = numbers.pop()
                    num2 = 0
                    if op != 'u':
                        num2 = numbers.pop()
                    num1 = self.operation(num1,num2,op)
                    numbers.append(num1)
                if e == ')':
                    operators.pop()
                else:
                    operators.append(e)
            else:
                numbers.append(int(e))


        return numbers.pop()

def main():
    # For local testing, use file-based I/O
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Use file-based I/O if files are provided; otherwise, standard I/O
    io = FastIO(input_file=input_file, output_file=output_file)

    try:
        # Read input
        data = io.readline().strip()
        print(Solution().calculate(data))
    finally:
        # Ensure resources are released
        io.flush()
        io.close()

if __name__ == "__main__":
    main()