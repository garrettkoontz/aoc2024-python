def read_file(filename: str) -> str:
    with open(filename) as f:
        s = f.read()
    return s
