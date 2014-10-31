import sys

def is_valid_int(string):
	try:
        int(string.strip())
    except (ValueError, TypeError, OverflowError):
    	return False
    else: 
    	return True
       
try:
	loops = sys.argv[1]
except IndexError:
	loops = raw_input("Input your fizz, buzz. ")

if is_valid_int(loops):
	number = int(loops)
    for x in xrange(1, number+1):
            if x % 3 == 0 and x % 5 == 0:
                print "FizzBuzz",
            elif x % 3 == 0:
                print "Fizz",
            elif x % 5 == 0:
                print "Buzz",
            else:
                print x,
else:
	print 'sdfafkl'