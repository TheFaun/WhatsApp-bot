from selenium import webdriver
"""
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url) 
"""
driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user: ')
msg = input('Enter the message: ')
count = int(input('Enter the count: '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
  msg_box.send_keys(msg)
  button = driver.find_element_by_class_name('_3M-N-')
  button.click()

print("FINISH!")