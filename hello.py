import os

if __name__ == "__main__":
    print("Hello, World!")
    print(os.getcwd())
    print(os.listdir())
    print(os.environ)
    print(os.environ.get("PATH"))
    print(os.environ.get("USER"))
    print(os.environ.get("HOME"))
    print(os.environ.get("SHELL"))
