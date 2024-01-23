from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluation

@pipeline
def train_pipeline():
    
    df = ingest_data()
    clean_data(df)
    train_model(df)
    evaluation(df)