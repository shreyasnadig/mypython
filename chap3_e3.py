def grade(score):
	if score < 0 or score > 1:
		return "Bad Score"
	if score >= 0.9:
		return 'A'
	elif score >= 0.8:
		return 'B'
	elif score >= 0.7:
		return 'C'
	elif score >= 0.6:
		return 'D'
	else: return 'F'

def main():
	try:
		score = raw_input("Enter score: ")
		g = grade(float(score))
		print (g)
	except:
		print("Bad score")

if __name__ == '__main__':
	main()
