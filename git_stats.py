"""Calculate and display git diff stats."""
import subprocess
import re

def get_diff_stats(commit):
    """Get the diff statistics for the given commit."""
    process = subprocess.Popen(['git', 'diff', f'{commit}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return None
    lines = [line.strip() for line in output.decode().split('\n')]
    added = 0
    removed = 0
    modified = 0
    for line in lines[1:]:
        match = re.match(r'([+-]) (.*)', line)
        if match:
            action, file = match.groups()
            if action == '+':
                added += 1
            elif action == '-':
                removed += 1
            else:
                modified += 1
    return {'added': added, 'removed': removed, 'modified': modified}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python git_stats.py <commit>")
        sys.exit(1)
    commit = sys.argv[1]
    stats = get_diff_stats(commit)
    if stats:
        print(f"Commit {commit} stats:\nAdded: {stats['added']}\nRemoved: {stats['removed']}\nModified: {stats['modified']}")
    else:
        print(f"Error: Unable to retrieve stats for commit {commit}")
