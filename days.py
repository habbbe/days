#!/usr/bin/env python

import sys
import dateparser
import pathlib
from datetime import datetime

dateArg = 'DATE|now|today|tomorrow|...'

cmd = pathlib.PurePath(sys.argv[0]).name

def error(msg):
    print(msg)
    printHelp()
    exit(1)

def printHelp():
    print(f'Usage: {cmd} [{dateArg}] until {dateArg}')
    print( f"""
Examples:
    {cmd} now until dec 25
    {cmd} January 1 1970 until now
    {cmd} until may 23 2030
""")

until = 'until '

cmdLine = " ".join(sys.argv[1:])

if cmdLine in ['--help', '-h', 'help']:
    printHelp()
    exit(0)

fromDate = datetime.now()

untilIdx = cmdLine.find(until)

if untilIdx == -1:
    error("Invalid syntax")

if untilIdx > 0:
    if not cmdLine[untilIdx - 1].isspace():
        error("Invalid syntax")

    fromDate = dateparser.parse(cmdLine[:untilIdx])
    if not fromDate:
        error("Invalid start date")

toDate = dateparser.parse(cmdLine[untilIdx + len(until):])

if not toDate:
    error("Invalid end date")

print(toDate - fromDate)
