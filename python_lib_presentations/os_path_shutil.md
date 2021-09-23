# The `os.path` module

## Working with filepaths

* `os.path.basename`: Returns the last part of a filepath, e.g. /usr/bin/python3 -> python3
* `os.path.dirname`: Returns all but the last part of a filepath, e.g. /usr/bin/python3 -> /usr/bin
* `os.path.split`: Returns the dirname and basename of a path in a tuple, e.g. /usr/bin/python3 -> ('/usr/bin', 'python3')
* `os.path.abspath`: Converts a relative path to an absolute one, e.g. Python/astro2 -> /home/david/Python/astro2
* `os.path.expanduser`: Expands ~ into the current user's home directoy, e.g. \~/Python/astro2 -> /home/david/Python/astro2
* `os.path.join`: Joins path components together intelligently, adding path separators appropriately (roughly the opposite of split)
* `os.path.splitext`: Splits the extension off a filename, e.g. Python/hello.py -> ('Python/hello', '.py')

## File operations

### Checking if things exist

* `os.path.exists`: Check if a file or directory exists
* `os.path.isfile`: Check if a file exists (returns False for directories)
* `os.path.isdir`: Check if a directory exists (returns False for files)

### Checking file metadata

* `os.path.getatime`: Gets last access time of a file
* `os.path.getmtime`: Gets last modification time of a file
* `os.path.getctime`: Gets last ctime of a file (creation for Windows, last metadata change for Unix)
* `os.path.getsize`: Gets file size of a path in bytes

# The `shutil` module

## High-level copying

* `shutil.copy`: Copies a file and its permissions
* `shutil.copy2`: Copies a file and all its metadata
* `shutil.copymode`: Copies permission bits from one path to another
* `shutil.copystat`: Copies metadata from one path to another
* `shutil.copytree`: Recursively copies a directory

## Other file operations

* `shutil.rmtree`: Recursively deletes a directory
* `shutil.move`: Recursively move a file or directory
* `shutil.which`: Finds the full path of a command
