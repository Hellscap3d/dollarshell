#!/usr/bin/env python3
import sys,os,subprocess
if len(sys.argv) == 1:
	print("dollarshell by Hellscaped")
	print("Usage: $ <command>")
	exit(0)
cmd = ""
def system(cmd):
	return subprocess.call('$SHELL -c "$GREPDB"', shell=True, env={'GREPDB': cmd,'SHELL':os.environ["SHELL"]})
os.system = system
index = 0
for v in sys.argv:
	if index-1 == len(sys.argv):
		cmd += v
	elif index != 0:
		cmd += v + " "
	index += 1
os.system(cmd)
