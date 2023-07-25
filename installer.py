import subprocess
import main

requirementsFile = "requirements.txt"

def installRequiredPackages():
    try:
        subprocess.check_call(["pip", "install", "-r", requirementsFile])
        print("Required packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing packages: {e}")
        exit(1)

installRequiredPackages()

#pip install -r requirements.txt
