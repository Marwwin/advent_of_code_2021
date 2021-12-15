#%%

flatten = lambda x: [subl 
                        for l in x
                        for subl in l]

def open_file(filename: str)-> list[str]:
    with open(filename) as f:
        return(f.readlines())

def create_caves_dict(filename:str)->dict[str,list[str]]:
    caves = {}
    lines  = open_file(filename)
    for line in lines:
        origin,rest = line.strip().split("-")
        if origin not in caves.keys():
            caves[origin] = []
        caves[origin].append(rest)
        if origin.isupper():
            if rest not in caves.keys():
                caves[rest] = []
            caves[rest].append(origin)
    return caves

def create_route(caves,path,current="start"):
    print(path)
    if "end" in path:
        return path
    path.append(current)

    if current in caves.keys():
        for c in caves[current]:
            if c.isupper() or c not in path:
                path = create_route(caves,path,c)

    return path
caves = create_caves_dict("test_day12.txt")
create_route(caves,[])