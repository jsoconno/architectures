#!/usr/bin/env python

import os

#os.system("python3 -m pytest --cov=architectures tests --cov-report xml")
os.system("bash <(curl -s https://codecov.io/bash) -t TOKEN")