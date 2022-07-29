import subprocess

result = subprocess.check_output("c:\\windows\\system32\\wbem\\wmic.exe csproduct get uuid", shell=False).strip().decode().split("\n")[1] #nosec

print(result)