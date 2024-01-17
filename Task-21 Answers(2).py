#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\shais\OneDrive\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")


# In[5]:


try:
    print("cookies present")
except:
    print("cookies not present")


# In[ ]:




