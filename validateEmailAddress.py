import re

'''
 validate email
 find domain
 find TLD
'''
def email(x="hamidaucc@gmail.com"):
	pattern=re.compile(r'''([\w\.-]+)
			   @
			   ([\w\.-]+)
			   \.
			   ([a-z]{2,6})$
			   ''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
	match=re.fullmatch(pattern,x)
	if match:
		print(f'e-mail: {match.group()}')
		print(f"Domain: {match.group(2)}")
		print(f"Top level domain : {match.group(3)}")
	else:
		print(f'Given email < {x} > is invalid !!')

email()
y="abcd_123@gmail.com"
wrongEmail="hamid@gmail.com@"
print("*" * 15)
email(y)
print("*" * 15)
email(wrongEmail)
