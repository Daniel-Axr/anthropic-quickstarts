from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import typer 
import csv
import os

EBS_LINK = "https://calculator.aws/#/createCalculator/EBS"
EC2_LINK = ""
DOWNLOADS = r"C:\Users\temp\Downloads"
app = typer.Typer()
options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get(EBS_LINK)

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(By.XPATH, "//input[@aria-label = 'Number of volumes Enter amount']")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="awsui_content_vjswe_1ekr7_149 awsui_label_1f1d4_ocied_5")

text_box.click()  # Ensure the text box is focused
text_box.send_keys()

# submit_button.click()

data = {

    'row' : 1,
    'data': {
        
        'Number of Volumes' : '3', 
        'Average duration' : '900',
        'Storage for each EC2 instance': 'General Purpose SSD (gp2)',
        'Storage amount per volume': '30 GB',
        'Snapshot Frequency': '3x Daily',
        'Amount changed per snapshot': '3',
        'Number of snapshots to restore': '1',
        'Number of GetSnapshotBlock API requests': '1',
        'Number of LIST API requests' : '1',
        'Number of PutSnapshotBlock API requests' : '1'

    }
    

}

def insertValueToInput(element_title, value):

    text_box = driver.find_element(By.XPATH, f"//input[@aria-label = '{element_title}']")

    ActionChains(driver)\
            .key_down(Keys.CONTROL)\
            .send_keys_to_element(text_box, )\
            .key_up(Keys.CONTROL)\
            .send_keys_to_element(text_box, value)\
            .perform()
    
def csvtodict():
    pass

#TODO update the function 
# to find the latest file 
def findfile(file_name):
    keeptry = True
    file_keyname = input("Enter the first few letters you want to search. Enter cont to exit")

    while keeptry: 
        file_list = os.listdir(DOWNLOADS)
        for i in file_list:
            
            if file_keyname in i:
                return os.path.join(DOWNLOADS, i) 
        if file_keyname == "cont":
            keeptry = False

    return -1


@app.command()
def downloaddata(driver, url: str, file_format: str):  
    driver.get(url)

    # Initialize ActionChains with the driver instance
    actions = ActionChains(driver)
    
    # Start the download sequence
    actions.key_down(Keys.ALT).send_keys("F").key_up(Keys.ALT).send_keys("D")

    # Add a conditional for the format
    if file_format == "csv":
        actions = actions.send_keys("C")
    elif file_format == "xlsx":
        actions = actions.send_keys("X")
    
    # Execute the actions
    actions.perform()

@app.command()
def listdatarow(row_number: int):
    pass
        
def getSpecs():
    pass


@app.command()
def fillallebs():

    insertValueToInput(element_title="Number of volumes Enter amount", value='3') 
    insertValueToInput(element_title="Average duration each instance runs Value", value='900') 
    insertValueToInput(element_title="Storage amount per volume Value", value='30') 
    insertValueToInput(element_title="Amount changed per snapshot Value", value='3') 
    insertValueToInput(element_title="Number of GetSnapshotBlock API requests Value", value='1') 
    insertValueToInput(element_title="Number of LIST API requests Value", value='1')
    insertValueToInput(element_title="Number of snapshots to restore Value", value='1')
    insertValueToInput(element_title="Number of PutSnapshotBlock API requests Value", value='1') 



def main():

    message = '''
    
    If you want to insert value according to the sheet enter i
    If you want to quit, enter q
    If you want to download data, enter d

    '''
    iscontinue = True
    userinput = ""
    while iscontinue:

        userinput = input(message)
        if userinput == "q":
            iscontinue = False

        if userinput == "i":
            print("These are the values from table")
            row = input("Which row do you want to input?")
            insertValueToInput(element_title="Number of volumes Enter amount", value=10)

        if userinput == "d":
            downloaddata


    driver.quit()    

if __name__ == "__main__":
    
    app()
    # main()
    