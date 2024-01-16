#  a-z
#  0-9
#  . _ timing only 1
#  @ timing 1
#  . 2,3 position from back side

import re
#
# email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# useremail = input("Enter your Email : ")
# if re.search(email_condition,useremail):
#     print("Right Email")
# else:
#     print("Wrong Email")
# ^ start with ke liye ye sign lagte hain
# ? fix that . _ must be come only one time...
# $ peeche se 2,3 index pr . 



# ## 🗒️ Answer
# The provided Python code uses a regular expression to validate if the entered email address is in the correct format. Here's a breakdown of the regular expression used:
# - `^[a-z]+`: The email must start with one or more lowercase letters.
# - `[\._]?`: There can be an optional dot (.) or underscore (_) after the initial letters.
# - `[a-z 0-9]+`: Followed by one or more lowercase letters or digits.
# - `[@]`: The mandatory "@" symbol.
# - `\w+`: One or more word characters (letters, digits, or underscores) representing the domain name.
# - `[.]`: The mandatory dot before the domain extension.
# - `\w{2,3}$`: The domain extension, consisting of two or three characters at the end.



# import re
email_condition = "^[a-z]+[._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
useremail = input("Enter your Email : ")
if re.search(email_condition, useremail):
       print("Right Email")
else:
       print("Wrong Email")
