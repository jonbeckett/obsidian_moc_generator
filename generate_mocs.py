import os
import sys
from pathlib import Path

def get_subdir_names(dir):
    "Get a list of immediate subdirectories"
    return next(os.walk(dir))[1]

def get_subfile_names(dir):
    "Get a list of immediate subfiles"
    return next(os.walk(dir))[2]

def spider(os_path,f_path):

    subdir_names = get_subdir_names(os_path)
    for subdir_name in subdir_names:

        os_subdir_path = os.path.join(os_path,subdir_name)
        f_subdir_path = f_path + ("/" if f_path!="" else "")  + subdir_name

        spider(os_subdir_path, f_subdir_path)

        moc_content = "# " + subdir_name + " Map of Contents\n\n"
        subfile_names = get_subfile_names(os_subdir_path)
        for file_name in filter(lambda sfn: Path(sfn).suffix == ".md", subfile_names):
            moc_content += " - [[" + f_subdir_path + "/" + Path(file_name).stem + "|" + Path(file_name).stem + "]]\n"

        moc_filename = os.path.join(os_path,subdir_name + " MoC.md")
        print(moc_filename)

        with open(moc_filename, 'w') as f:
            f.write(moc_content)


if (len(sys.argv)==1):
    print("\ngenerate_mocs.py - Obsidian Map of Contents Creation Tool, by Jonathan Beckett\n\nExample : python generate_mocs.py c:\\my\\vault\\root\\folder\n\n")
    sys.exit(0)

init_path = sys.argv[1]

if not os.path.isdir(init_path):
    print("The directory (" + init_path +") does not exist")
    sys.exit(0)

spider(init_path,"")