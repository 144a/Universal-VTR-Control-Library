import subprocess

def regenerate_requirements():
    subprocess.run(['pipreqs', '.', '--force'])

if __name__ == "__main__":
    regenerate_requirements()