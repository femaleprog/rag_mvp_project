import sys
import pytest
import json

sys.path.insert(0, '/Users/cozzy/Desktop/personal-projects/rag_test_technique/app')

from ingestion import *
from recommendation import generate_report, generate_global_report

def test_generate_report():
    
    employees_data = load_data_annexe1("data/annexe1.json")
    trainings = load_data_annexe2("data/annexe2.json")

    reports = generate_report(employees_data[:2], trainings, 1)
    
    assert isinstance(reports, list)
    assert len(reports) != 0
    assert "employee_name" in reports[0]
    assert "evaluation" in reports[0]
    assert "score" in reports[0]
    assert "recommended_trainings" in reports[0]

    global_report = generate_global_report(reports)
    
    assert isinstance(global_report, dict)
    assert len(global_report) != 0
    assert "individual_reports" in global_report
    
    report = open("report.json", 'w')

    json_string = json.dumps(global_report, ensure_ascii=False, indent =2)

    report.write(json_string)

test_generate_report()