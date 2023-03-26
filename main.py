def generate_text(length: int, _path: str) -> bool:
    """generates the letter A length times and writes to file
    
    Returns true on success.
    
    """
    with open(_path, "w") as _file:
        _file.write("A" * length)
        return True


if __name__ == "__main__":
    generate_text(1200, "./temp_file.txt")
