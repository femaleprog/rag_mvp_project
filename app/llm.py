from mistralai import Mistral
import requests
import numpy as np

import os
from getpass import getpass

from dotenv import load_dotenv

load_dotenv()

API = os.getenv('API')
api_key = os.getenv('MISTRAL_API_KEY')
client = Mistral(api_key=api_key)



def generate_prompt_detail_evaluation(evaluation: str):
    prompt = f"""
    Tu es un assistant RH
    Voici l'évaluation d'un employé :
    {evaluation}
    
    Peux tu détailler cette évaluation en 3 phrases, en mettant l'accent sur les 
    domaines ou l'employé doit monter en compétences grace à des formations. Sois claire
    et structurée. N'inclus pas de charactères speciaux. 

    Exemple : 

    Evaluation : Besoins de renforcer la gestion de projet et la communication.

    Evalution détaillée : Cette personne devrait développer ses capacités à gérer des projets et à bien communiquer avec les autres. Elle a besoin d'une formation qui va l'aider à 
    perfectionner dans le pilotage de projets et dans la mise en pratique de nouvelles méthodologies et approches sur des projets. Cette formation devrait aussi lui apprendre à exprimer et structurer ses idées,
    savoir planifier et respecter des délais.

     """
    return prompt



def generate_prompt_recommendation(recommendation : dict):

    prompt = f"""
    Tu es un assistant RH expert.

    Voici les informations de l'employé :

    Nom de l'employé : {recommendation['employee_info']['employe']}
    Evaluation : {recommendation['employee_info']['evaluation']}
    Score : {recommendation['employee_info']['score']}

    Voici une liste des formations recommandées pour cet employé:
     {recommendation['relevant_trainings']} 

    Peux-tu générer un rapport pour cet employé détaillé présentant des recommandations
    personnalisées pour le développement des compétences.

    Exemple : 

    - Employée : Emilie Sanchez
    - Evaluation : Besoin de renforcer ses compétences en management 
                   des projets.
    - Score : 60
    - Trainings : 

      - Training 1 : 
          Contenu : 
        
    

    """
    return prompt

def generate_synthese(employee_report : dict):

    prompt = f"""
    Tu es un assistant RH expert.

    Voici le rapport d'un comployé :
    {employee_report}
    
    Peux tu faire une synthese concise, structurée et claire sous le format suivant :

    - Points forts  : ( si non mentionné, dit non mentionnés )
    - Points à améliorer :  ( soit concis )
    - Domaines de formations recommandées :  (domaine de formation, liste maximum 3)

    N'inclus pas de charactères spéciaux et donne directement la réponse sans justification.
    Termine tes phrases par un point.
    """
    return prompt

def run_mistral(user_message, model="mistral-large-latest"):
    
    messages = [
        {
            "role": "user", "content": user_message
        }
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )
    
    return (chat_response.choices[0].message.content)

