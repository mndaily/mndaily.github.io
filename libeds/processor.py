import json

bases = {'name': '', 'children': []}
cores = []
courses = json.load(open('courses.json'))['courses']
themes = []
subjects = []

mapping = {
	'AH': 'Arts/Humanities',
	'BIOL': 'Biological Science',
	'HIS': 'Historical Perspective',
	'LITR': 'Literature',
	'MATH': 'Mathematical Thinking',
	'PHYS': 'Physical Science',
	'SOCS': 'Social Sciences',
	'CIV': 'Civic Life and Ethics',
	'DSJ': 'Diversity and Social Justice',
	'ENV': 'The Environment',
	'GP': 'Global Perspectives',
	'TS': 'Technology & Society'
}

def get_index(l, name):
	for i in range(len(l)):
		if l[i]['name'] == mapping[name]: return i
	return -1

def get_index_course(l, name):
	for i in range(len(l)):
		if l[i]['name'] == name: return i
	return -1

for course in courses:
	if not course['diversified_core']: continue
	if not course['designated_theme']: continue
	if course['catalog_number'][-1] == 'H': continue

	if course['diversified_core'] not in cores:
		bases['children'].append({'name': mapping[course['diversified_core']], 'children':[]})
		cores.append(course['diversified_core'])

	idx1 = get_index(bases['children'], course['diversified_core'])

	if (course['diversified_core'], course['designated_theme']) not in themes:
		bases['children'][idx1]['children'].append({'name': mapping[course['designated_theme']], 'children':[]})
		themes.append((course['diversified_core'], course['designated_theme']))

	idx2 = get_index(bases['children'][idx1]['children'], course['designated_theme'])

	if (course['diversified_core'], course['designated_theme'], course['subject']) not in subjects:
		bases['children'][idx1]['children'][idx2]['children'].append({'name': course['subject'], 'children':[]})
		subjects.append((course['diversified_core'], course['designated_theme'], course['subject']))

	idx3 = get_index_course(bases['children'][idx1]['children'][idx2]['children'], course['subject'])
	link = "http://onestop2.umn.edu/courseinfo/viewCourseGuideTermAndSubject.do?searchSubject=" + course['subject'] + "#" + course['subject'] + course['catalog_number']

	bases['children'][idx1]['children'][idx2]['children'][idx3]['children'].append({'name': course['title'], 'link': link, 'size': 1})

with open('data.json', 'w') as f:
  json.dump(bases, f, ensure_ascii=False)
