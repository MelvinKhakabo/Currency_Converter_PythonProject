# Currency_Converter_PythonProject
A currency converter fetches real-time exchange rates from an API and allows users to convert between various currencies

# Outline of the Currency Converter Project
## Objective
Build a Python application that converts amounts between different currencies using live exchange rates from an API (e.g., ExchangeRate API or Currency Layer API).

## Features
Currency Conversion
Converts a specified amount from one currency to another using real-time exchange rates.
Fetch Live Rates
Retrieves the latest exchange rates from a currency exchange API.
View Available Currencies
Displays a list of supported currencies for the user.
User-Friendly Menu
Simple menu-driven interface for ease of use.

### Structure
API Integration
Use the requests library to fetch exchange rate data from an API.
Handle errors like API downtime or invalid responses.
Currency Conversion Logic
Calculate the target currency amount using the formula:
Converted Amount
=
Base Amount
×
Exchange Rate
Converted Amount
=
Base Amount
×
Exchange Rate

### Interactive Menu:
1. Display options to the user
2. Convert Currency.
3. View Available Currencies.
4. Exit the program.
Error Handling
Validate user input (e.g., numeric amounts, valid currency codes).
Handle network issues and API errors gracefully.
Modules and Libraries:
requests:
Fetch live data from the API.
json:
Parse API responses.

### Setup
Register for an API key from a currency exchange service.
Set up the base URL for fetching data.
Fetch Exchange Rates
Use the API endpoint to retrieve a JSON object containing exchange rates.
Currency Conversion
Prompt the user for the base and target currencies and the amount to convert.
Use the fetched rates to compute the conversion.
Display Results
Show the converted amount along with the source and target currencies.
Additional Features
Provide a list of supported currencies.
Allow the user to exit or restart the program.

#### Example Interaction:
Welcome to the Currency Converter!
Enter your base currency (e.g., USD): USD

1. Convert Currency
2. View Available Currencies
3. Exit
Choose an option: 1

Enter target currency (e.g., EUR): EUR
Enter amount to convert: 100

100 USD = 85.73 EUR

1. Convert Currency
2. View Available Currencies
3. Exit
Choose an option: 2

Available Currencies:
USD, EUR, GBP, INR, JPY, ...

1. Convert Currency
2. View Available Currencies
3. Exit
Choose an option: 3







