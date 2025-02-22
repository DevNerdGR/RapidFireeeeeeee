import subprocess
import sys
import time

VERSION_NUMBER = "1.0.0"

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

with open("./requirements.txt", "r") as f:
    data = f.read().split("\n")

def main():
    print("-" * 10 + f" Computer Generated Rapid Fire III setup v{VERSION_NUMBER} " + "-" * 10)
    print("Installing required packages\n\n")
    
    
    for d in data:
        install(d)

    time.sleep(1)
    print("\n\nSetup complete!")
    if input("Start bot? y/n ").strip().lower() == "y":
        import discordBotInterface

if __name__ == "__main__":
    main()