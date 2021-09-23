# The Basics

Using raw strings allows us to avoid having to double-escape backslashes

```python
'\\ ' == r'\ '
```

re.match searches for a pattern from the beginning of a string

```python
multimatch(r'python', ['python', 'python2', 'cpython'])
```

re.search searches for a pattern anywhere in a string

```python
multisearch(r'python', ['python', 'python2', 'cpython'])
```

# Basic pattern elements

. matches any single character

```python
multimatch(r'python.', ['python', 'python2', 'python3', 'pythona', 'python3.8'])
```

^ and $ match the start and end of a string or line

```python
multisearch(r'^expected$', ['expected', 'unexpected', 'expectedly'])
```

# Quantifiers

\* matches any number of the preceding item

```python
multimatch(r'whee*', ['whee', 'wheeee', 'wheeeeeeeeeeeeeee', 'wheef', 'whef', 'whf'])
```

\+ matches one or more of the previous item

```python
multimatch(r'whee+', ['whee', 'wheeeeeee', 'wheef', 'whef'])
```

? matches 0 or 1 of the previous item

```python
multimatch(r'whee?', ['whe', 'whee', 'wheee', 'why'])
multimatch(r'https?', ['http', 'https'])
```

{m} matches exactly m repetitions of the previous item

```python
multimatch(r'whe{2}$', ['whe', 'whee', 'wheee'])
multimatch(r'whe{3}$', ['whe', 'whee', 'wheee'])
```

{m, n} matches m to n (inclusive) repetitions of the previous item
```python
multimatch(r'whe{2,4}$', ['whe', 'whee', 'wheee', 'wheeee'])
```

# Wildcards

## Character sets

[Square brackets] match any of the characters inside them

```python
multimatch(r'^M[NOIA]$', ['MN', 'MO', 'MI', 'MT'])
```

Putting a caret first in the brackets matches anything *except* the characters inside

```python
multimatch(r'^M[^NOIA]$', ['MN', 'MO', 'MI', 'MT', 'MJ'])
```

You can also specify ranges of characters with a hyphen

```python
multimatch(r'^[A-Z]{2,3}[0-9]{2,3}$', ['AB12', 'ABC123', 'ABCD123', 'AB1'])
```

## Predefined character sets

* `\d`: Decimal digits; equivalent to [0-9]
* `\w`: Word characters; equivalent to [0-9a-zA-Z_]
* `\s`: Whitespace; matches spaces, line breaks, tabs, etc.
* `\b`: Word boundary: matches the empty string, but only at the start or end of a sequence of word characters

```python
multimatch(r'^\w+\s+\w+$', ['Luke Skywalker', 'Han Solo', 'Yoda'])
multimatch(r'^[A-Za-z]\w*$', ['x', 'varname', 'var_name', '1var_name'])
multisearch(r'\bknowing\b', ['He was knowing', 'He was knowingly', 'He was unknowing'])
```

Capitalizing them inverts what they match, e.g. \D matches anything *except* decimal digits

| matches the items on either side of it

```python
multimatch(r'red|yellow|green', ['red', 'yellow', 'greeny', 'blue'])
```

## Capture groups

Enclosing something in (parentheses) puts it in a group; the contents of a group can be pulled out of the match object afterward

```python
multimatch(r'^(\w+)\s+(\w+$)', ['Luke Skywalker', 'Han Solo', 'Yoda'])
```

(?:...) designates a non-capturing group (useful for applying quantifiers or other operations to a whole group)

```python
multimatch(r'\w+(?:,\w+)*$', ['words', 'words,words', 'words,words,words2'])
```

\1, \2, etc. match a previously matched group
```python
multimatch(r'^(\w+)\n\1$', ['duplicate_line\nduplicate_line'])
```

## Looking ahead/behind

* (?=...) matches the empty string only if followed by a match for ...
* (?!...) matches the empty string only if *not* followed by a match for ...
* (?<=...) matches the empty string only if preceded by a match for ...
* (?<!...) matches the empty string only if *not* preceded by a match for ...

# Substituting

re.sub replaces matches to a pattern with a replacement string (which can contain references to groups in the pattern)

Removing duplicate lines:

```python
re.sub(r'^(\w+)(?:\n\1)+$', r'\1', 'duplicate_line\nduplicate_line\nduplicate_line')
```

# Exercises

1. Write a regular expression to match Email addresses
2. Write a regular expression to match strings surrounded by quotation marks (single or double)
3. Write a regular expression that can be used in re.sub to fix Python indentation
