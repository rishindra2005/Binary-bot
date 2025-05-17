import os

def load_env(env_file='.env'):
    """
    Load environment variables from .env file
    """
    try:
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                # Parse variables
                key, value = line.split('=', 1)
                os.environ[key] = value
    except FileNotFoundError:
        print(f"Warning: {env_file} file not found")

def get_env(key, default=None):
    """
    Get environment variable with a default value
    """
    return os.environ.get(key, default) 