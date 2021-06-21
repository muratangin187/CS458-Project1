#SRS Login System

##Introduction
In this project, we implemented SRS login page and reset password page. In addition to the existing functionality, we implemented a captcha system.
Project structure divided into three different folders.

###Backend
In the backend folder, there is a node project exist. It implemented by using different frameworks such as Express.js and NeDB.
In order to run backend server, you need to enter backend folder and run 'npm install'. After the command finished, you can start server via 'npm run start'

###Frontend
In the frontend folder, we used HTML, CSS and javascript to develop index, login, and auth pages. We used Bootstrap for styling and Axios for handling network requests. There is no need to run a seperate server for frontend code, you can access frontend when you start backend server via "localhost:3000".

###Test
You can see the test cases and the main program in the test folder. It is implemented in Python. In order to run "test.py" you need to install webdriver_manager and selenium via pip package manager. Then you can run the script via "python3 test.py" command.

##Authors
Furkan Kazım Akkurt 21702900
Murat Angın 21702962
Muhammed Emre Yıldız 21702825