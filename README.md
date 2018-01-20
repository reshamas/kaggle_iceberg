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
- RS: notebook had CV  https://github.com/irshadqemu/Kaggle-Competitions/blob/master/Planet_amazon_resnet34.ipynb

## Done
- RS: running Grover's NB, with resnext50, increase image size sequentially (my notebook 7_5_xxx)
- RS: submit that notebook where I had 0.2258

---
# Models

## 1)  Grover's Baseline:  resnet18
* valid log_loss = 0.2918
* test  log_loss = **0.2932**  
* bs=32, image sz=75, resize 1.3x

---
## 2)  resnext50
* valid log_loss = 0.269
* test  log_loss = **0.2566**  
* notebook:  http://localhost:8888/notebooks/kaggle_iceberg/7_1_resnext50_more_epoch_submitted.ipynb
* submitted Jan 14
* bs=32, sz=150, resize 1.3, sgdr 5 epochs
* Leaderboard:  2452 of 3380 --> 78 percentile

---
## 3)  resnext50
* valid log_loss = 0.2508
* test  log_loss = **0.2394**  
* notebook:  7_6_x
* submitted Jan 20
* bs=32, sz=75, resize 1.3, sgdr 5 epochs
* Leaderboard:  2333 of 3309 --> 70.5 percentile

---
## 4)  resnext50
* valid log_loss = 0.2272
* test  log_loss = **0.2073**  
* notebook:  http://localhost:8888/notebooks/my_repos/kaggle_iceberg/7_7_resnext50_more_epoch_update_sz_zm15.ipynb
* submitted Jan 20
* bs=32, sz=75, resize 1.5, sgdr 5 epochs, lr=0.0075, dropout=0.55
* Leaderboard:  1997 of 3310 --> 60th percentile

---
## 5)  
* valid log_loss = 0.xxxx
* test  log_loss = **0.xxx**  
* notebook:  7_x
* submitted 
* bs=32, sz=150, resize 1.3, sgdr 5 epochs
* Leaderboard:  2xxx of xxxx


---
### test ??
* got 0.2258 ? resnext50, more epochs?

---

# Kaggle Rankings
- 1655 of 3310 --> 50% percentile 0.1865
- 984 of 3310 --> 29.7% percentile 0.1498
- 827 of 3310 --> 25% percentile 0.1463
- 19 of 3310 --> 0.6% percentile 0.1002
    
    
    
    
