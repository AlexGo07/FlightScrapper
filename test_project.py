import pytest
from project import sort_flights, load_flights_from_file, scrape_flights
import os
import pandas as pd


def test_sort_flights():
    #creating sample data to test the functions
    test_flights = [
        {'Origin': 'Cluj', 'Destination': 'London', 'Date': '2024-01-20', 'Cost': 200, 'Duration': 4},
        {'Origin': 'Cluj', 'Destination': 'Paris', 'Date': '2024-01-21', 'Cost': 150, 'Duration': 3},
        {'Origin': 'Cluj', 'Destination': 'Rome', 'Date': '2024-01-22', 'Cost': 300, 'Duration': 5}
    ]

    sorted_by_cost = sort_flights(test_flights, 'cost')
    assert sorted_by_cost[0]['Cost'] == 150
    assert sorted_by_cost[-1]['Cost'] == 300

    sorted_by_duration = sort_flights(test_flights, 'duration')
    assert sorted_by_duration[0]['Duration'] == 3
    assert sorted_by_duration[-1]['Duration'] == 5


def test_load_flights_from_file(tmp_path):
    test_flights = [
        {'Origin': 'Cluj', 'Destination': 'London', 'Cost': 200, 'Duration': 4},
        {'Origin': 'Cluj', 'Destination': 'Paris', 'Cost': 150, 'Duration': 3}
    ]
    test_file = tmp_path / "test_flights.csv"
    pd.DataFrame(test_flights).to_csv(test_file, index=False)

    # Test loading flights
    loaded_flights = load_flights_from_file(test_file)
    assert len(loaded_flights) == 2
    assert loaded_flights[0]['Origin'] == 'Cluj'
    assert loaded_flights[1]['Destination'] == 'Paris'


def test_scrape_flights():
    flights = scrape_flights('cluj', 'london')

    assert isinstance(flights, list)
    if flights:
        assert all(key in flights[0] for key in ['Origin', 'Destination', 'Date', 'Cost', 'Duration'])
