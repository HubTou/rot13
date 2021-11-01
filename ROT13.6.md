# ROT13(6)

## NAME
rot13 — encrypt or decrypt caesar ciphers

## SYNOPSIS
**rot13**
\[-p|--printable\]
\[-r|--rotate NUMBER\]
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
-r\|--rotate NUMBER|Rotate NUMBER characters instead of 13
--debug|Enable debug mode
--help\|-?|Print usage and a short help message and exit
--version|Print version and exit
--|Options processing terminator

## ENVIRONMENT
The *ROT13_DEBUG* environment variable can be set to any value to enable debug mode.

The *FLAVOUR* or *ROT13_FLAVOUR* environment variables can be set to one of the following values, to implement only the corresponding options and behaviours.
* bsd | bsd:freebsd : FreeBSD [caesar(6)](https://www.freebsd.org/cgi/man.cgi?query=caesar) or [rot13(6)](https://www.freebsd.org/cgi/man.cgi?query=rot13)

## EXIT STATUS
The **rot13** utility exits 0 on success, and >0 if an error occurs.

## SEE ALSO
[caesar(6)](https://www.freebsd.org/cgi/man.cgi?query=caesar),
[fortune(6)](https://github.com/HubTou/fortune/blob/main/README.md),
[rot13(3)](https://github.com/HubTou/rot13/blob/main/ROT13.3.md),
[tr(1)](https://www.freebsd.org/cgi/man.cgi?query=tr)

## STANDARDS
The **rot13** utility is a standard UNIX command, though not a POSIX one.

It tries to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for [Python](https://www.python.org/) code.

## PORTABILITY
Tested OK under Windows.

## HISTORY
Rotated postings to [USENET](https://en.wikipedia.org/wiki/Usenet) and some of the databases used by the fortune(6) program
are [rotated by 13 characters](https://en.wikipedia.org/wiki/ROT13).

A program to decrypt caesar cyphers,
called [decrypt](https://minnie.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/src/new/new/news/src/caesar.c),
was contributed to [4.2BSD](https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution#4.2BSD)
by [Rick Adams](https://en.wikipedia.org/wiki/Rick_Adams_(Internet_pioneer)) in September 1982.
Its authors were Stan King and John Eldridge, working on an algorithm suggested by [Bob Morris](https://en.wikipedia.org/wiki/Robert_Morris_(cryptographer)).
That software [became the caesar(6) game](https://minnie.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/src/games/caesar/caesar.c)
in [4.3BSD-Reno](https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution#4.3BSD), in 1990.

Rot13 has also been implemented as a simple tr(1) characters translation.

This re-implementation was made for the [PNU project](https://github.com/HubTou/PNU).

The ability to process optional strings or filenames,
as well as choosing a different rotation or character set,
has been added in this re-implementation.

## LICENSE
This utility is available under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## AUTHORS
[Hubert Tournier](https://github.com/HubTou)

This manual page is based on the one written for [FreeBSD](https://www.freebsd.org/).

## CAVEATS
Unicode characters are left unchanged.

## SECURITY CONSIDERATIONS
This command's only purpose is to obfuscate a text, rather than seriously intending to protect it.
This last purpose has been deprecated about 2000 years ago!

