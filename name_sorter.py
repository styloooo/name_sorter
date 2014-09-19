#Not stable name sorter
import sys

print "Welcome to name sorter!"

def main(argv):
	names = []
	i = 1
	while True:

		print "Enter first and last name %s:" %i
		name = raw_input()
		if(name == "-1"):
			break
		names.append(name)
		i += 1

	names.sort(key=lambda x: x.split()[1])
	print names

if(__name__ == "__main__"):
	main(sys.argv)