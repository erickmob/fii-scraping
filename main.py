# Press Shift+F10 to execute   
import csv
import requests
from bs4 import BeautifulSoup

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting...')
    print('Connecting to target url...')

    url = 'https://www.fundsexplorer.com.br/ranking'
    response = requests.get(url)
    page = response.content
    print('Conected!')



    print('Starting to parse target page ...')
    soup = BeautifulSoup(page, 'html.parser')

    tableRanking = soup.find('table', id='table-ranking')
    # tableHeader = tableRanking.findAll("th")
    # tableRows = tableRanking.findAll("tr")
    #
    #
    # print("Printing TableHeaders")
    # for th in tableHeader:
    #     print(th.get_text())
    #
    # print("Printing TableRows")
    # for tr in tableRows:
    #     print(tr.get_text())

    output_rows = []
    for table_row in tableRanking.findAll('tr'):
        headers = table_row.findAll('th')
        columns = table_row.findAll('td')

        output_row = []
        for header in headers:
            output_row.append(header.text)

        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print("Done")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
