# Client-API
# Currency Converter CLI (REST API Client)

This is a **Python command-line application** that fetches **real-time currency exchange rates** from a public REST API and allows users to:

- View exchange rates for a base currency
- Convert an amount from one currency to another
- Run automated tests using `pytest`
- 
##  Features

- Fetch live currency exchange rates
- Convert currency using command line
- Retry API requests on failure
- Configurable API URL (Environment Variable / config.json)
- Input validation
- Unit tests with mocked API calls

  ## Technologies Used

- Python 3
- `requests`
- `argparse`
- `pytest`
- `unittest.mock`

##  Project Structure

├── client.py # Main application code

├── test_client.py # Unit tests

├── config.json # (Optional) API configuration

├── README.md # Project documentation

## Create virtual environment (optional but recommended)

python -m venv venv

source venv/bin/activate

venv\Scripts\activate         

## Install dependencies

pip install requests pytest

## Usage
## Show exchange rates

python client.py rates --from USD

## Convert currency

python client.py convert --from USD --to INR --amount 100

## Example output:

100 USD = 8300 INR

## conclusion

This project shows how to build a Python command-line application that fetches real-time data from a REST API.

It demonstrates good practices like input validation, error handling, environment variables, and retry logic.

It helps beginners understand unit testing using pytest and mocking without calling real APIs.
