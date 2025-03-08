import subprocess
import sys
import time
import discordBotInterface

VERSION_NUMBER = "2.0.0"

def getVersionNumber() -> str:
    return VERSION_NUMBER

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

with open("./requirements.txt", "r") as f:
    data = f.read().split("\n")

def main():
    print("-" * 10 + f" Computer Generated Rapid Fire III v{VERSION_NUMBER} " + "-" * 10)

    if input("Run package installation process (only needed for first use)? y/n ").strip().lower() == "y":
        print("Installing required packages\n\n")
        for d in data:
            install(d)
        time.sleep(1)
        print("\n\nSetup complete!")

    if input("Start bot? y/n ").strip().lower() == "y":
        discordBotInterface.startBot()

if __name__ == "__main__":
    main()