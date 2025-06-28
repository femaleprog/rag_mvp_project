from sentence_transformers.cross_encoder import CrossEncoder
from llm import generate_prompt_detail_evaluation, run_mistral




def relevant_trainings(employee_evaluation : str, trainings_corpus : list[dict], top_k : int) -> list :
    
    """
    this function takes as 
    Input : 
    - employee evaluation : evaluation of an employee, very concise
    - training_corpus : list of dicts : keys : content , type, source
    - top_k : top most relevant trainings

    Output :
    - array with top k most relevant courses
    """

    output = []

    model = CrossEncoder("cross-encoder/stsb-distilroberta-base")
    
    # on détaille l'évaluation de l'employé 
    prompt = generate_prompt_detail_evaluation(employee_evaluation)

    detailed_evaluation = run_mistral(prompt)

    trainings_content = [ training['content'] for training in trainings_corpus]

    ranks = model.rank(detailed_evaluation, trainings_content)
    
    for training_dict in ranks[:top_k]:  

        output.append(trainings_corpus[training_dict["corpus_id"]])

    
    return output



