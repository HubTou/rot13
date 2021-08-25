# Installation
pip install [pnu-rot13](https://pypi.org/project/pnu-rot13/)

# ROT13(6)

## NAME
rot13 — encrypt or decrypt caesar ciphers

## SYNOPSIS
**rot13**
\[-p|--printable\]
\[-r|--rotate number\]
\[--debug\]
\[--help|-?\]
\[--version\]
\[--\]
\[string ...\]
\[filename ...\]

## DESCRIPTION
The **rot13** utility encrypts or decrypts [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) using a rotation of 13 characters.
By default, **rot13** reads from the standard input and writes to the standard output.
If an optional parameter corresponding to a valid filename is given, **rot13** will process this file instead.
If the optional parameter is not a filename, **rot13** will rotate this string.

### OPTIONS
Options | Use
------- | ---
-p\|--printable|Rotate all printable ASCII characters instead of just the alphabetical ones
-r\|--rotate number|Rotate ''number'' characters instead of 13
--debug|Enable debug mode
--help\|-?|Print usage and a short help message and exit
--version|Print version and exit
--|Options processing terminator

## ENVIRONMENT
The ROT13_DEBUG environment variable can also be set to any value to enable debug mode.

## EXIT STATUS
The **rot13** utility exits 0 on success, and >0 if an error occurs.

## SEE ALSO
[caesar(6)](https://www.freebsd.org/cgi/man.cgi?query=caesar),
[fortune(6)](https://github.com/HubTou/fortune/blob/main/README.md)

## STANDARDS
The **rot13** utility is a standard UNIX command, though not a POSIX one.

It tries to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for [Python](https://www.python.org/) code.

## PORTABILITY
Tested OK under Windows.

## HISTORY
Rotated postings to [USENET](https://en.wikipedia.org/wiki/Usenet)
and some of the databases used by the fortune(6) program
are [rotated by 13 characters](https://en.wikipedia.org/wiki/ROT13).

This re-implementation was made for the [PNU project](https://github.com/HubTou/PNU).

The ability to process optional strings or filenames,
as well as choosing a different rotation or character set,
has been added in this re-implementation.

## LICENSE
This utility is available under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## AUTHORS
[Hubert Tournier](https://github.com/HubTou)

The man page is derived from the [FreeBSD project's one](https://www.freebsd.org/cgi/man.cgi?query=rot13).

## CAVEATS
Unicode characters are left unchanged.

## SECURITY CONSIDERATIONS
This command's only purpose is to obfuscate a text, rather than seriously intending to protect it.
This last purpose has been deprecated about 2000 years ago!

