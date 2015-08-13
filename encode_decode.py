
def encode(list_of_strings, delimiter):
    return delimiter.join(list_of_strings)

def decode(myString, delimiter):
    return myString.split(delimiter)

delimiter = '\0'
enc = encode(["abc", "c", "d"], delimiter)
print "%s is the encoded list" % enc

dec = decode(enc, delimiter)
n = 1
for i in dec:
    print "entry number %d = %s" % (n, i)
    n += 1

delimiter = '---'
enc = encode(["1", "cba", "dc"], delimiter)
print "%s is the encoded list" % enc

dec = decode(enc, delimiter)
print "%s is the decoded list" % dec




    



