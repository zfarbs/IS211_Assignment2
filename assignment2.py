import logging
import urllib.request
from datetime import datetime
import argparse

logging.basicConfig(filename='errors.log')
logger = logging.getLogger('assignment2')


def downloadData(url):
    try:
        res = urllib.request.urlopen(url).read().decode('utf-8')
        return(res)
    except:
        return('Error getting data, expected a URL')


def processData(data):
    data = data.split('\n')[1:-1]
    processed_data = {}
    line_num = 1

    for i in data:
        line_num += 1
        i = i.split(',')

        try:
            i[2] = datetime.strptime(i[2], '%d/%m/%Y').date()
        except:
            logger.error('Error processing line #{} for ID #{}'.format(
                line_num, i[0]))
            pass

        processed_data[i[0]] = (i[1], i[2])
    return(processed_data)


def displayPerson(id, personData):
    for key in personData:
        if int(key) == int(id):
            print('Person #{} is {} with a birthday of date {}'.format(
                key, personData[key][0], personData[key][1]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True)
    args = parser.parse_args()

    csv_data = downloadData(args.url)
    processed_data = processData(csv_data)
    query = int(input('User ID: '))

    while query > 0:
        displayPerson(query, processed_data)
        query = int(input('User ID: '))


if __name__ == '__main__':
    print(main())
