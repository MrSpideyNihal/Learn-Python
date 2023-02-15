"""A singleton class for managing configuration."""
import os
class ConfigManager:
    """A singleton class for managing configuration."""
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance
    def load(self) -> dict:
        """Load configuration from a file."""
        filename = 'config.ini'
        config = {}
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f:
                    key, value = line.strip().split('=')
                    config[key] = value
        return config
    def save(self, data: dict) -> None:
        """Save configuration to a file."""
        filename = 'config.ini'
        with open(filename, 'w') as f:
            for key, value in data.items():
                f.write(f'{key}={value}
')

if __name__ == '__main__':
    config = ConfigManager()
    print(config.load())
