# entity-everything
>  Easy to use tool for encoding text to html entities. 

## Features
1. Encoding text passed as an argument
2. Encoding text from the standard input

## What is the purpose of this script?
There are plenty of online tools on the Internet for encoding text to html entities. However, the solutions i found have one thing in common: they only convert special characters, without changing letters and numbers.

If for some reason you want to convert letters and numbers to entities as well, "entity-everything" is the script for you.

## How to use?
Encoding text passed as an argument:
```
python entity-everything.py "Text to encode"
```
Encoding text from the standard input:
```
echo "Text to encode" | python entity-everything.py
```

## Examples
```
python entity-everything.py "Lorem ipsum"
# Result: &#76;&#111;&#114;&#101;&#109;&#32;&#105;&#112;&#115;&#117;&#109;
```

```
python entity-everything.py "Hello! 🙂"
# Result: &#72;&#101;&#108;&#108;&#111;&#33;&#32;&#128578;
```


## Technologies used
The script has been written in Python.
It should work with versions 3.9 or higher.
The script does not require any dependencies.