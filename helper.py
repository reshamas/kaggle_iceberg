import pandas as pd
import numpy as np
import os

def make_test_file(log_preds,test_df,model_name,classes,submission_folder):
    probs = np.exp(log_preds)
    probs = np.mean(probs,axis=0)
    df = pd.DataFrame(probs)
    df.columns = classes
    df['id'] = test_df['id']
    df=df.drop('ship',axis=1)
    df=df.rename(columns={'ice':'is_iceberg'})
    SUBM = f'{submission_folder}/{model_name}'
    os.makedirs(SUBM, exist_ok=True)
    df.to_csv(f'{SUBM}subm.gz', compression='gzip', index=False)
    print(f"Saving to {SUBM}subm.gz")