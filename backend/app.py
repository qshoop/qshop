import subprocess
import sys

if __name__ == "__main__":
    # اجرای فایل start.sh با استفاده از bash
    sys.exit(subprocess.call(["bash", "start.sh"]))