#!/usr/bin/env python

import os

#os.system("python3 -m pytest --cov=architectures tests --cov-report xml")
os.system("<(curl -s https://codecov.io/bash) -t b7c724c3-f526-498a-9bc5-7b9df8537d37")