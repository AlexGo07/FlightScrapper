import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


def scrape_flights(origin, destination):
    driver = webdriver.Chrome()
    url = f"https://www.google.com/travel/flights/flights-from-{origin}-to-{destination}.html"

    driver.get(url)
    time.sleep(5)

    flights = []

    try:
        flight_elements = driver.find_elements(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/section[1]/table/tbody/tr[1]/td[1]")
        for flight in flight_elements:
            cost = flight.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/section[1]/table/tbody/tr[1]/td[1]').text
            date = flight.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/section[1]/table/tbody/tr[1]/td[2]/div[2]/span[7]').text
            duration = flight.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/section[1]/table/tbody/tr[1]/td[2]/div[2]/span[5]').text

            flights.append({
                'Origin': origin,
                'Destination': destination,
                'Date': date,
                'Cost': float(cost.replace('RON', '').replace(',', '').strip()),
                'Duration': int(re.search(r'(\d+)', duration).group(0))
            })
    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()
    return flights


def load_flights_from_file(filename='flights.csv'):
    try:
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            flights = df.to_dict('records')
            print(f"Loaded {len(flights)} flights from {filename}")
            return flights
        else:
            print("No existing flights file found. Starting with empty list.")
            return []
    except Exception as e:
        print(f"Error loading flights: {e}")
        return []


def save_to_file(flights, filename='flights.csv'):
    df = pd.DataFrame(flights)
    try:
        df.to_csv(filename, mode='a', header=False, index=False)
    except FileNotFoundError:
        df.to_csv(filename, mode='w', header=True, index=False)
    print(f"Data saved to {filename}")


def clear_file(filename='flights.csv'):
    try:
        df = pd.DataFrame(columns=['Origin', 'Destination', 'Date', 'Cost', 'Duration'])
        df.to_csv(filename, index=False)
        print(f"All flights cleared from {filename}")
    except Exception as e:
        print(f"Error clearing flights: {e}")


def sort_flights(flights, sort_by):
    if sort_by == 'cost':
        return sorted(flights, key=lambda x: x['Cost'])
    elif sort_by == 'duration':
        return sorted(flights, key=lambda x: x['Duration'])
    else:
        print("Invalid sort option.")
        return flights


def display_flights(flights):
    print("\nCurrent Flights:")
    print("-----------------------------------")
    for flight in flights:
        print(f"From {flight['Origin']} to {flight['Destination']}")
        print(f"Date: {flight['Date']}")
        print(f"Cost: RON {flight['Cost']}")
        print(f"Duration: {flight['Duration']} hr")
        print("-----------------------------------")


def display_menu():
    print("\n-----------------------------------")
    print("          FLIGHT CHECKER")
    print("-----------------------------------")
    print("1. Add New Flights")
    print("2. Sort and Display Flights")
    print("3. Clear All Flights")  # New option
    print("4. Exit")
    print("-----------------------------------")


def main():
    flights = load_flights_from_file()

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            while True:
                origin = input("Enter the origin city: ")
                destination = input("Enter the destination city: ")

                scraped_flights = scrape_flights(origin, destination)
                if scraped_flights:
                    flights.extend(scraped_flights)
                    save_to_file(scraped_flights)

                another = input("Do you want to add another flight? (yes/no): ").strip().lower()
                if another != 'yes':
                    break

        elif choice == '2':
            if not flights:
                print("No flights available to sort. Please add flights first.")
                continue

            while True:
                print("\nSort by:")
                print("1. Cost")
                print("2. Duration")
                print("3. Back to main menu")
                sort_choice = input("Select sorting option (1-3): ").strip()

                if sort_choice == '1':
                    sorted_flights = sort_flights(flights.copy(), 'cost')
                    display_flights(sorted_flights)
                elif sort_choice == '2':
                    sorted_flights = sort_flights(flights.copy(), 'duration')
                    display_flights(sorted_flights)
                elif sort_choice == '3':
                    break
                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == '3':
            confirm = input("Are you sure you want to clear all flights? (yes/no): ").strip().lower()
            if confirm == 'yes':
                clear_file()
                flights = []
                print("All flights have been cleared.")
            else:
                print("Clear operation cancelled.")

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
