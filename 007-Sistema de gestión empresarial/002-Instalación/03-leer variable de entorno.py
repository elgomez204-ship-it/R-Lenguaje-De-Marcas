# En el shell (terminal):
# echo 'export NOMBRE="JUAN PATINO"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))