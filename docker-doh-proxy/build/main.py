import subprocess

subprocess.run(["pip", "install", "doh-proxy"], check=True)
requirements = subprocess.check_output(["pip", "freeze"])
with open("/root/requirements.txt", "wb") as file:
    file.write(requirements)
