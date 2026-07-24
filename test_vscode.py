import subprocess

print("Script started")

try:
    process = subprocess.Popen("code.cmd", shell=True)
    print("Popen succeeded")
    print("PID:", process.pid)
except Exception as e:
    print("Exception:", repr(e))

print("Script finished")