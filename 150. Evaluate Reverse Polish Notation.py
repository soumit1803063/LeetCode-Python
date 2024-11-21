from fastio import FastIO
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+','-','*','/']:
                num1,num2,op = stack.pop(),stack.pop(),t
                if op == "+":
                    num1= num2+num1
                elif op == "-":
                    num1= num2-num1
                elif op == "*":
                    num1= num2*num1
                elif op == "/":
                    num1= int(num2/num1)
                stack.append(num1)
            else:
                stack.append(int(t))
        return stack[0]

def main():
    # For local testing, use file-based I/O
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Use file-based I/O if files are provided; otherwise, standard I/O
    io = FastIO(input_file=input_file, output_file=output_file)

    try:
        # Read input
        data = io.readline().strip()
        res = Solution().evalRPN(data.split(","))
        print(res)
    finally:
        # Ensure resources are released
        io.flush()
        io.close()

if __name__ == "__main__":
    main()