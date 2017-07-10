grades=[]
print('Enter grades from all sections:')
for section in range(1,18):
	grade = raw_input("section %d grade: " % section)
	grades.append(int(grade))
	if section == 8 or section == 16:
		print('-----------------------')
print("SCORE: %d / 100" % sum(grades))
