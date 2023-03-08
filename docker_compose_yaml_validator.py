"""A simple Docker Compose YAML file validator."""
import yaml

def validate_yaml(yaml_file_path):
    """Validate a Docker Compose YAML file."""
    try:
        with open(yaml_file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        raise Exception(f'Invalid YAML: {str(e)}')

if __name__ == "__main__":
    yaml_file_path = 'docker-compose.yml'
    print(validate_yaml(yaml_file_path))
