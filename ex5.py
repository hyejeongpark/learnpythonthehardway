name = 'Zed A. Shaw'
age = 35
height = 74 #inches
height_in_centimeters = height * 1.6
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %s centimeters tall." % height_in_centimeters
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % ( 
    age, height, weight, age + height + weight)