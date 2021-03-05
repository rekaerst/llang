#!/usr/bin/python3
import sys
import typing


def main(argv: list):
    if len(argv) > 1:
        src_file = open(argv[1])
    else:
        print("\033[1;37mllang: \033[1;31mfatal error\033[0m: no input file")
        return 1

    chars = read(src_file)
    tokens = tokenize(chars)

    print(tokens)


def read(src_file: typing.IO) -> typing:
    """genarte a list of characters from file

    All comments, which are lines starts with //,will be discarded

    Args:
        src_file (typing.IO): source file to read

    Returns:
        typing: a list of characters from src_file
    """
    l1 = src_file.readlines()
    l2 = []
    # get rid of comments
    for i in range(len(l1)):
        if str.strip(l1[i])[0:2] != "//":
            l2 += l1[i]
    return l2


def tokenize(chars: list) -> list:
    token = ""
    tokens = []
    separator_chars = "\ \t\n"
    special_chars = "()+-*/:;"
    string_indicators = "\"\'"
    # the flag is to be set to True if we are in a string literial, otherwise is set to False
    is_instr = False

    for i in range(len(chars)):
        # always check if we are in a string literial first
        if chars[i] in string_indicators:
            # we are at the end of a string literial
            if is_instr:
                # keep \"s for our parser
                tokens += ["\"" + token + "\""]
                token = ""
            # flip a coin
            is_instr = not is_instr
            continue

        # a string literial is a token in the whole
        if is_instr:
            token += chars[i]
            continue

        # count special chars as a token on it's own and a separator
        if chars[i] in special_chars:
            if token != "":
                tokens += [token]
            token = ""
            tokens += [chars[i]]
            continue

        # now noly keywords and separator chars are lefted
        if chars[i] in separator_chars:
            # empty token is useless, skip it
            if token != "":
                tokens += [token]
            token = ""
        else:
            token += chars[i]

    return tokens


if __name__ == "__main__":
    sys.exit(main(sys.argv))
