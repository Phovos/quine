import subprocess
import sys
import os

# Repository URL
REPO_URL = "https://github.com/PHOVOS/quine.git"

quine_template = '''import subprocess
import sys
import os

# Repository URL
REPO_URL = {repo_url}

quine_template = {source_code}

def git_pull():
    stash_result = subprocess.run(['git', 'stash', 'push', '-m', 'Quine temporary stash'], capture_output=True, text=True)
    if stash_result.returncode != 0:
        return False

    pull_result = subprocess.run(['git', 'pull', '--rebase', 'origin', 'master'], capture_output=True, text=True)
    if pull_result.returncode != 0:
        subprocess.run(['git', 'stash', 'pop'], capture_output=True, text=True)  # Ensure we don't lose our changes
        return False

    pop_result = subprocess.run(['git', 'stash', 'pop'], capture_output=True, text=True)
    return pop_result.returncode == 0 and pull_result.returncode == 0

def git_commit():
    with open(__file__, 'w') as f:
        f.write(quine_template.format(repo_url=repr(REPO_URL), source_code=repr(quine_template)))

    add_result = subprocess.run(['git', 'add', __file__], capture_output=True, text=True)
    if add_result.returncode != 0:
        sys.exit(f"Failed to add file to git: {add_result.stderr}")

    commit_result = subprocess.run(['git', 'commit', '-m', 'Update quine at runtime'], capture_output=True, text=True)
    if commit_result.returncode != 0:
        sys.exit(f"Failed to commit changes: {commit_result.stderr}")

    push_result = subprocess.run(['git', 'push', '--set-upstream', 'origin', 'master'], capture_output=True, text=True)
    if push_result.returncode != 0:
        sys.exit(f"Failed to push changes: {push_result.stderr}")

def initialize_repo():
    if not os.path.exists('.git'):
        init_result = subprocess.run(['git', 'init'], capture_output=True, text=True)
        if init_result.returncode != 0:
            sys.exit(f"Failed to initialize git repository: {init_result.stderr}")

        remote_add_result = subprocess.run(['git', 'remote', 'add', 'origin', REPO_URL], capture_output=True, text=True)
        if remote_add_result.returncode != 0:
            sys.exit(f"Failed to add remote: {remote_add_result.stderr}")

        pull_result = subprocess.run(['git', 'pull', '--allow-unrelated-histories', 'origin', 'master'], capture_output=True, text=True)
        if pull_result.returncode != 0:
            sys.exit(f"Failed to pull from remote repository: {pull_result.stderr}")

        git_commit()
    else:
        branch_result = subprocess.run(['git', 'checkout', '-B', 'master'], capture_output=True, text=True)
        if branch_result.returncode != 0:
            sys.exit(f"Failed to create and switch to master branch: {branch_result.stderr}")

        remote_add_result = subprocess.run(['git', 'remote', 'add', 'origin', REPO_URL], capture_output=True, text=True)
        if remote_add_result.returncode != 0 and "already exists" not in remote_add_result.stderr:
            sys.exit(f"Failed to add remote: {remote_add_result.stderr}")

        set_upstream_result = subprocess.run(['git', 'branch', '--set-upstream-to=origin/master', 'master'], capture_output=True, text=True)
        if set_upstream_result.returncode != 0:
            sys.exit(f"Failed to set upstream branch: {set_upstream_result.stderr}")

def quine():
    if not git_pull():
        sys.exit("Failed to pull from remote repository. Please check your network connection and repository permissions.")
    
    print(quine_template.format(repo_url=repr(REPO_URL), source_code=repr(quine_template)))
    git_commit()

if __name__ == "__main__":
    initialize_repo()
    quine()
'''

def git_pull():
    stash_result = subprocess.run(['git', 'stash', 'push', '-m', 'Quine temporary stash'], capture_output=True, text=True)
    if stash_result.returncode != 0:
        return False

    pull_result = subprocess.run(['git', 'pull', '--rebase', 'origin', 'master'], capture_output=True, text=True)
    if pull_result.returncode != 0:
        subprocess.run(['git', 'stash', 'pop'], capture_output=True, text=True)  # Ensure we don't lose our changes
        return False

    pop_result = subprocess.run(['git', 'stash', 'pop'], capture_output=True, text=True)
    return pop_result.returncode == 0 and pull_result.returncode == 0

def git_commit():
    with open(__file__, 'w') as f:
        f.write(quine_template.format(repo_url=repr(REPO_URL), source_code=repr(quine_template)))

    add_result = subprocess.run(['git', 'add', __file__], capture_output=True, text=True)
    if add_result.returncode != 0:
        sys.exit(f"Failed to add file to git: {add_result.stderr}")

    commit_result = subprocess.run(['git', 'commit', '-m', 'Update quine at runtime'], capture_output=True, text=True)
    if commit_result.returncode != 0:
        sys.exit(f"Failed to commit changes: {commit_result.stderr}")

    push_result = subprocess.run(['git', 'push', '--set-upstream', 'origin', 'master'], capture_output=True, text=True)
    if push_result.returncode != 0:
        sys.exit(f"Failed to push changes: {push_result.stderr}")

def initialize_repo():
    if not os.path.exists('.git'):
        init_result = subprocess.run(['git', 'init'], capture_output=True, text=True)
        if init_result.returncode != 0:
            sys.exit(f"Failed to initialize git repository: {init_result.stderr}")

        remote_add_result = subprocess.run(['git', 'remote', 'add', 'origin', REPO_URL], capture_output=True, text=True)
        if remote_add_result.returncode != 0:
            sys.exit(f"Failed to add remote: {remote_add_result.stderr}")

        pull_result = subprocess.run(['git', 'pull', '--allow-unrelated-histories', 'origin', 'master'], capture_output=True, text=True)
        if pull_result.returncode != 0:
            sys.exit(f"Failed to pull from remote repository: {pull_result.stderr}")

        git_commit()
    else:
        branch_result = subprocess.run(['git', 'checkout', '-B', 'master'], capture_output=True, text=True)
        if branch_result.returncode != 0:
            sys.exit(f"Failed to create and switch to master branch: {branch_result.stderr}")

        remote_add_result = subprocess.run(['git', 'remote', 'add', 'origin', REPO_URL], capture_output=True, text=True)
        if remote_add_result.returncode != 0 and "already exists" not in remote_add_result.stderr:
            sys.exit(f"Failed to add remote: {remote_add_result.stderr}")

        set_upstream_result = subprocess.run(['git', 'branch', '--set-upstream-to=origin/master', 'master'], capture_output=True, text=True)
        if set_upstream_result.returncode != 0:
            sys.exit(f"Failed to set upstream branch: {set_upstream_result.stderr}")

def quine():
    if not git_pull():
        sys.exit("Failed to pull from remote repository. Please check your network connection and repository permissions.")
    
    print(quine_template.format(repo_url=repr(REPO_URL), source_code=repr(quine_template)))
    git_commit()

if __name__ == "__main__":
    initialize_repo()
    quine()
