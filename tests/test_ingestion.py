

import sys
import pytest
sys.path.insert(0, '/Users/cozzy/Desktop/personal-projects/rag_test_technique/app')

from ingestion import *

def test_load():

    loaded_data2 = load_data_annexe2("data/annexe2.json")
    loaded_data1 = load_data_annexe1("data/annexe1.json")

    assert isinstance(loaded_data2, list)
    assert len(loaded_data2) > 0

    assert isinstance(loaded_data1, list)
    assert len(loaded_data1) > 0

def test_clean_data():
    data = { 'evaluation' : 'technically good but has a communication \n problems'}
    cleaned_data = clean_data(data) 
    assert "\n" not in  cleaned_data['evaluation']

test_load()
test_clean_data()

