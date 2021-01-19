#!/usr/bin/env python

# import os
# import subprocess as sp
# import requests
# res = requests.get('https://stackoverflow.com/questions/26000336')

# os.system("python3 -m pytest --cov=architectures tests --cov-report xml")
#os.system("bash curl -s https://codecov.io/bash -t b7c724c3-f526-498a-9bc5-7b9df8537d37")

# os.system('openssl req -nodes -newkey rsa:2048 -sha256 -keyout mynode.key -out mynode.csr -subj "/C=US/ST=Florida/L=St Petersburg/O=MyCompany/OU=MyOU/CN=mynode/emailAddress=administrators@my.com" -reqexts OPTS -config <(cat /etc/pki/tls/openssl.cnf <(printf "[OPTS]\  basicConstraints = CA:FALSE  subjectAltName = DNS:mynode,DNS:myf5  keyUsage = digitalSignature, keyEncipherment  extendedKeyUsage = serverAuth, clientAuth"))')

# { cat /etc/pki/tls/openssl.cnf;
#   printf "[OPTS]\  basicConstraints = CA:FALSE  subjectAltName = DNS:mynode,DNS:myf5  keyUsage = digitalSignature, keyEncipherment  extendedKeyUsage = serverAuth, clientAuth";
# } | openssl req -nodes -newkey rsa:2048 -sha256 -keyout mynode.key -out mynode.csr -subj "/C=US/ST=Florida/L=St Petersburg/O=MyCompany/OU=MyOU/CN=mynode/emailAddress=administrators@my.com" -reqexts OPTS -config -