import time
with open('a.txt','a+') as f:
   while True:
	   line = f.readline()
	   if line is None:
	       time.sleep(2)
	   print line