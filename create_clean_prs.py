import subprocess
import random

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def reset_and_create_conflict_free():
    print("Switching to main...")
    run("git checkout main")
    run("git pull origin main")

    # 1. Clean up old branches (optional, but good for hygiene)
    # We won't delete remote branches to avoid errors if they are already closed, 
    # but we will just ignore them and create NEW unique names.

    # 2. Create 5 NEW conflict-free branches
    for i in range(1, 6):
        branch_name = f"feature/independent-{random.randint(10000, 99999)}"
        print(f"Creating {branch_name}...")
        
        run(f"git checkout -b {branch_name}")
        
        # Create a UNIQUE file for this branch
        filename = f"updates/update_{i}_{random.randint(100,999)}.txt"
        os.makedirs("updates", exist_ok=True)
        
        with open(filename, "w") as f:
            f.write(f"This is an independent update for branch {branch_name}.\n")
            f.write("Since this file is unique, it will NEVER conflict with others.\n")
        
        run("git add .")
        run(f"git commit -m \"Add independent feature {i}\"")
        
        print(f"Pushing {branch_name}...")
        run(f"git push origin {branch_name}")
        
        # Go back to main
        run("git checkout main")

    print("\nDONE! Created 5 new branches that are guaranteed not to conflict.")

if __name__ == "__main__":
    import os
    reset_and_create_conflict_free()
