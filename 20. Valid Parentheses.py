from fastio import FastIO
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')':'(',
            '}':'{',
            ']':'['}
        for p in s:
            if p in ['(','{','[']:
                stack.append(p)
            else:
                if len(stack) == 0 or stack[-1] != mp[p]:
                    return False
                else:
                    stack.pop()
        return not bool(len(stack))

def main():
    # For local testing, use file-based I/O
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Use file-based I/O if files are provided; otherwise, standard I/O
    io = FastIO(input_file=input_file, output_file=output_file)

    try:
        # Read input
        data = io.readline().strip()

        res = str(Solution().isValid(data))
        io.write(res)
    finally:
        # Ensure resources are released
        io.flush()
        io.close()

if __name__ == "__main__":
    main()