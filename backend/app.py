import subprocess
import sys

if __name__ == "__main__":
    sys.exit(subprocess.call(["python", "-m", "gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]))