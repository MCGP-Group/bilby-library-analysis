import os
import subprocess

def create_conda_env():
    print("Creating Conda environment from environment.yml...")
    subprocess.run(["conda", "env", "create", "-f", "environment.yml"], check=True)

def install_kernel():
    print("Installing the Jupyter kernel for the new environment...")
    subprocess.run(["conda", "run", "-n", "gw_research_env", "python", "-m", "ipykernel", "install", "--user", "--name", "gw_research_env", "--display-name", "Python (gw_research_env)"], check=True)

def main():
    create_conda_env()
    install_kernel()

if __name__ == "__main__":
    main()
