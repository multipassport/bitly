import argparse
import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(headers, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {'long_url': url}
    response = requests.post(bitly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def get_count_of_clicks(headers, url):
    bitlink = urlparse(url)._replace(scheme='').geturl()
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_short_link(headers, url):
    bitlink = urlparse(url)._replace(scheme='').geturl()
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser(
        description='Script which either converts URL to bit.ly shortlink'
            ' or returns the number of bit.ly shortlink clicks.',
        )
    parser.add_argument(
        'url',
        help='Enter url to shorten it or bitlink to get total clicks '
            'on the link:\n',
        )
    return parser


if __name__ == '__main__':
    parser = create_parser()
    user_url = parser.parse_args().url

    load_dotenv()
    headers = {'Authorization': f'Bearer {os.getenv("BITLY_TOKEN")}'}
    
    try:
        if is_short_link(headers, user_url):
            clicks_count = get_count_of_clicks(headers, user_url)
            print('The link was clicked', clicks_count, 'times.')
        else:
            bitlink = shorten_link(headers, user_url)
            print('Shortlink: ', bitlink)
    except requests.exceptions.HTTPError:
        print('Incorrect link')
