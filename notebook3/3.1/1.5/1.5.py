def load_config(filename):
    with open(filename, 'r') as f:
        code = f.read()
    exec(code)


if __name__ == '__main__':
    load_config('hello.py')
