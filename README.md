# Welcome to "Azure ML Training" Workshop!

<!-- 
Guidelines on README format: https://review.docs.microsoft.com/help/onboard/admin/samples/concepts/readme-template?branch=master

Guidance on onboarding samples to docs.microsoft.com/samples: https://review.docs.microsoft.com/help/onboard/admin/samples/process/onboarding?branch=master

Taxonomies for products and languages: https://review.docs.microsoft.com/new-hope/information-architecture/metadata/taxonomies?branch=master
-->

## Overview 
This repository contains content of a two part workshop of using Tensorflow 2.0 on Azure Machine Learning service. The different components of the workshop are as follows:

- Part 1: [Model Training](https://github.com/microsoft/bert-stack-overflow/blob/master/1-Training/AzureServiceClassifier_Training.ipynb)
- Part 2: [Inferencing and Deploying a Model](https://github.com/microsoft/bert-stack-overflow/blob/master/2-Inferencing/AzureServiceClassifier_Inferencing.ipynb)

The workshop demonstrates end-to-end Machine Learning workflow on the example of training a [BERT](https://arxiv.org/pdf/1810.04805.pdf) model to automatically tag questions on Stack Overflow.


## Getting started with the workshop environment

1. Login to Azure ML studio

    * Navigate to: [https://ml.azure.com](https://ml.azure.com).
    * In the Welcome screen select preprovisioned subcription "AzureML Nursery" and workspace "mltraining-westeurope-N-ws". Select N based on the workspace assigned to you:
    ![](1-Training/images/studio-sign-in.png)

2. Create Azure Machine Learning Notebook VM

    * Click on **Compute** tab on the left navigation bar.
    * In the Notebook VM section, click **New**.
    * Enter Notebook VM name of your choice and click **Create**. Creation should take approximately 5 minutes.

3. Clone this repository to Notebook VM in your Azure ML workspace

    * Once Notebook VM is created and is in Running state, click on the **Jupyter** link. This will open Jupyter web UI in new browser tab.
    * In Jupyter UI click **New > Terminal**.
    * In terminal window, type and execute command: `ls`
    * Notice the name of your user folder and use that name to execute next command: `cd <userfolder>`
    * Clone the repository of this workshop by executing following command: `git clone https://github.com/maxluk/bert-azureml-training.git`

4. Open Part 1 of the workshop

    * Go back to the Jupyter window.
    * Navigate to `bert-azureml-training/1-Training/` folder.
    * Open `AzureServiceClassifier_Training.ipynb` notebook.

You are ready to start training your model! Have fun.
