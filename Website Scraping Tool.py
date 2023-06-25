#!/usr/bin/env python
# coding: utf-8

# In[1]:


# website data extraction tool using python
# We can use the Extracted  data for different purposes like Data Analysis, Marketing


# In[2]:


# COMPLETE PROJECT 


# In[3]:


# imports the time module in Python, allow to access various functions and classes related to timekeeping and delays.

import time

# imports the Options class from the selenium.webdriver.chrome.options module, which allows you to customize the behavior and settings of the Chrome browser when using Selenium.

from selenium.webdriver.chrome.options import Options

# imports the webdriver module from the selenium library, allow to automate web browsers.

from selenium import webdriver

# imports the By class from the selenium.webdriver.common.by module, which is used in Selenium to specify the locating mechanism for finding web elements on a webpage.

from selenium.webdriver.common.by import By

# imports the NoSuchElementException class from the selenium.common.exceptions module.

from selenium.common.exceptions import NoSuchElementException

# Create ChromeOptions object
options = Options()

# Create a connection with the browser
browser = webdriver.Chrome(options=options)

# Maximize the browser window
browser.maximize_window()

# Open the website
browser.get("https://www.knowafest.com/explore/upcomingfests")

# Access Table from website by ID  

table=browser.find_element(By.ID,"tablaDatos")

# search the elements within the table
# Access Table Body (tbody tag)

tbody = table.find_element(By.TAG_NAME,"tbody")

# Accessing ALL table rows (tr tags) within table body (tbody tag) 

tr_list= tbody.find_elements(By.TAG_NAME,"tr")

# To Make DataFrame use pandas library

import pandas as pd

# Created Empty Lists for appending All Table Data Elements from All Table Rows except FIRST TABLE ROW

# After printing my_data (pandas Dataframe) by using dictionary(result_dict) , get lists of value in rows, under each key which becomes a name of column

# This line of code initializes multiple empty lists in a single line. Each list is assigned to a corresponding variable

Event_Name_list = []
Event_Start_Date_list = []
Event_Type_list = []
Event_Organiser_Name_list = []
Event_Address_list = []
Event_End_Date_list = []
Event_Organiser_Email_list = []

i=0
for tr in tr_list:
    if i==0:
        i+=1
        continue
        
   
    td_list = tr.find_elements(By.TAG_NAME, "td") # Extract Each table row -> ALL table data elements ; EXCEPT FIRST TABLE ROW 
    
    # We cannot use td_list of tbody because tbody is not iterate each table rows to extract individual table rows'(tr tag); all table body(td tag) elements 
    
    # After extracting ALL table data elements from ALL Table Rows within tbody; ALL table data elements, not supports INDEXING
    
    start_date = td_list[0].text
    event_name = td_list[1].text # Another way of fetching the element    
    
    read_more_button = td_list[1].find_element(By.XPATH,".//span[@class='btn btn-sm u-btn-skew u-btn-primary g-mr-10 g-mb-15']")
    browser.execute_script("arguments[0].scrollIntoView();", read_more_button)
    read_more_button.click()

    # Switching to the newly opened tab
    
    current_window = browser.current_window_handle
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)
    
    # It finds the email address of the event organizer by searching for an HTML element with the class "card-body" 
    # If a matching email address is found, it assigns it to the variable "event_organiser_email". If no match is found, it assigns the value "N/A" to the variable.

    try:
        divclass = browser.find_element(By.XPATH, "//div[@class='card-body']")
        a_tags = divclass.find_elements(By.XPATH, "//a[@class='link link-secondary link-pointer']")

        for a_tag in a_tags:
            if a_tag.get_attribute("href").startswith("mailto:"):
                event_organiser_email = a_tag.get_attribute("href").split(":")[1]
                break
    except NoSuchElementException:
        event_organiser_email = "N/A"

    # Switch back to the original window
    browser.close()
    browser.switch_to.window(current_window)
    time.sleep(5)

    event_type = td_list[2].text
    event_location_data = td_list[3]
    event_end_date = td_list[4].text

    span_tag_list_elements_within_td_tag_elements = event_location_data.find_elements(By.TAG_NAME,"span")
    event_organiser_name = span_tag_list_elements_within_td_tag_elements[1].text
    event_address = span_tag_list_elements_within_td_tag_elements[2].text
          
    print("Event_Name:",    event_name, 
          "Event_Start_Date:",   start_date, 
          "Event_Type:",  event_type,
          "Event_Organiser_Name:",  event_organiser_name , 
          "Event_Address: ",   event_address, 
          "Event_End_Date:",   event_end_date,
          "Event_Organiser_Email:",event_organiser_email)
    print("\n\n")
    
    Event_Name_list.append(event_name)
    Event_Start_Date_list.append(start_date)
    Event_Type_list.append(event_type)
    Event_Organiser_Name_list.append( event_organiser_name)
    Event_Address_list.append(event_address)
    Event_End_Date_list.append(event_end_date)
    Event_Organiser_Email_list.append(event_organiser_email)

result_dict = {"Event Name": Event_Name_list, "Event Start Date": Event_Start_Date_list, "Event Type": Event_Type_list,
               "Event Oraganiser Name": Event_Organiser_Name_list, "Event Address":Event_Address_list, 
               "Event End Date": Event_End_Date_list, "Event Organiser Email": Event_Organiser_Email_list}

my_data2 = pd.DataFrame(data=result_dict)


# In[4]:


my_data2


# In[5]:


# Export the data to a csv file
my_data2.to_csv("KNOW A FEST EVENTS LISTS WITH EVENT ORGANIZERS EMAIL.csv")


# In[ ]:




