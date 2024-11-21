from fastio import FastIO
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path = [p for p in path.split('/') if p]
        for p in path:
            if p == '.':
                continue
            elif p== '..':
                if len(stack) !=0:
                    stack.pop()
            else:
                stack.append(p)

        return '/'+'/'.join(stack)




def main():
    # For local testing, use file-based I/O
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Use file-based I/O if files are provided; otherwise, standard I/O
    io = FastIO(input_file=input_file, output_file=output_file)

    try:
        # Read input
        data = io.readline().strip()

        res = str(Solution().simplifyPath(data))
        io.write(res)
    finally:
        # Ensure resources are released
        io.flush()
        io.close()

if __name__ == "__main__":
    main()