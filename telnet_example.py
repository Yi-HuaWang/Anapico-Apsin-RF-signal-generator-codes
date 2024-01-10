import telnetlib
import time

instr = telnetlib.Telnet('192.168.1.31', 18)
instr.write(b"*IDN?\n")
print(instr.read_until(b"\n", 2))

instr.write(b"OUTP ON\n")
time.sleep(2)
instr.write(b"OUTP OFF\n")

instr.close()