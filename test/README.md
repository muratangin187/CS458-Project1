#Test Cases

##Test Case 1

###Test 1.1 - Login with existing credentials and valid captcha
###Test 1.2 - Login with existing credentials and invalid captcha
###Test 1.3 - Login with non-existing credentials and valid captcha
###Test 1.4 - Login with non-existing credentials and invalid captcha
###Test 1.5 - Login without credentials and valid captcha

##Test Case 2

###Test 2.1 - Copy password field via control+c and control+v
###Test 2.2 - Copy id field via control+c and control+v

##Test Case 3

###Test 3.1 - Enter home page after login(redirect auth page)
###Test 3.2 - Enter reset password page after login(ID is autofilled)

##Test Case 4

###Test 4.1 - Reset password enter invalid ID
###Test 4.2 - Reset password enter valid ID
###Test 4.3 - Reset password enter valid ID and invalid answer
###Test 4.4 - Reset password enter valid ID and just answer(password field empty)
###Test 4.5 - Reset password enter valid ID, invalid answer and new password
###Test 4.6 - Reset password enter valid ID, valid answer and invalid password(passwords do not match)
###Test 4.7 - Reset password enter valid ID, valid answer and valid password

##Test Case 5

###Test 5.1 - Try captcha for multiple times
###Test 5.2 - Try captcha for multiple times(exceed limit)