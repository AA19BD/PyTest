def read_from_file(filename: str) -> list[str]:
    """

    @rtype: object
    """
    with open(filename, "r") as f:
        return f.readlines()


