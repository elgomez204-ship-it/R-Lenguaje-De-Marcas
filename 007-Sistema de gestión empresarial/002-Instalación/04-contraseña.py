# En el shell (terminal):
# echo 'export CONTRASENA_EMPRESA="EMPRESA123$"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("CONTRASENA_EMPRESA"))