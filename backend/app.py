import os
import subprocess

if __name__ == "__main__":
    # اجرای فایل start.sh که کارهای migrate و gunicorn رو انجام می‌ده
    os.chmod("start.sh", 0o755)
    subprocess.run(["./start.sh"])