import subprocess
import os

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def fix_conflicts():
    # 1. Update main
    print("Updating main...")
    run("git checkout main")
    run("git pull origin main")

    # 2. Get branches
    result = subprocess.run("git branch --list \"feature/*\"", shell=True, capture_output=True, text=True)
    branches = [b.strip() for b in result.stdout.split('\n') if b.strip()]

    print(f"Found branches: {branches}")

    for branch in branches:
        print(f"Fixing {branch}...")
        try:
            run(f"git checkout {branch}")
            # Merge main into feature, preferring feature's version for conflicts
            # This creates a merge commit and makes it compatible with main
            try:
                run("git merge main -m \"Sync with main to fix conflicts\" -X ours")
            except subprocess.CalledProcessError:
                # If merge failed despite -X ours (rare but possible), try to abort
                print(f"Merge failed for {branch}, aborting merge.")
                run("git merge --abort")
                continue
            
            run(f"git push origin {branch}")
            print(f"Successfully fixed {branch}")
        except Exception as e:
            print(f"Error processing {branch}: {e}")

    run("git checkout main")
    print("All done.")

if __name__ == "__main__":
    fix_conflicts()
