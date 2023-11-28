import subprocess
import webbrowser
import os


def check_and_install_dependencies():
    # Check for Python and Pip, install Django and other dependencies
    print("Installing dependencies...")
    subprocess.run(["sudo", "pip", "install", "django"], check=True)
    subprocess.run(["sudo", "pip", "install", "requests"], check=True)


def setup_directories():
    print("Setting up directory...")
    directory = "/var/lib/greenmind"
    if not os.path.exists(directory):
        os.makedirs(directory, mode=0o700)


def start_django_server():
    subprocess.Popen(["sudo", "python", "/piauth/manage.py", "runserver"])


def open_browser():
    print("Opening browser...")
    webbrowser.open("http://localhost:8000")


def main():
    check_and_install_dependencies()
    setup_directories()
    start_django_server()
    open_browser()


if __name__ == "__main__":
    main()
