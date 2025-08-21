#!/usr/bin/env python3
import subprocess
import os
import random
import string

def run_cmd(cmd):
    """Run a git command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{cmd}': {e}")
        return None

def create_random_content():
    """Create random content for files"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(100, 1000)))

def inflate_git_repo():
    """Inflate the git repository size by creating many commits and branches"""
    
    print("Starting git repository inflation...")
    
    # Create a temporary directory for our inflation files
    temp_dir = "git_inflation_temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Create multiple branches and make many commits
    for branch_num in range(1, 21):  # Create 20 branches
        branch_name = f"inflate-branch-{branch_num}"
        print(f"Creating branch: {branch_name}")
        
        # Create and checkout new branch
        run_cmd(f"git checkout -b {branch_name}")
        
        # Make 50 commits on this branch
        for commit_num in range(1, 51):
            # Create a temporary file with random content
            temp_file = os.path.join(temp_dir, f"temp_{branch_num}_{commit_num}.txt")
            with open(temp_file, 'w') as f:
                f.write(create_random_content())
            
            # Add and commit the file
            run_cmd(f"git add {temp_file}")
            run_cmd(f"git commit -m 'Inflation commit {commit_num} on branch {branch_name}'")
            
            # Delete the file and commit the deletion
            run_cmd(f"git rm {temp_file}")
            run_cmd(f"git commit -m 'Remove inflation file {commit_num} on branch {branch_name}'")
        
        # Go back to main branch
        run_cmd("git checkout main")
        
        # Merge the branch to create merge commits
        run_cmd(f"git merge {branch_name} --no-ff -m 'Merge inflation branch {branch_num}'")
        
        # Delete the branch
        run_cmd(f"git branch -d {branch_name}")
    
    # Clean up temporary directory
    if os.path.exists(temp_dir):
        run_cmd(f"rm -rf {temp_dir}")
    
    print("Git repository inflation completed!")

if __name__ == "__main__":
    inflate_git_repo()
