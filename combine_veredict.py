#!/usr/bin/env python3
import sys

final_veredict = 'AC'
for veredict_file in sys.argv[2:]:
	veredict = open(veredict_file, "r").readline().strip()
	if veredict != 'AC':
		final_veredict = veredict
		break
print(f"{sys.argv[1]},{final_veredict}")

