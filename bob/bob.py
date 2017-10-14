import re
def hey(string):
	string = string.strip()
	if (string == ''):
		return "Fine. Be that way!"
	elif string.isupper():
		return "Whoa, chill out!"
	elif (string.endswith('?')):
		return 'Sure.'
	return 'Whatever.'
	"""
	string = string.strip()
	if len(re.findall(r'[A-Z]',string))>7 or len(re.findall(r'[A-Z]+!',string))>0:
		return "Whoa, chill out!"
	if string == '' or len(re.findall('Bob',string))>0:
		return "Fine. Be that way!"
	if string[-1] == "?":
		return "Sure."
	return "Whatever." """
	

