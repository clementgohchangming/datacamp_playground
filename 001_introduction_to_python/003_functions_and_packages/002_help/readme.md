# Help!
Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: `help().` In IPython specifically, you can also use `?` before the function name.

To get help on the `max()` function, for example, you can use one of these calls:

```python
help(max)
?max
```

Use the Shell to open up the documentation on `complex().` Which of the following statements is true?

# Possible Answers
1. `complex()` takes exactly two arguments: `real` and `[, imag]`.

2. `complex()` takes two arguments: `real` and `imag`. Both these arguments are required.

3. `complex()` takes two arguments: `real` and `imag`. `real` is a required argument, `imag` is an optional argument.

4. `complex()` takes two arguments: `real` and `imag`. If you don't specify `imag`, it is set to 1 by Python.

# Answer

3. 
`complex()` takes two arguments: `real` and `imag.` `real` is a required argument, `imag` is an optional argument.

```python
In [1]:
help(complex)
Help on class complex in module builtins:

class complex(object)
 |  complex(real[, imag]) -> complex number
 |  
 |  Create a complex number from a real part and an optional imaginary part.
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      complex.__format__() -> str
 |      
 |      Convert to a string according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  conjugate(...)
 |      complex.conjugate() -> complex
 |      
 |      Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number
```
