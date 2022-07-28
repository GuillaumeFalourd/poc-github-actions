import subprocess
import os

try:
    shell=os.environ['SHELL']
except Exception:
    shell = ""

if 'bash' in shell:
    result = subprocess.check_output("/c/windows/system32/wbem/wmic.exe csproduct get uuid", shell=False).strip().decode().split("\n")[1]
else:
    print(shell)
    result = subprocess.check_output("c:\\windows\\system32\\wbem\\wmic.exe csproduct get uuid", shell=False).strip().decode().split("\n")[1]

print(result)