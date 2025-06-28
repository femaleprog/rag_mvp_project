from rag import relevant_trainings
from ingestion import *
from llm import run_mistral, generate_synthese



def generate_report(employees_data : list[dict], training_data : list[dict], top_k : int = 1) -> list: 

    """

    Generate a structured report for each employee
    
    """

    reports = []

    for employee in employees_data :

        employee_report = {
            "employee_name" : employee['employe'],
            "evaluation" : employee['evaluation'],
            "score"  : employee['score'],
            "recommended_trainings" : relevant_trainings(employee['evaluation'], training_data, top_k)
        }
        
        reports.append(employee_report)

        

    
    return reports






def generate_global_report(reports : list[dict]) -> list[dict] :
    
    global_report = {
        "Number of employees" : len(reports)
        
    } 

    for report in reports:

        prompt = generate_synthese(report)
        synthese = run_mistral(prompt)
        report["synthèse"] = clean_data(synthese)

    global_report["individual_reports"] = reports

    return global_report


