from argparse import ArgumentParser

def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="serial_debugger",
        description="Debug devices over serial"
    )
    
    parser.add_argument(
        "-b", "--baud",
        default=9600,
        type=int,
        help="serial port baud rate",
    )
    
    parser.add_argument(
        "-t", "--timeout",
        default=1,
        type=int,
        help="serial port timeout period",
    )
    
    parser.add_argument(
        "-e", "--encoding",
        default="utf-8",
        type=str,
        help="the character encoding used over the serial port",
    )
    
    return parser
