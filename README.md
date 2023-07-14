# website data extraction tool using python.

# The project automates the procss of collecting data from website.

# It quickly extract large amounts of data which saves time and effort compared to manual extraction. 

# It provide real-time information, allows us to stay updated with web changes.

# We can use the Extracted  data for different purposes like Data Analysis, Marketing and promotion.

# It can be used for Creating reports and analysis, also for Research and academic purposes.

Technology Stack:

Programming Language: Python

Libraries/Frameworks: Selenium, Pandas

Main Steps:

a. Establishing Browser Connection:

   1.The project uses Selenium's webdriver to establish a connection with the Chrome browser.
   
   2.The browser window is maximized to ensure optimal visibility.

b. Navigating to the Website:

   1.The code opens a target website (https://www.knowafest.com/explore/upcomingfests) to scrape event data.

c. Scraping Event Data:

   1.The code locates the table containing event details on the website using its ID.
   
   2.It extracts each row of the table, excluding the header row.
   
   3.For each row, it retrieves specific information such as event name, start date, event type, organizer name, address, end date, and organizer 
     email.
   

d. Additional Information Extraction:

   1.The code interacts with a "Read More" button in each row to open a new tab for further information.
   
   2.In the new tab, it searches for the event organizer's email address, if available, and retrieves it.
   
   3.The code switches back to the original window after extracting the required data.

e. Data Storage and Presentation:

   1.The extracted data is then appended to separate lists for each field (event name, start date, etc.).
   
   2.The lists are organized into a dictionary and used to create a Pandas DataFrame named "my_data2."
