import subprocess

subprocess.run(["pip", "install", "doh-proxy"], check=True)
requirements = subprocess.check_output(["pip", "freeze"])
with open("/root/source/requirements.txt", "wb") as file:
    file.write(requirements)
subprocess.run(["cp", "--recursive", "/root/source/.", "/root/output"],
               check=True)
