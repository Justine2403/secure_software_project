''''
Your name: 
Student ID:
E-mail:
'''

import args, urllib.request
from urllib.error import HTTPError

def fuzz(arguments):
    """Fuzz a target URL with the command-line arguments specified by ``arguments``."""
    
    # Load the URL template and the wordlist
    url_template = arguments.url
    wordlist_path = arguments.wordlist

    # Read the wordlist file
    with open(wordlist_path, 'r') as f:
        words = f.readlines()

    # Strip any extra whitespace from the words
    words = [word.strip() for word in words]

    # Get the extensions to add (if any)
    extensions = arguments.extensions

    # Get the list of match codes (default to [200, 301, 302, 401, 403])
    match_codes = arguments.match_codes or [200, 301, 302, 401, 403]

    # Iterate over the wordlist
    for word in words:
        # Create a list of URLs to test: the base word + extensions
        urls_to_test = [url_template.replace("FUZZ", word)]  # Include the base word without extensions
        for ext in extensions:
            urls_to_test.append(url_template.replace("FUZZ", word + ext))  # Add the word with each extension

        # Iterate over all the URLs to test
        for fuzzed_url in urls_to_test:
            try:
                # Make an HTTP request
                with urllib.request.urlopen(fuzzed_url) as response:
                    status_code = response.getcode()
                    
                    # Check if the status code matches any in the list of match codes
                    if status_code in match_codes:
                        # Print the status code and URL in the required format
                        print(f"{status_code} {fuzzed_url}")

            except HTTPError as e:
                # Skip 404 errors and any other HTTP errors, check against match_codes
                if e.code in match_codes:
                    print(f"{e.code} {fuzzed_url}")

# do not modify this!
if __name__ == "__main__":
    arguments = args.parse_args()
    fuzz(arguments)
