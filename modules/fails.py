from modules import terminal

fails = []

def add_fail(file):
    terminal.print_red("failed: " + file)
    fails.append(file)

def add_fails(files):
    for file in files:
        add_fail(file)
