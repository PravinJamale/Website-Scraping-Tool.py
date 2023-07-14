# website data extraction tool using python.

Technology Stack:

Programming Language: Python

Libraries/Frameworks: Selenium, Pandas

Main Steps:

a. Establishing Browser Connection:

   1. The project uses Selenium's webdriver to establish a connection with the Chrome browser.
   
   2. The browser window is maximized to ensure optimal visibility.

b. Navigating to the Website:

   1. The code opens a target website (https://www.knowafest.com/explore/upcomingfests) to scrape event data.

c. Scraping Event Data:

   1. The code locates the table containing event details on the website using its ID.
   
   2. It extracts each row of the table, excluding the header row.
   
   3. For each row, it retrieves specific information such as event name, start date, event type, organizer name, address, end date, and 
      organizer email.
   

d. Extracting Event Organizer Email:

   1. The code clicks on a "Read More" button in each row to open a new tab with more details.
   
   2. In the new tab, it searches for an HTML element with the class "card-body" to locate the event organizer's email address.
   
   3. If a email address is found, it extracts and stores it. If not, it assigns the value "N/A" to the variable. 
   
   
e.  Switching Windows and Exception Handling:

   1. The code switches between the original window and the newly opened tab to perform necessary actions.
   
   2. Exception handling is implemented to handle scenarios where the email address is not found or elements are not present. 


f. Data Storage and Presentation:

   1. The extracted data is then appended to separate lists for each field (event name, start date, etc.).


g. Creating and Exporting DataFrame:

   1. The lists containing event data are organized into a dictionary.
   
   2. The dictionary is used to create a Pandas DataFrame named "my_data2".

   3. The DataFrame is exported to a CSV file named "KNOW A FEST EVENTS LISTS WITH EVENT ORGANIZERS EMAIL.csv".
   
  
