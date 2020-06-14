
## Delete all comma "," except the one at the first of each row ( the one who separate the origin of recipes and their ingredients ) 
with open("train_cuisine.csv","r") as infile, \
     open("output.csv","w") as outfile:
	for line in infile:
     		outfile.write(("".join(line.split(","))).replace("'",",'",1).replace("'",""))








