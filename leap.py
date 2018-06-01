
year = int(input())

leap = False

def is_leap(year):
	if year%4==0:
		if year%100!=0:
			leap = True
		if year%100==0:
			if year%400==0:
				leap = True
			else:
				leap = False
	else:
		leap = False
	return leap

print(leap)


