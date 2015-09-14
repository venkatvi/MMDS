if __name__ == '__main__':
	x = [ 15, 21, 24, 30, 49];
	multiplesOfTwo = [];
	multiplesOfThree = [];
	multiplesOfFive = []
		
	for i in range(len(x)):
		num = x[i];
		isMultipleOfTwo = False;
		isMultipleOfThree = False;
		isMultipleOfFive =False;
		while (num%2 == 0):
			if (isMultipleOfTwo == False):
				multiplesOfTwo.append(x[i]);
				isMultipleOfTwo = True;
			num = num/2;
		while( num%3 == 0):
			if (isMultipleOfThree == False):
				multiplesOfThree.append(x[i]);	
				isMultipleOfThree = True;
			num = num/3;
		while(num%7 == 0):
			if (isMultipleOfFive == False):
				multiplesOfFive.append(x[i]);	
				isMultipleOfFive = True;
			num = num/5; 

	print multiplesOfTwo
	print multiplesOfThree
	print multiplesOfFive
	print sum(multiplesOfTwo);
	print sum(multiplesOfThree);
	print sum(multiplesOfFive);