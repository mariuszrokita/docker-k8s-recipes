import os
import pwd


def main():
    print("Running python application...")
    print("CWD:", os.getcwd())
    print("UID:", os.getuid())
    print("GID:", os.getgid())
    print("UserName:", pwd.getpwuid(os.getuid())[0])


if __name__ == '__main__':
    main()
