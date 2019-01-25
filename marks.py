def grade(name,marks):
	print(name)
	if 100>=marks>90:
		print('A Grade')
	elif 90>=marks>80:
		print('B Grade')
	elif 80>=marks>70:
		print('C Grade')
	elif 70>=marks>60:
		print('D Grade')
	elif 60>=marks>50:
		print('E Grade')
	else:
		print('F Grade')

def grade_all(dictionary):
	for name, marks in dictionary.items():
		grade(name, marks)

test_dict={'Parvinder': 90,'Singh': 35}
grade_all(test_dict)