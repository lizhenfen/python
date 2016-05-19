user_input = int(raw_input("number: ").strip())

#first
if user_input > 5:
    print "this number gt 5"
else:
    print "this number lt 5"

#second
print "this number gt 5" if user_input > 5 else "this number lt 5"