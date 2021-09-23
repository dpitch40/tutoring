# Useful system information

* **os.environ**: Dictionary storing environment variables
* **os.uname**: Returns information on the computer and operation system
```python
os.uname()
posix.uname_result(sysname='Linux', nodename='BABBAGE', release='5.4.0-77-generic', version='#86~18.04.1-Ubuntu SMP Fri Jun 18 01:23:22 UTC 2021', machine='x86_64')
```
* **os.cpu_count**: Returns the number of CPUs this computer has

# Python versions of command-line functions
os module function | Bash command
--- | ---
chdir | cd
getcwd | pwd
chmod | chmod
chown | chown
listdir | ls
mkdir | mkdir
remove | rm
rename | mv

# Other useful functions

* **os.system**: Lets you run terminal commands from Python!
* **os.walk**: Recursively traverses a directory structure, yielding a series of (dir, subdirs, filenames) tuples
* **os.urandom**: Returns random bytes for cryptographic use

# Portability

* **os.curdir**: e.g. "."
* **os.pardir**: e.g. ".."
* **os.sep**: "/" on Linux/Mac, "\\" on Windows
