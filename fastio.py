import sys
from typing import Optional
import os

class FastIO:
    def __init__(self, input_file: Optional[str] = None, output_file: Optional[str] = None):
        """
        Initialize FastIO class.
        
        If input_file and output_file are provided, use them for file-based I/O.
        Automatically create the output file if it does not exist.
        Otherwise, use sys.stdin and sys.stdout for standard I/O.
        """
        self.use_file = input_file is not None and output_file is not None
        if self.use_file:
            # Open input file for reading
            if not os.path.exists(input_file):
                raise FileNotFoundError(f"Input file '{input_file}' not found.")
            self.input = open(input_file, 'r')
            
            # Create output file if it doesn't exist
            self.output = open(output_file, 'w')
        else:
            self.input = sys.stdin
            self.output = sys.stdout
        self._read_buffer = ''
        self._write_buffer = []

    def read(self) -> str:
        """Read input efficiently."""
        if self.use_file:
            return self.input.read()
        else:
            return sys.stdin.read()

    def readline(self) -> str:
        """Read a single line of input efficiently."""
        if self.use_file:
            if not self._read_buffer:
                self._read_buffer = self.input.read()
            if '\n' in self._read_buffer:
                line, self._read_buffer = self._read_buffer.split('\n', 1)
                return line + '\n'
            else:
                line, self._read_buffer = self._read_buffer, ''
                return line
        else:
            return sys.stdin.readline()

    def write(self, s: str) -> None:
        """Write output efficiently."""
        if self.use_file:
            self._write_buffer.append(s)
        else:
            sys.stdout.write(s)

    def flush(self) -> None:
        """Flush the output buffer."""
        if self.use_file:
            self.output.write(''.join(self._write_buffer))
            self.output.flush()
            self._write_buffer = []
        else:
            sys.stdout.flush()

    def close(self) -> None:
        """Close file handles if file I/O is used."""
        if self.use_file:
            self.input.close()
            self.output.close()
