from app.ingestion import load_data

def main():
    incomplete_evaluations_path = "data/annexe1.json"
    incomplete_evaluations = load_data(incomplete_evaluations_path)

main()