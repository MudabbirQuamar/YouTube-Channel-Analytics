import os
from transform_data import extract_data_from_json,cleaning_data,transform_data,tag_analysis

os.makedirs("Data/Processsed_data",exist_ok=True)

def load_to_csv():

    structured_data=extract_data_from_json()
    structured_data.to_csv("../Data/Processed_data/structured_data.csv",index=False)
    clean_data=cleaning_data(structured_data)
    clean_data.to_csv("../Data/Processed_data/cleaned_data.csv",index=False)
    transformed_data=transform_data(clean_data)
    transformed_data.to_csv("../Data/Processed_data/transformed_data.csv",index=False)
    tag_analyzed_data=tag_analysis(transformed_data)
    tag_analyzed_data.to_csv("../Data/Processed_data/tag_analyzed_data.csv",index=False)


if __name__=="__main__":
    load_to_csv()