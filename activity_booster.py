import os
import random
import subprocess
from datetime import datetime, timedelta
import argparse

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def git_commit(message, date_str=None):
    if date_str:
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        subprocess.run(['git', 'commit', '-m', message], env=env, check=True, shell=True)
    else:
        run_command(f'git commit -m "{message}"')

def generate_activity(num_commits, days, max_commits_per_day):
    # Ensure activity file exists
    if not os.path.exists("activity_log.txt"):
        with open("activity_log.txt", "w") as f:
            f.write("Activity Log\n")

    start_date = datetime.now() - timedelta(days=days)
    
    total_commits = 0
    for day in range(days + 1):
        current_date = start_date + timedelta(days=day)
        # Random number of commits for this day
        daily_commits = random.randint(1, max_commits_per_day)
        
        for _ in range(daily_commits):
            if total_commits >= num_commits:
                break
                
            with open("activity_log.txt", "a") as f:
                f.write(f"Commit on {current_date} - {random.randint(1, 1000)}\n")
            
            run_command("git add activity_log.txt")
            
            # Format date for git
            date_str = current_date.strftime('%Y-%m-%dT%H:%M:%S')
            git_commit(f"Update activity log {total_commits}", date_str)
            total_commits += 1
        
        if total_commits >= num_commits:
            break
            
    print(f"Generated {total_commits} commits over {days} days.")

def create_branches(num_branches):
    print(f"Creating {num_branches} branches for PR preparation...")
    for i in range(num_branches):
        branch_name = f"feature/enhancement-{random.randint(1000, 9999)}"
        run_command(f"git checkout -b {branch_name}")
        
        with open("activity_log.txt", "a") as f:
            f.write(f"\nFeature work on {branch_name}\n")
        
        run_command("git add activity_log.txt")
        run_command(f'git commit -m "Work on {branch_name}"')
        
        # Checking out main again to branch off it next time? 
        # Or just stay? better to go back to main to keep branches independent
        run_command("git checkout main")
        
        print(f"Created branch {branch_name}. Push with 'git push origin {branch_name}' to trigger network graph.")

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity Booster")
    parser.add_argument("--commits", type=int, default=10, help="Total number of commits to generate")
    parser.add_argument("--days", type=int, default=5, help="Number of days to spread activity over")
    parser.add_argument("--branches", type=int, default=0, help="Number of branches to create (for PRs)")
    
    args = parser.parse_args()
    
    # Commits
    if args.commits > 0:
        generate_activity(args.commits, args.days, 10)
        
    # Branches
    if args.branches > 0:
        create_branches(args.branches)
        
    print("\nDone. Run 'git push' to update your GitHub contribution graph.")
    if args.branches > 0:
        print("Run 'git push --all' to push all new branches.")

if __name__ == "__main__":
    main()
