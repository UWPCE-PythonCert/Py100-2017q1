# Load dependent modules
import requests

def BLSscraper(URL):
    # Define global variables and start a session
    session = requests.Session()
    response = session.get('{0}'.format(URL))
    response = response.text
    response = response.split(sep="\n")

    # Print header row
    print("Series ID\t\t\t\t\t\tPeriod\t\tValue (000s)\tPreliminary")

    # Loop through each item in the response (row), reformat, and print
    for item in response:
        cells = str(item)
        cells = cells.split(sep=" ")
        if cells[0] == str("SMS53000000000000001"):
            print(str(cells[0])+"\t\t"+str(cells[10])+str(cells[16]))


BLSscraper("https://download.bls.gov/pub/time.series/sm/sm.data.50.Washington")