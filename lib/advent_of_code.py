def open_file(filename)-> list[str]:
    with open(filename) as f:
        return(f.readlines())