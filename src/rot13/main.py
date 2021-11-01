#!/usr/bin/env python
""" rot13 - encrypt or decrypt caesar ciphers
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import getopt
import logging
import os
import signal
import sys

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: rot13 - encrypt or decrypt caesar ciphers v1.0.5 (November 1, 2021) by Hubert Tournier $"

# Default parameters. Can be overcome by environment variables, then command line options
parameters = {
    "Command line arguments": False,
    "Character set" : "alphabetical",
    "Rotation": 13,
    "Command flavour": "PNU",
}


################################################################################
def _initialize_debugging(program_name):
    """Debugging set up"""
    console_log_format = program_name + ": %(levelname)s: %(message)s"
    logging.basicConfig(format=console_log_format, level=logging.DEBUG)
    logging.disable(logging.INFO)


################################################################################
def _display_help():
    """Displays usage and help"""
    print("usage: rot13 [--debug] [--help|-?] [--version]", file=sys.stderr)
    if parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        print("       [--]", file=sys.stderr)
        print(
            "  ---------  ------------------------------------------",
            file=sys.stderr
        )
        print("  --debug    Enable debug mode", file=sys.stderr)
        print("  --help|-?  Print usage and this help message and exit", file=sys.stderr)
        print("  --version  Print version and exit", file=sys.stderr)
        print("  --         Options processing terminator", file=sys.stderr)
    else: # if parameters["Command flavour"] == "PNU":
        print("       [-p|--printable] [-r|--rotate NUMBER]", file=sys.stderr)
        print("       [--] [string ...] [filename ...]", file=sys.stderr)
        print(
            "  ------------------  ------------------------------------------",
            file=sys.stderr
        )
        print("  -p|--printable      Rotate all printable ASCII characters", file=sys.stderr)
        print("  -r|--rotate NUMBER  Rotate NUMBER characters instead of 13", file=sys.stderr)
        print("  --debug             Enable debug mode", file=sys.stderr)
        print("  --help|-?           Print usage and this help message and exit", file=sys.stderr)
        print("  --version           Print version and exit", file=sys.stderr)
        print("  --                  Options processing terminator", file=sys.stderr)
    print(file=sys.stderr)


################################################################################
def _handle_interrupts(signal_number, current_stack_frame):
    """Prevent SIGINT signals from displaying an ugly stack trace"""
    print(" Interrupted!\n", file=sys.stderr)
    _display_help()
    sys.exit(0)


################################################################################
def _handle_signals():
    """Process signals"""
    signal.signal(signal.SIGINT, _handle_interrupts)


################################################################################
def _process_environment_variables():
    """Process environment variables"""
    # pylint: disable=C0103
    global parameters
    # pylint: enable=C0103

    if "ROT13_DEBUG" in os.environ:
        logging.disable(logging.NOTSET)

    if "FLAVOUR" in os.environ:
        parameters["Command flavour"] = os.environ["FLAVOUR"].lower()
    if "ROT13_FLAVOUR" in os.environ:
        parameters["Command flavour"] = os.environ["ROT13_FLAVOUR"].lower()

    # Command variants supported:
    if parameters["Command flavour"] == "PNU":
        parameters["Command line arguments"] = True
    elif parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        pass
    else:
        logging.critical("Unimplemented command FLAVOUR: %s", parameters["Command flavour"])
        sys.exit(1)

    logging.debug("_process_environment_variables(): parameters:")
    logging.debug(parameters)


################################################################################
def _process_command_line():
    """Process command line options"""
    # pylint: disable=C0103
    global parameters
    # pylint: enable=C0103

    # option letters followed by : expect an argument
    # same for option strings followed by =
    if parameters["Command flavour"] == "PNU":
        character_options = "pr:?"
        string_options = [
            "debug",
            "help",
            "printable",
            "rotate=",
            "version",
        ]
    elif parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        character_options = "?"
        string_options = [
            "debug",
            "help",
            "version",
        ]

    try:
        options, remaining_arguments = getopt.getopt(
            sys.argv[1:], character_options, string_options
        )
    except getopt.GetoptError as error:
        logging.critical("Syntax error: %s", error)
        _display_help()
        sys.exit(1)

    for option, argument in options:

        if option == "--debug":
            logging.disable(logging.NOTSET)

        elif option in ("--help", "-?"):
            _display_help()
            sys.exit(0)

        elif option == "--version":
            print(ID.replace("@(" + "#)" + " $" + "Id" + ": ", "").replace(" $", ""))
            sys.exit(0)

        elif option in ("-p", "--printable"):
            parameters["Character set"] = "ASCII"

        elif option in ("-r", "--rotate"):
            try:
                parameters["Rotation"] = int(argument)
            except ValueError as error:
                logging.critical("Option -r|--rotate parameter has to be an integer: %s", error)
                sys.exit(1)

    logging.debug("_process_command_line(): parameters:")
    logging.debug(parameters)
    logging.debug("_process_command_line(): remaining_arguments:")
    logging.debug(remaining_arguments)

    return remaining_arguments


################################################################################
def rot(text, rotation=13, character_set="alphabetical"):
    """Return the ROTxx version of the given text"""
    rotated_text = ""

    if character_set == "alphabetical":
        for character in text:
            if character.isalpha():
                if character.isupper():
                    rotated_text += chr(ord('A') + (ord(character) - ord('A') + rotation) % 26)
                else:
                    rotated_text += chr(ord('a') + (ord(character) - ord('a') + rotation) % 26)
            else:
                rotated_text += character

    elif character_set == "ASCII":
        for character in text:
            if character.isprintable():
                rotated_text += chr(ord(' ') + (ord(character) - ord(' ') + rotation) % 95)
            else:
                rotated_text += character

    return rotated_text


################################################################################
def main():
    """The program's main entry point"""
    program_name = os.path.basename(sys.argv[0])

    _initialize_debugging(program_name)
    _handle_signals()
    _process_environment_variables()
    arguments = _process_command_line()

    if len(arguments) \
    and parameters["Command line arguments"]:
        for argument in arguments:
            if os.path.isfile(argument):
                with open(argument, "r") as file:
                    for line in file.readlines():
                        print(
                            rot(
                                line,
                                rotation=parameters["Rotation"],
                                character_set=parameters["Character set"]
                            ),
                            end=""
                        )
            else:
                print(
                    rot(
                        argument,
                        rotation=parameters["Rotation"],
                        character_set=parameters["Character set"]
                    )
                )
    else:
        for line in sys.stdin:
            print(
                rot(
                    line,
                    rotation=parameters["Rotation"],
                    character_set=parameters["Character set"]
                ),
                end=""
            )

    sys.exit(0)


if __name__ == "__main__":
    main()
