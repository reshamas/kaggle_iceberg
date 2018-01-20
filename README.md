# Kaggle Competition


## Statoil/C-CORE Iceberg Classifier Challenge
### Ship or iceberg, can you decide from space?

https://www.kaggle.com/c/statoil-iceberg-classifier-challenge  

### References
Grover's notebook:  https://github.com/groverpr/deep-learning/blob/master/image_comp_1_2.ipynb

---
## To Do
- add incidence angle
- cross validation
- stacking of models (ensembling)
- look at, within various models, which images are being misclassified
- RS: running Grover's NB, with resnext50, increase image size sequentially (my notebook 7_5_xxx)
- RS: notebook had CV  https://github.com/irshadqemu/Kaggle-Competitions/blob/master/Planet_amazon_resnet34.ipynb
- RS: submit that notebook where I had 0.22


---
# Models

## Grover's Baseline:  resnet18
* valid log_loss = 0.2918
* test  log_loss = **0.2932**  
* bs=32, image sz=75, resize 1.3x

---
## resnext50
* valid log_loss = 0.269
* test  log_loss = **0.2566**  
* notebook:  http://localhost:8888/notebooks/kaggle_iceberg/7_1_resnext50_more_epoch_submitted.ipynb
* submitted Jan 14
* bs=32, sz=150, resize 1.3, sgdr 5 epochs

---
## resnext50
* valid log_loss = 0.2508
* test  log_loss = **0.2394**  
* notebook:  7_6_x
* submitted Jan 20
* bs=32, sz=150, resize 1.3, sgdr 5 epochs
* Leaderboard:  2333 of 3309


    
###
got 0.235 sz=150, zm 1.5


---
    
### resnext50 (log_loss = 0.248)
    - follow Grover's other defaults
    - resize 1.3x
    

### resnext50 (log_loss = 0.249)
    - follow Grover's other defaults
    - resize 1.5x
    
   
### resnext50 (log_loss = 0.250)
    - follow Grover's other defaults
    - resize 1.2x
    - zoom 1.2
    
    
    
    
    
