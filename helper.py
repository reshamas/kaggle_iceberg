import pandas as pd
import numpy as np
import os
import PIL
import matplotlib.pyplot as plt

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
    

    
def make_submission(learn,data,output_file_name):
    log_preds,y = learn.TTA(is_test=True)
    # get file names
    file_ids = []
    for test_idx,test_filename in enumerate(data.test_dl.dataset.fnames):
        _,fname = os.path.split(test_filename)
        file_id,ext = os.path.splitext(fname)
        file_ids.append(str(file_id))
        
    test_probs = np.mean(np.exp(log_preds)[:,:,0] ,axis=0)
    # joining id and probability
    d = {'id': file_ids, 'is_iceberg': test_probs}
    submit_df = pd.DataFrame(data=d)#.sort_values('id')

    submit_df.to_csv(output_file_name, index = None)
    

def plots(ims, figsize=(12,6), rows=1, titles=None):
    f = plt.figure(figsize=figsize)
    for i in range(len(ims)):
        sp = f.add_subplot(rows, len(ims)//rows, i+1)
        sp.axis('Off')
        if titles is not None: sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i])
    
    
def load_img_id(ds, idx,path): return np.array(PIL.Image.open(path+ds.fnames[idx]))

def mask(probs,actual_y,label=0,condition=True,size=5):
    predicted_y = np.argmax(probs,axis=1)
    
    if condition:
        idxs = np.where((predicted_y==actual_y) & (actual_y==label))[0]
    else:
        idxs = np.where((predicted_y!=actual_y) & (actual_y==label))[0]
    
    relevant_probs = probs[:,label]
    
    
    sorted_idxs = idxs[np.argsort(relevant_probs[idxs])]
    if condition == True:
        return sorted_idxs[-size:]
    else:
        return sorted_idxs[:size]
    
    #return idxs[np.argsort(relevant_probs[idxs])[::-1][:size]]

    

def mask_pandas(probs,actual_y,label=0,condition=True,size=5):
    predicted_y = np.argmax(probs,axis=1)
    df3 = pd.DataFrame({'actual_y':actual_y,'predicted_y':predicted_y,'prob':probs[:,label]})
    
    if condition == True:
        sorted_df =  df3[df3['actual_y']==df3['predicted_y']].sort_values(['prob'],ascending=False)
    else:
        sorted_df = df3[df3['actual_y']!=df3['predicted_y']].sort_values(['prob'],ascending=True)
    
    print (sorted_df.head(size))
    return sorted_df[:size].index
    
def plot(data,probs,actual_y,image_path,label=0,condition=True,class_map={0:'ice',1:'ship'}):
    
    #idxs = mask(probs,actual_y,label=label,condition=condition)
    idxs = mask_pandas(probs,actual_y,label=label,condition=condition)

    imgs = [load_img_id(data.val_ds,x,image_path) for x in idxs]
    title_probs = [probs[x][label] for x in idxs]
    
    predicting_class = class_map[label]
    cond_str = "incorrectly classified"
    if condition:
        cond_str = "correctly classified"
    title = f"Most {cond_str} for {predicting_class}"
    
    print(title)
    return plots(imgs, rows=1, titles=title_probs, figsize=(16,8)) 