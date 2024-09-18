
# Dork Searcher

Welcome to Dork Searcher! This tool allows you to automate the process of searching for URLs using a list of dorks across multiple search engines. It's designed to help security researchers and developers efficiently gather URLs based on specific search queries.

## Features

- **Multi-Engine Support**: Search across multiple search engines (Google, Bing, DuckDuckGo, and more).
- **Customizable**: Adjust the number of pages, delay between searches, and number of processes.
- **Results Saving**: Save the collected URLs to a file for further analysis.
- **Parallel Execution**: Utilize multiple processes to speed up the search.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NightfallSecDev/dork-searcher.git
   cd dork-searcher
   ```

2. **Install Dependencies**

   Ensure you have Python 3.7 or later installed. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with the following options:

```bash
python dork_search.py -f dorks.txt -e google,bing,duckduckgo -p 2 -P 4 -o results.txt -d 2
```

### Options

- `-f, --file`: Specify the file containing dorks (one dork per line).
- `-e, --engine`: Specify the search engines to use (comma-separated list). Available options: `google`, `bing`, `duckduckgo`, and more.
- `-p, --pages`: Number of pages to search for each dork (default: 1).
- `-P, --processes`: Number of processes to use for parallel execution (default: 2).
- `-o, --output`: Output file to save URLs (default: `output.txt`).
- `-d, --delay`: Delay time between searches in seconds (default: 1).

## Example

To search for dorks listed in `dorks.txt` across Google, Bing, and DuckDuckGo, save the results in `results.txt`, and introduce a 2-second delay between searches:

```bash
python dork_search.py -f dorks.txt -e google,bing,duckduckgo -p 2 -P 4 -o results.txt -d 2
```

## Contributing

We welcome contributions to improve this project! If you have any suggestions or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request with a clear description of the changes.

## Acknowledgments

- [@NightfallSecDev](https://github.com/NightfallSecDev) - Author


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



