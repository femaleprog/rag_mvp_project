import sys
import json
sys.path.insert(0, '/Users/cozzy/Desktop/personal-projects/rag_test_technique/app')

from rag import relevant_trainings
from ingestion import *


def test_rag():
    
    trainings_output = []

    employees_data = load_data_annexe1('data/annexe1.json')

    training_corpus =  load_data_annexe2('data/annexe2.json')
    
    employee_evaluation = employees_data[0]['evaluation']


    trainings_output = relevant_trainings(employee_evaluation, training_corpus, 2 )
    
    assert isinstance(trainings_output, list)
    assert len(trainings_output) >= 1
    assert 'content' in trainings_output[0] 
    assert 'type' in trainings_output[0] 
    assert 'source' in trainings_output[0] 

    

    
    rag_output = open("rag_output.json", "w")

    output = {
        "Evaluation" : employees_data[0]['evaluation']
    }

    trainings = []
    for training in trainings_output :

        single_training = {
            "Content" : training['content'],
            "Type" : training['type'],
            "Source" : training['source']
        }

        trainings.append(single_training)

    output["trainings"] = trainings
    json_string = json.dumps(output, ensure_ascii=False, indent = 2)
    rag_output.write(json_string)

test_rag()
