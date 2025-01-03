#currency code python code
import requests

# Base URL for ExchangeRate API
API_URL = "https://api.exchangerate-api.com/v4/latest/"

# Fetch conversion rates
def get_conversion_rate(base_currency):
    try:
        response = requests.get(f"{API_URL}{base_currency}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching rates: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Convert currency
def convert_currency(data, from_currency, to_currency, amount):
    if to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        converted_amount = rate * amount
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print(f"Currency '{to_currency}' not found!")

# Main menu
def main():
    print("Welcome to the Currency Converter!")
    base_currency = input("Enter your base currency (e.g., USD): ").upper()
    data = get_conversion_rate(base_currency)
    if not data:
        print("Unable to fetch exchange rates. Exiting...")
        return

    while True:
        print("\nCurrency Converter")
        print("1. Convert Currency")
        print("2. View Available Currencies")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            to_currency = input("Enter target currency (e.g., EUR): ").upper()
            try:
                amount = float(input("Enter amount to convert: "))
                convert_currency(data, base_currency, to_currency, amount)
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif choice == "2":
            print("\nAvailable Currencies:")
            print(", ".join(data["rates"].keys()))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
