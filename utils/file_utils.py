def read_file(path):
    filename = path.split("/")[-1]
    with open(path, "rb") as f:
        file_bytes = f.read()
    return file_bytes, filename