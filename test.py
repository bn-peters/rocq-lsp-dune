#!/usr/bin/env python3

import sys
from pathlib import Path

from pytanque import Pytanque, PytanqueMode


file_path = Path(sys.argv[1] if len(sys.argv) > 1 else "token_logrel/temp.v").resolve()

with Pytanque(mode=PytanqueMode.STDIO) as client:
    client.set_workspace(debug=False, dir=str(Path(".").resolve()))
    toc = client.toc(str(file_path))

for name, _ in toc:
    print(name)
