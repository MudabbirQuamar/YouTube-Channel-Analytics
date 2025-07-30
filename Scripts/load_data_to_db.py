import sys
import os

# Add project root directory to sys.path
project_root = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from db.connection import get_engine
from transform_data import extract_data_from_json,cleaning_data,transform_data,tag_analysis

engine= get_engine() # create a new _engine.engine instance

#saving df to the postgre tables
structured_data= extract_data_from_json()
structured_data.to_sql("structure_data",engine,index=False,if_exists="replace")
cleaned_data = cleaning_data(structured_data)
cleaned_data.to_sql("clean_data",engine,index=False,if_exists="replace")
transformed_data= transform_data(cleaned_data)
transformed_data.to_sql("transformed_data",engine,index=False,if_exists="replace")
tag_analyzed_data = tag_analysis(transformed_data)
tag_analyzed_data.to_sql("tag_analyzed_data",engine,index=False,if_exists="replace")




# Verification step
from db.connection import get_engine
import pandas as pd

engine = get_engine()
df = pd.read_sql("SELECT * FROM transformed_data LIMIT 5", con=engine)
print("\n✅ Sample data from structure_data table:")
print(df)

