# Flight Price Checker

#### Video Demo: <https://youtu.be/clU7cSsxF78>

#### Description:
Flight Price Checker is a Python application that helps users track and compare flight prices. The program scrapes flight information from Google Flights, allows users to sort flights by different criteria, and maintains a record of flight data for future reference.

## Features

- **Flight Data Scraping**: Automatically retrieves flight information including:
  - Price
  - Duration
  - Dates
  - Origin and destination cities

- **Sorting Capabilities**: Sort flights by:
  - Cost (ascending order)
  - Duration (ascending order)

- **Data Management**:
  - Save flight information to CSV file
  - Load existing flight data
  - Clear all saved flights
  - View sorted flight information in console

## Project Structure

- `project.py`: Main program file containing core functionality
- `test_project.py`: Test suite for the program
- `requirements.txt`: List of required Python packages
- `flights.csv`: CSV file storing flight data (created when program runs)

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/AlexGo07/FlightScrapper.git>
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Ensure you have Chrome WebDriver installed for Selenium

## Usage

1. Run the program:
```bash
python project.py
```

2. Choose from the following options:
   - Add New Flights: Search and add flights to database
   - Sort and Display Flights: View flights sorted by cost or duration
   - Clear All Flights: Remove all saved flight data
   - Exit: Close the program

## Functions

### `scrape_flights(origin, destination)`
Scrapes flight information from Google Flights for specified routes.
- Parameters:
  - `origin`: Departure city
  - `destination`: Arrival city
- Returns: List of dictionaries containing flight information

### `sort_flights(flights, criteria)`
Sorts flight data based on specified criteria.
- Parameters:
  - `flights`: List of flight dictionaries
  - `criteria`: Sorting criterion ('cost' or 'duration')
- Returns: Sorted list of flights

### `load_flights(filename='flights.csv')`
Loads existing flight data from CSV file.
- Parameters:
  - `filename`: Name of CSV file (default: 'flights.csv')
- Returns: List of flight dictionaries

## Testing

Run tests using pytest:
```bash
pytest test_project.py
```

## Dependencies

- Python 3.6+
- Selenium
- Pandas
- Pytest
- Chrome WebDriver

## Design Choices

1. **Selenium Web Scraping**: 
   - Chosen for reliable data extraction from dynamic web pages
   - Allows automation of flight searches

2. **CSV Storage**:
   - Simple and efficient data storage

3. **Modular Structure**:
   - Separate functions for different features

## Future Improvements

- Add support for more flight search engines
- Implement price tracking over time
- Add email notifications for price drops
- Include more sorting criteria (e.g., number of stops)
- Add graphical user interface

## Author

Gorgan Alexandru

