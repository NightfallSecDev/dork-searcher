import requests
import argparse
import time
from functools import partial
from multiprocessing import Pool
from bs4 import BeautifulSoup as bsoup

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', help='Specify the file containing dorks')
    parser.add_argument('-e', '--engine', dest='engine', help='Specify the Search Engine (comma-separated list)')
    parser.add_argument('-p', '--pages', dest='pages', help='Specify the Number of Pages (Default: 1)', default=1, type=int)
    parser.add_argument('-P', '--processes', dest='processes', help='Specify the Number of Processes (Default: 2)', default=2, type=int)
    parser.add_argument('-o', '--output', dest='output', help='Specify the output file to save URLs', default='output.txt')
    parser.add_argument('-d', '--delay', dest='delay', help='Specify the delay time between searches in seconds (Default: 1)', default=1, type=float)
    return parser.parse_args()

# Define search functions for each search engine
def google_search(query, page):
    base_url = 'https://www.google.com/search'
    headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    params   = { 'q': query, 'start': page * 10 }
    resp = requests.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'html.parser')
    links = soup.findAll("div", { "class" : "yuRUbf" })
    return [link.find('a').get('href') for link in links]

def bing_search(query, page):
    base_url = 'https://www.bing.com/search'
    headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    params   = { 'q': query, 'first': page * 10 + 1 }
    resp = requests.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'html.parser')
    links  = soup.findAll('cite')
    return [link.text for link in links]

# Define additional search functions (dummy implementations)
def duckduckgo_search(query, page):
    base_url = 'https://duckduckgo.com/'
    headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    params   = { 'q': query, 's': page * 10 }
    resp = requests.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'html.parser')
    links = soup.findAll("a", {"class": "result__a"})
    return [link.get('href') for link in links]

# Add more search functions for other search engines...

# Create a dictionary for easy search engine selection
SEARCH_ENGINES = {
    'google': google_search,
    'bing': bing_search,
    'duckduckgo': duckduckgo_search,
    # Add more engines here
}

def save_results(result, output_file):
    with open(output_file, 'a') as f:
        for page_results in result:
            for url in page_results:
                f.write(url + '\n')

def main():
    options = get_arguments()

    if not options.file:
        print("Please provide a file with dorks using the -f option.")
        return

    engines = options.engine.lower().split(',')
    search_functions = [SEARCH_ENGINES.get(engine.strip()) for engine in engines if SEARCH_ENGINES.get(engine.strip())]
    
    if not search_functions:
        print('Invalid search engines! Please check the list of available engines.')
        return

    # Clear output file before writing new results
    with open(options.output, 'w') as f:
        pass  # This clears the file

    with open(options.file, 'r') as file:
        dorks = [line.strip() for line in file if line.strip()]

    for dork in dorks:
        for search_function in search_functions:
            print(f"\nProcessing dork: {dork} with {search_function.__name__}")
            target = partial(search_function, dork)

            with Pool(options.processes) as pool:
                results = pool.map(target, range(options.pages))

            save_results(results, options.output)
            time.sleep(options.delay)  # Delay between searches

if __name__ == '__main__':
    banner = '''
    ██████╗░░█████╗░██████╗░██╗░░██╗  ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
    ██║░░██║██║░░██║██████╔╝█████═╝░  ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
    ██║░░██║██║░░██║██╔══██╗██╔═██╗░  ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
    ██████╔╝╚█████╔╝██║░░██║██║░╚██╗  ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
    ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

    Made By: @NightfallSecDev
    GitHub: https://github.com/NightfallSecDev
    YouTube:not avilabie 
    '''

    print(banner)
    main()
