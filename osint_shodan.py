#!/usr/bin/python3
import shodan
import config


SHODAN_API_KEY = config.SHODAN_API_KEY

api = shodan.Shodan(SHODAN_API_KEY)

try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError as e:
        print('Error: {}'.format(e))
