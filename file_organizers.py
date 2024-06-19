import os
from typing import Callable, Dict, List

# TODO: change path separators


## Open and read file list
def read_links_from_file(file: str) -> Dict[str, List[str]]:
    # Open file
    f = open(file, "r", encoding="utf-8")

    try:
        lines = f.readlines()
    finally:
        f.close()

    # Sort into folder hierarchy
    siteLib: Dict[str, List[str]] = {}

    currDir = ""

    for index, line in enumerate[str](lines):
        if line.startswith("\n"):
            continue
        # Retreat in hierarchy
        if line.startswith("--"):
            if currDir == "":
                raise Exception(
                    f"Tried to regress out of base path on file line {index + 1}"
                )
            elif "/" not in currDir:
                currDir = ""

            dirParts = currDir.split("/")

            dirParts.pop()

            currDir = "/".join(dirParts)
        # Advance in hierarchy
        elif line.startswith("-"):
            # Get clean name with no unnecessary surrounding formatting
            newPart = (
                line.rstrip("\n")
                .removeprefix("-")
                .strip()
                .replace("/", "、")
                .replace("\\", "、")
                .replace(":", " -")
                .replace("@", "_at_")
                .replace("#", "_")
                .replace("?", "_")
                .replace("*", "_")
                .replace(">", "_")
                .replace("|", "、")
                .replace("<", "_")
            )

            # Add first part without leading '/' to keep the path relative
            if currDir == "":
                currDir = newPart
            else:
                currDir = os.path.join(currDir, newPart)
        # Add to hierarchy
        else:
            if currDir not in siteLib:
                siteLib[currDir] = []

            siteLib[currDir].append(line.rstrip("\n"))

    return siteLib


def iterate_on_lib(
    siteLib: Dict[str, List[str]], callback: Callable[[str, List[str]], None]
) -> None:
    for group in siteLib.items():
        callback(group[1], group[0])


# Create directoy if it doesn't exist
def create_directory(path: str):
    if path == "":
        return

    if not os.path.isdir(path):
        os.makedirs(path)
