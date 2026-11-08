import subprocess
import sys

if __name__ == "__main__":
    # اجرای دستورات جنگو بدون نیاز به فایل start.sh
    subprocess.run(["python", "manage.py", "migrate", "--noinput"])
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"])
    sys.exit(subprocess.call(["python", "-m", "gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]))