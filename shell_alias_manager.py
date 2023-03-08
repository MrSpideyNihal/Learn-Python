"""A simple shell alias manager."""
import os

def set_alias(alias_name, command):
    """Set a shell alias."""
    if not alias_name:
        raise Exception('Alias name cannot be empty')
    if not command:
        raise Exception('Command cannot be empty')
    os.system(f'echo alias {alias_name}="{command}" >> ~/.bashrc; source ~/.bashrc')

def get_alias(alias_name):
    """Get the value of a shell alias."""
    if not alias_name:
        raise Exception('Alias name cannot be empty')
    command = os.popen(f'echo \$({alias_name})').read().strip()
    return command

if __name__ == "__main__":
    set_alias('ll', 'ls -l')
    print(get_alias('ll'))
