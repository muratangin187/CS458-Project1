from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestRunner:

    def __init__(self):
        self.home = "http://localhost:3000/"
        self.resetPassword = "http://localhost:3000/reset.html"
        self.authPage = "http://localhost:3000/auth.html"
        self.logs = []
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager(log_level=50).install())
        except:
            raise Exception("Error occured on webdriver initialization of Chrome")
        
    def __del__(self):
        time.sleep(3)
        self.driver.close()
    
    def goUrl(self, link):
        self.driver.get(link)
        
    def getHomeScreenFormElements(self):
        idInput = self.driver.find_element_by_id("idNumber")
        passwordInput = self.driver.find_element_by_id("password")
        captchaInput = self.driver.find_element_by_id("captcha")
        loginButton = self.driver.find_element_by_id("loginButton")
        realCaptcha = self.driver.execute_script("return currentCaptcha;")
        idInput.clear()
        passwordInput.clear()
        captchaInput.clear()
        return idInput, passwordInput, captchaInput, loginButton, realCaptcha

    def getResetScreenFormElements(self):
        idInput = self.driver.find_element_by_id("idNumber")
        answerInput = self.driver.find_element_by_id("questionText")
        newPassword = self.driver.find_element_by_id("newPassword")
        newPasswordAgain = self.driver.find_element_by_id("newPasswordAgain")
        resetButton = self.driver.find_element_by_id("forgetButton")
        idInput.clear()
        return idInput, answerInput, newPassword, newPasswordAgain, resetButton
        
    def runTestOne(self):
        print("\nStarted Test Case #1")
        self.goUrl(self.home)
        
        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        idInput.send_keys("21702962")
        passwordInput.send_keys("123")
        captchaInput.send_keys(realCaptcha)
        loginButton.click()
        time.sleep(2)
        
        if(self.driver.current_url == self.authPage):
            print("--Success Test #1.1")
        else:
            print("--Failed Test #1.1")

        logoutButton = self.driver.find_element_by_id("logoutButton")
        logoutButton.click()
        time.sleep(1)

        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        idInput.send_keys("21702962")
        passwordInput.send_keys("123")
        captchaInput.send_keys("RANDOM")
        loginButton.click()
        time.sleep(2)
        if(self.driver.current_url == self.home):
            alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
            if(alert == "Please enter correct captcha!"):
                print("--Success Test #1.2")
            else:
                print("--Failed Test #1.2")
        else:
            print("--Failed Test #1.2")
        time.sleep(1)

        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        idInput.send_keys("217021232")
        passwordInput.send_keys("123213")
        captchaInput.send_keys(realCaptcha)
        loginButton.click()
        time.sleep(2)
        if(self.driver.current_url == self.home):
            alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
            if(alert == "Invalid password or ID"):
                print("--Success Test #1.3")
            else:
                print("--Failed Test #1.3")
        else:
            print("--Failed Test #1.3")
        time.sleep(1)

        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        idInput.send_keys("217021232")
        passwordInput.send_keys("123213")
        captchaInput.send_keys("RANDOM")
        loginButton.click()
        time.sleep(2)
        if(self.driver.current_url == self.home):
            alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
            if(alert == "Please enter correct captcha!"):
                print("--Success Test #1.4")
            else:
                print("--Failed Test #1.4")
        else:
            print("--Failed Test #1.4")
        time.sleep(1)

        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        captchaInput.send_keys(realCaptcha)
        loginButton.click()
        time.sleep(2)
        if(self.driver.current_url == self.home):
            alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
            if(alert == "Please fill ID and password fields"):
                print("--Success Test #1.5")
            else:
                print("--Failed Test #1.5")
        else:
            print("--Failed Test #1.5")
        time.sleep(1)

    def runTestTwo(self):
        print("\nStarted Test Case #2")
        self.goUrl(self.home)
        
        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        passwordInput.send_keys("123123")
        beforePassword = passwordInput.get_attribute("value")
        passwordInput.send_keys(Keys.CONTROL, "a")
        passwordInput.send_keys(Keys.CONTROL, "c")
        passwordInput.clear()
        passwordInput.send_keys(Keys.CONTROL, "v")
        afterPassword = passwordInput.get_attribute("value")
        if(afterPassword != beforePassword):
            print("--Success Test #2.1")
        else:
            print("--Failed Test #2.1")

        #########################################
        idInput.send_keys("21702913")
        beforeId = idInput.get_attribute("value")
        idInput.send_keys(Keys.CONTROL, "a")
        idInput.send_keys(Keys.CONTROL, "c")
        idInput.clear()
        idInput.send_keys(Keys.CONTROL, "v")
        afterId = idInput.get_attribute("value")
        if(afterId == beforeId):
            print("--Success Test #2.2")
        else:
            print("--Failed Test #2.2")
        time.sleep(1)

    def runTestFive(self):
        print("\nStarted Test Case #5")
        self.goUrl(self.home)
        
        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        captchaInput.clear()
        captchaInput.send_keys("FIRST TRY CAPTCHA")
        loginButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert != "Please enter correct captcha!"):
            print("--Failed Test #5.1")
        else:
            print("--Success Test #5.1")
        #########################################
        for i in range(6):
            captchaInput.clear()
            captchaInput.send_keys(str(i) + " TRY CAPTCHA")
            loginButton.click()
            alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
            time.sleep(1)
        captchaInput.clear()
        captchaInput.send_keys("LAST TRY CAPTCHA")
        loginButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "Please try again later (Too many attempt)"):
            print("--Success Test #5.2")
        else:
            print("--Failed Test #5.2")
        time.sleep(1)

    def runTestThree(self):
        print("\nStarted Test Case #3")
        self.goUrl(self.home)
        
        #########################################
        idInput, passwordInput, captchaInput, loginButton, realCaptcha = self.getHomeScreenFormElements()
        idInput.send_keys("21702825")
        passwordInput.send_keys("456")
        captchaInput.send_keys(realCaptcha)
        loginButton.click()
        time.sleep(2)
        
        self.goUrl(self.home)

        if(self.driver.current_url == self.authPage):
            print("--Success Test #3.1")
        else:
            print("--Failed Test #3.1")

        self.goUrl(self.resetPassword)

        if(self.driver.find_element_by_id("idNumber").get_attribute("disabled")):
            print("--Success Test #3.2")
        else:
            print("--Failed Test #3.2")
        
        self.goUrl(self.authPage)
        logoutButton = self.driver.find_element_by_id("logoutButton")
        logoutButton.click()
        time.sleep(1)

    def runTestFour(self):
        print("\nStarted Test Case #4")
        self.goUrl(self.resetPassword)
        
        #########################################
        idInput, answerInput, newPassword, newPasswordAgain, resetButton = self.getResetScreenFormElements()
        idInput.send_keys("21702900123")
        resetButton.click()
        time.sleep(1)
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "No student found with ID Number"):
            print("--Success Test #4.1")
        else:
            print("--Failed Test #4.1")

        #########################################
        idInput, answerInput, newPassword, newPasswordAgain, resetButton = self.getResetScreenFormElements()
        idInput.clear()
        idInput.send_keys("21702900")
        resetButton.click()
        time.sleep(1)
        resetButtonName = resetButton.get_attribute("innerText")
        if(resetButtonName == "Reset password"):
            print("--Success Test #4.2")
        else:
            print("--Failed Test #4.2")
        #########################################
        answerInput.send_keys("random answer")
        resetButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "Please fill all the fields"):
            print("--Success Test #4.3")
        else:
            print("--Failed Test #4.3")
        time.sleep(1)
        #########################################
        newPassword.send_keys("random password")
        newPasswordAgain.send_keys("random password")
        resetButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "The answer of the secret question is false"):
            print("--Success Test #4.4")
        else:
            print("--Failed Test #4.4")
        time.sleep(1)
        #########################################
        answerInput.clear()
        newPassword.clear()
        newPasswordAgain.clear()
        answerInput.send_keys("liverpool")
        newPassword.send_keys("random password")
        newPasswordAgain.send_keys("random password two")
        resetButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "You need to write same password twice"):
            print("--Success Test #4.5")
        else:
            print("--Failed Test #4.5")
        time.sleep(1)
        #########################################
        answerInput.clear()
        newPassword.clear()
        newPasswordAgain.clear()
        answerInput.send_keys("liverpool")
        newPassword.send_keys("789")
        newPasswordAgain.send_keys("789")
        resetButton.click()
        alert = self.driver.find_element_by_id("alertBox").get_attribute("innerText")
        if(alert == "You changed your password successfully, please login now"):
            print("--Success Test #4.6")
        else:
            print("--Failed Test #4.6")
        time.sleep(2)
        if(self.driver.current_url == self.home):
            print("--Success Test #4.7")
        else:
            print("--Failed Test #4.7")
        
testRunner = TestRunner()
testRunner.runTestOne()
testRunner.runTestTwo()
testRunner.runTestThree()
testRunner.runTestFour()
testRunner.runTestFive()
