import subprocess
import os

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {cmd}: {result.stderr}")
        raise Exception(result.stderr)
    return result.stdout.strip()

def fix_all_branches():
    # 1. Fetch everything
    print("Fetching updates...")
    run("git fetch --all")

    # 2. Get list of feature branches
    output = run("git branch --list \"feature/*\"")
    branches = [b.strip() for b in output.split('\n') if b.strip()]

    for branch in branches:
        print(f"Processing {branch}...")
        try:
            # Checkout
            run(f"git checkout {branch}")
            
            # Try to merge main
            try:
                run("git merge origin/main --no-edit")
            except Exception:
                print(f"  Conflict detected on {branch}. resolving...")
                # Conflict State!
                # Strategy: Take content from Main, and append our signature again.
                # 1. Checkout main's version of the conflicting file
                run("git checkout origin/main -- activity_log.txt")
                
                # 2. Append something unique to it
                with open("activity_log.txt", "a") as f:
                    f.write(f"\nResolved conflict for {branch}\n")
                
                # 3. Add and Continue/Commit
                run("git add activity_log.txt")
                
                # Check if we are in a merge state
                if os.path.exists(".git/MERGE_HEAD"):
                    run("git commit --no-edit")
                else:
                    run("git commit -m \"Force resolve conflict\"")

            # Push
            print(f"  Pushing {branch}...")
            run(f"git push origin {branch}")
            
        except Exception as e:
            print(f"Failed to process {branch}: {e}")
            # Abort merge if stuck to clean up for next
            subprocess.run("git merge --abort", shell=True)

    print("Checking out main...")
    subprocess.run("git checkout main", shell=True)
    print("Done.")

if __name__ == "__main__":
    fix_all_branches()
