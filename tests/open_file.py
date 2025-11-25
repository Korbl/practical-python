def read_from_file(filename: str):
    with open(filename, "r") as handle:
        return handle.readlines()
