import vxi11
import time

instr =  vxi11.Instrument("192.168.1.31")
instr.write("*IDN?\n")
print(instr.read())

instr.write("OUTP ON\n")
time.sleep(2)
instr.write("OUTP OFF\n")
	
instr.close()
