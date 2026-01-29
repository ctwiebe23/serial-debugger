# NAME

serial_debugger — Debug devices over serial

# SYNOPSIS

    serial_debugger [-h] [-b BAUD] [-t TIMEOUT] [-e ENCODING]

# DESCRIPTION

Prompts the user to connect to a serial port, and then echoes all text recieved
over that connection to the terminal.

Press `<C-c>` to begin composing a message, and `Enter` to send it.

Press `<C-\>` to exit the program.

# OPTIONS

-h, \--help
:   show this help message and exit

-b, \--baud BAUD
:   serial port baud rate

-t, \--timeout TIMEOUT
:   serial port timeout period

-e, \--encoding ENCODING
:   the character encoding used over the serial port
