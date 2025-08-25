def demo():
    # BAD: exec()
    code = "print('Hello from exec!')"
    exec(code)

    # BAD: os.system()
    import os
    os.system("ls -la")

demo()
