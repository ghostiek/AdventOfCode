import re


def get_dir_sizes(txt):
    logged_dirs = {}
    current_dir = ""
    for i in txt:
        # We have an instruction
        if i.startswith("$"):
            if "$ cd" in i:
                matches = re.match(r"^\$ cd (.*)$", i)
                grp = matches.group(1)
                if grp == "/":
                    # Start at root
                    current_dir = ""
                elif grp == "..":
                    dirs = current_dir.split("/")[:-1]
                    current_dir = "/".join(dirs)
                else:
                    # Append to dir
                    current_dir += "/" + grp
        # Read result
        else:
            matches = re.match(r"^(\d+)", i)
            if matches is not None:
                size = matches.group(1)
                directories = current_dir.split("/")
                for dir_idx in range(len(directories)):
                    directory = "/".join(directories[:dir_idx+1])
                    logged_dirs[directory] = logged_dirs.get(directory, 0) + int(size)
    return logged_dirs