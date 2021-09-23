# The `argparse` module: your solution for command line Python scripts

## A simple example

Say we want to write a Python script for randomly generating passwords that works like this:

```
python3 password.py <password_length> [-p/--punctuation]
```

The Python code for generating a simple but secure password looks like:

```python
import secrets
import string

def generate_password(length, use_punctuation=False):
    chars = string.ascii_letters + string.digits
    if use_punctuation:
        chars += string.punctuation
    return ''.join([secrets.choice(chars) for i in range(length)])
```

Parsing the command line arguments the hard way, with `sys.argv`:

```python
import sys

def main():
    length = None
    use_punctuation = False
    for arg in sys.argv[1:]:
        if arg in ('-p', '--punctuation'):
            use_punctuation = True
        elif arg.isdigit():
            try:
                length = int(arg)
            except ValueError:
                print(f'Invalid length: {arg!r}')
                sys.exit(1)
        else:
            print(f'Unrecognized argument: {arg}')

    if length is None:
        print('Must specify password length')
    else:
        print(generate_password(length, use_punctuation))

if __name__ == '__main__':
    main()
```

The easy way, with the `argparse` module:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Randomly generate a secure password')

    parser.add_argument('-p', '--punctuation', action='store_true',
        help='Whether to use punctuation characters in the password')
    parser.add_argument('length', type=int, help='The number of characters in the password')

    args = parser.parse_args()

    print(generate_password(args.length, args.punctuation))

if __name__ == '__main__':
    main()
```

This is not only simpler and more understandable, but it also automatically handles invalid inputs and generates a usage string to show users how to invoke this script.

```
$ python3 password.py -h
usage: password.py [-h] [-p] length

Randomly generate a secure password

positional arguments:
  length             The number of characters in the password

optional arguments:
  -h, --help         show this help message and exit
  -p, --punctuation  Whether to use punctuation characters in the password
```

## A more complex example


```python
    parser = argparse.ArgumentParser(description='Download some album artwork.')
    parser.add_argument('-t', "--test", action="store_true",
                        help="Only preview changes, do not actually make them.")
    parser.add_argument('-e', "--extra", action="append", nargs=2, default=list(),
                        help="Specify extra data fields for tracks loaded from an external source.")
    parser.add_argument('-d', '--domain', help="Manually set the domain for web parsing")
    parser.add_argument("sources", nargs='+',
        help="The source(s) to get metadata from (db, files, or a location of a track list).")
    args = parser.parse_args()
```

Usage examples:

```
python3 DownloadArt.py https://vocadb.net/Al/3326 -e album "Ningen Shikkatsu" -e albumartist ZilartP -t
python3 DownloadArt.py https://vocadb.net/Al/9729 https://vocadb.net/Al/18050 https://vocadb.net/Al/788 https://vocadb.net/Al/12393
```

How would we parse these arguments with `sys.argv`? Do we even want to try?

## Exercise

Set up an ArgumentParser that accepts two regular expressions as arguments and performs a regular expression substitution using them on all files in the current directory. Add an option to preview the filename changes before making them (like --test above). Extra credit: actually write this script.

Example usage:

```
python3 rename_files.py "(Render.*)\.jpeg" "\1\.jpg"
python3 rename_files.py "SomeName(.+)" "\1SomeOtherName" -t
```
