#!/usr/bin/env python
# coding: utf-8

# In[1]:


# website data extraction tool using python.

# The project automates the procss of collecting data from website.

# It quickly extract large amounts of data which saves time and effort compared to manual extraction. 

# It provide real-time information, allows us to stay updated with web changes.

# We can use the Extracted  data for different purposes like Data Analysis, Marketing and promotion.

# It can be used for Creating reports and analysis, also for Research and academic purposes.


# In[2]:


# COMPLETE PROJECT 


# In[3]:


import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# To Create a connection with browse

browser = webdriver.Chrome()

# To Maximize the browser window
browser.maximize_window()

# For Opening the website
browser.get("https://www.knowafest.com/explore/upcomingfests")

# Accessed Table from website by ID  

table=browser.find_element(By.ID,"tablaDatos")

# searching the elements within the table
# TO Access Table Body (tbody tag)

tbody = table.find_element(By.TAG_NAME,"tbody")

# Accessed ALL table rows (tr tags) within table body (tbody tag) 

tr_list= tbody.find_elements(By.TAG_NAME,"tr")

# For Making DataFrame used pandas library

import pandas as pd

# Created Empty Lists for appending All Table Data Elements from All Table Rows except FIRST TABLE ROW

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
        
   
    td_list = tr.find_elements(By.TAG_NAME, "td") # Extracted Each table row -> ALL table data elements ; EXCEPT FIRST TABLE ROW 
    
    start_date = td_list[0].text
    event_name = td_list[1].text # Another way of fetching the element    
    
    read_more_button = td_list[1].find_element(By.XPATH,".//span[@class='btn btn-sm u-btn-skew u-btn-primary g-mr-10 g-mb-15']")
    browser.execute_script("arguments[0].scrollIntoView();", read_more_button)
    read_more_button.click()

    # Switched to the newly opened tab
    
    current_window = browser.current_window_handle
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)
    
    
    
    try:
        divclass = browser.find_element(By.XPATH, "//div[@class='card-body']")
        a_tags = divclass.find_elements(By.XPATH, "//a[@class='link link-secondary link-pointer']")
             
    # Above, It finds the email address of the event organizer by searching for an HTML element with the class "card-body" 
    
    
    # If a matching email address is found, it assigns it to the variable "event_organiser_email". If no match is found, it assigns the value "N/A" to the variable.
    
        for a_tag in a_tags:
            if a_tag.get_attribute("href").startswith("mailto:"):
                event_organiser_email = a_tag.get_attribute("href").split(":")[1]
                break
    except NoSuchElementException:
        event_organiser_email = "N/A"
  
   
    # Switched back to the original window
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
