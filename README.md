# Obsidian Map of Content Generator

This is a python 3 script that automatically creates Map of Content markdown files for a directory tree full of markdown files.

It generates a file called "folder name MoC.md" alongside each folder. Within each MoC file is the title of the folder, and links to each markdown file within the folder.

The script iterates through every folder below the passed in folder name, generating maps of content as it goes. Beware that if you already have maps of content named after sibling folders, they will get over-written.

Example:

```python generate_mocs.py c:\my\vault```

You can of course run the script as many times as needed - it will just over-write the MoCs it has generated each time.

Note that the links are written in the "Obsidian way" - with pure folder and filenames used to make the paths

*Warning - if you have spaces on the end of any filenames, it will break the links in Obsidian - so be careful to clean your filenames up beforehand - there are a number of great free bulk filename tools around.*
