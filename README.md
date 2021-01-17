[![Build Status](https://travis-ci.org/aws-samples/amazon-sagemaker-bert-classify-pytorch.svg?branch=master)](https://travis-ci.org/aws-samples/amazon-sagemaker-bert-classify-pytorch)

# Amazon Sagemaker BERT text classification using PyTorch
 
 We train  Stanford Sentiment Treebank - 2 (SST2) using BERT
 
 ## Dataset
 We use the [ Stanford Sentiment Treebank - 2](https://nlp.stanford.edu/sentiment/index.html)
 
 ## Setting up locally
 1. Install python 3.7.4
 
 1. Set up requirements. 
    
    ```bash
    pip install -r tests/requirements.txt
    ```
    
 1. Verify set up
    
    ```bash
    export PYTHONPATH=./src
    pytest
    ```
    

 ## SST2
 
1. Preprocess data to split data into train , test and val sample files and save them to `processdata` directory
      
    ```bash
    export PYTHONPATH=src
    datadir=tmp
    
    python src/utils/sst2_split_utils.py --sentencefile $datadir/datasetSentences.txt  --sentiment $datadir/sentiment_labels.txt  --dictionary $datadir/dictionary.txt --split $datadir/datasetSplit.txt --outdir processdata
    ```