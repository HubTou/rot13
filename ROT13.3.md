# ROT13(3)

## NAME
rot13 — return the ROTXX version of the given text

## SYNOPSIS
**import rot13**

String rot13.**rot**(String *text*, Int *rotation*, String *character_set*)

## DESCRIPTION
The **rot** function returns the ROT13 version of the given *text*.

All the other parameters also have default values and thus are optional.

The *rotation* parameter sets the character set rotation to be used instead of the default 13.

The *character_set* parameter defines the characters affected by the rotation.
Possible values are:
* "alphabetical" for [A-Za-z] characters. The default value
* "ASCII" for printable ASCII characters

## SEE ALSO
[caesar(6)](https://www.freebsd.org/cgi/man.cgi?query=caesar),
[fortune(6)](https://github.com/HubTou/fortune/blob/main/README.md),
[rot13(6)](https://github.com/HubTou/rot13/blob/main/ROT13.6.md)

## STANDARDS
The **rot13** library tries to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for [Python](https://www.python.org/) code.

## HISTORY
There is a [rot13 codec](https://docs.python.org/3/library/codecs.html?highlight=rot13) usable with the str.encode() function in Python, but it is less flexible.

This library was made for the [PNU project](https://github.com/HubTou/PNU).

## LICENSE
This utility is available under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## AUTHORS
[Hubert Tournier](https://github.com/HubTou)

## CAVEATS
Unicode characters are left unchanged.

## SECURITY CONSIDERATIONS
This command's only purpose is to obfuscate a text, rather than seriously intending to protect it.
This last purpose has been deprecated about 2000 years ago!

