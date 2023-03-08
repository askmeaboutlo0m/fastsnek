# NAME

fastsnek - high performance looping code in Python, but terrible

# SYNOPSIS

You need a way to install Perl modules, I'd recommend carton so you don't sully your system with this mess:

```
carton install
carton exec ./fastsnek.pl
```

Otherwise, install the `Inline::C` and `Inline::Python` modules manually and just run `./fastsnek.pl`.

# DESCRIPTION

This thing lets you run native code dynamically in Python, with Perl as a glue between them.

The [fastsnek.pl](fastsnek.pl) script is just a very small amount of Perl that will provide a function to compile some C code and otherwise just drops into Python immediately.

[fastsnek.py](fastsnek.py) then proceeds to compile some high-performance C code, which Perl will wire up. And then it proceeds to call that C function, which will print some numbers but it will do so real fast.

I've used this kind of thing in anger, but you really shouldn't. I had my reasons, honest, I'm not mad. And even if I am, you'll never catch me anyway!

# LICENSE

This code is licensed under CC0 1.0 Universal. See [the LICENSE file](LICENSE) for details.
