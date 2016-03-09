from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("fourth?" )
fifth = raw_input("fifth?" )

print "So, first is %r, second %r, third %r, fourth %r, fifth %r!" % (
    first, second, third, fourth, fifth)