# Decorator Basics

Decorators are placed above a function or class definition. They are an example of "syntactic sugar"; they don't do anything new, but provide an easier and more readable way to modify classes.

## Basic Decorators

The syntax for simple decorators looks like this:

```python
def decorator1(func):
    # Do something and return a function

def decorator2(func):
    # Do something else and return a function

@decorator1
@decorator2
def f():
    # Do something
```

The decorated definition is equivalent to:

```python
def f():
    # Do something
f = decorator1(decorator2(f))
```

### Examples

Automatically cache the result of a long-running or costly function so it only has to be run once:

```python
cache_dict = dict()

def cache(func):
    def wrapped(*args, **kwargs):
        if func not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[func] = result
        return cache_dict[func]
    return wrapped

@cache
def long_running_func():
    # Do something time-consuming
```

Two real world examples from my Telephone Pictionary game:

Require a user to be logged in to access a page:

```python
def require_logged_in(func):
    def wrapped(*args, **kwargs):
        if 'username' in flask_session:
            return func(*args, **kwargs)

        flash('You must login to view this page', 'warning')
        return render_template('login.html')
    return wrapped
```

Automatically provide Flask endpoint functions with the currently logged-in player and a database session:

```python
def inject_current_player(func):
    def wrapped(*args, **kwargs):
        with current_app.db.session_scope() as session:
            return func(session, get_current_player(session), *args, **kwargs)
    return wrapped
```

## Decorators with Arguments

Decorator functions can also accept arguments. In this case, they should return an argumentless function which in turn should return a function to replace the decorated function.

```python
def decorator_with_arguments(arg1, arg2):
    def inner(func):
        def wrapped(*args, **kwargs):
            # Do something and return a function
        return wrapped
    return inner

def decorator2(func):
    # Do something else and return a function

@decorator1(1, 'a')
@decorator2
def f():
    # Do something
```

The decorated definition is equivalent to:

```python
def f():
    # Do something
f = decorator_with_arguments(1, 'a')(decorator2(f))
```

### Examples

Add a function to a registry:

```python
function_registry = dict()

def register_function(key):
    def inner(func):
        function_registry[key] = func
        return func
    return inner
```

Flask routing (mapping Python functions to URLs):

```python
from flask import current_app

@current_app.route('/', methods=['GET'])
def index():
    return '<p>A web page</p>'
```

## Class Decorators

Similar to function decorators, they are called on a class after it is defined and their return value replaces the class.

```python
@f1(arg)
@f2
class Foo: pass
```

Is equivalent to:

```python
class Foo: pass
Foo = f1(arg)(f2(Foo))
```

### Example

A simpler way to add classes to a registry than metaclasses?

```python
class_registry = dict()

def register_class(key):
    def inner(cls):
        class_registry[key] = cls
        return cls
    return inner

@register_class('foo')
class Foo:
    pass
```

# Some Useful Build-in Decorators

## @classmethod

```python
class Foo:

    @classmethod
    def class_method(cls, *args):
        pass
```

## @staticmethod

```python
class Foo:

    @staticmethod
    def static_method(*args):
        pass
```

## @property

```python
class Foo:

    @property
    def bar(self):
        return calculate_bar()

    @bar.setter
    def bar(self, value):
        return set_bar(value)

    @bar.deleter
    def bar(self):
        return delete_bar()

foo = Foo()
foo.bar = 'a'
print(foo.bar)
del foo.bar
```

## @functools.cached_property

```python
from functools import cached_property

class Foo:
    @cached_property
    def calculate_bar(self):
        return time_consuming_calculation()
```

## @functools.wraps

Used in wrapper/decorator functions to preserve the signature (arguments, docstring, etc.) of the wrapped function.

Really real-world example:

```python
def inject_current_player(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        with current_app.db.session_scope() as session:
            return func(session, get_current_player(session), *args, **kwargs)
    return wrapped
```

# Exercises

1. Write a decorator that keeps track of the arguments a function has been called with and the result, and returns the cached result if it is called with the same arguments again.

```python
@cache_with_arguments
def is_prime(n)
    # Calculations go here

print(is_prime(127)) # Should be calculated
print(is_prime(128)) # Should be calculated
print(is_prime(127)) # Should be returned from cache, not recalculated
```

2. Write a decorator that makes a function behave differently (e.g. return None) if its string argument matches a provided regular expression.

```python
ignore_re = re.compile(r'^http://')

@ignore_from_re(ignore_re)
def get_secure_web_content(url):
    return requests.get(url).text
```
