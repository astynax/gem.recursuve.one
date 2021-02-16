#!/usr/bin/env python3
from datetime import datetime
import os
import sys
from pathlib import Path


def main():
    message = ' '.join(a.strip() for a in sys.argv[1:]).strip()
    if not message:
        print('New message:')
        message = sys.stdin.read().strip()
        if not message:
            sys.exit()

    microlog = Path(sys.argv[0]).parent / '..' / 'data' / 'microlog.gmi'
    if not microlog.is_file():
        sys.exit(f'File {microlog} not found!')

    stamp = datetime.now().strftime('%Y.%m.%d %H:%M')

    buf = []
    with microlog.open() as inp:
        stream = iter(inp.readlines())
        for line in stream:
            if line.isspace():
                break
            buf.append(line)
        buf.append(f'''
### {stamp}

{message}

''')
        for line in stream:
            buf.append(line)

    with microlog.open('w') as out:
        out.writelines(buf)


if __name__ == '__main__':
    main()
