from signal import signal, SIGINT, SIGQUIT
from sys import exit

from serial import Serial
from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo

from log import Log
from cli import build_parser
    
def prompt_user_for_port() -> ListPortInfo:
    "Prompts the user until a valid serial port is chosen"
    selected_port: ListPortInfo = None

    while selected_port is None:
        ports = comports()
        
        if len(ports) == 0:
            Log.warn_in("No ports found; press any key to rescan...")
            continue
        
        if len(ports) == 1:
            Log.info(f"One port found; automatically connecting to {ports[0].device}")
            selected_port = ports[0]
            break
        
        Log.info("Available ports:\n")
        i = 0
        for port in ports:
            i += 1
            Log.info(f"  {i}) {port.device}: {port.description}")

        raw_choice = input("\nChoose your port (enter a number): ")
        
        try:
            choice = int(raw_choice)
            selected_port = ports[choice - 1]
        except:
            Log.error("Not a valid number")
            continue
    
    return selected_port

def read_from_ser(ser: Serial, encoding: str) -> str:
    "Reads a string from the serial port"
    return ser.readline().decode(encoding, errors="replace").strip()

def send_to_ser(ser: Serial, encoding: str, string: str):
    "Writes a string to the serial port"
    ser.write(string.encode(encoding, errors="replace"))

def main():
    ser: Serial = None
    parser = build_parser()
    args = parser.parse_args()

    def shutdown():
        Log.info("Shutting down...")
        if ser is not None:
            ser.close()
        Log.info("Done!")
        exit(0)
        
    def sigquit(signum, frame):
        print("")
        shutdown()

    signal(SIGQUIT, sigquit)
    
    def sigint(signum, frame):
        print("")
        if ser is None:
            Log.warn("Serial port is not initialized")
            return
        
        message = input("send: ")
        send_to_ser(ser, args.encoding, message)
    
    signal(SIGINT, sigint)
    
    port = prompt_user_for_port()
        
    Log.info(f"Opening serial on {port.device}...")
    try:
        ser = Serial(port.device, baudrate=args.baud, timeout=args.timeout)
        
        Log.info("Success.  Press <C-c> to write a message, and <C-\\> to begin shutdown")
        
        Log.info(f"Listening...")
        while True:
            resp = read_from_ser(ser, args.encoding)
            if (resp.strip() != ""):
                Log.info("recv: " + resp)

    except Exception as ex:
        Log.error("ERROR connecting to serial device: ")
        print(ex)

    shutdown()
    
if __name__ == "__main__":
    main()
