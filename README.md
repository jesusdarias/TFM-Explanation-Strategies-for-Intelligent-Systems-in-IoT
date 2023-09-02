# TFM-Explanation-Strategies-for-Intelligent-Systems-in-IoT

This repository contains the code associated with my master's degree final project: "Explanation Strategies for Intelligent Systems in IoT". The **"Notebooks"** folder contains the jupyter notebooks with the code for the training of the use case models, as well as the execution of the explainers for replication of the results. It also contains the proposed explanation strategies in json format which can be imported from the [iSee Explanation Experience Editor](https://editor-dev.isee4xai.com/).

The **"src"** folder contains the code for the implementations and wrappers of the explanation methods utilized in the experiments adapted to the web service format used in iSee. If you want to launch the server locally to test the explainers using the requests from the notebooks, see the next section.

## Getting Explanations from the local server

To launch the explainability server, follow these steps:

1) From the root folder, create a virtual environment for the installation of the required libraries with:

           
```console
python -m venv .
```
                
            
2) Use pip to install the dependencies from the requirements file.

```console
pip install -r requirements.txt
```
            
3) Once all the dependencies have been installed, execute the script to launch the server with:

```console
python app.py
```

Now you can make requests to the local server. You can use the example requests from the notebooks by changing the url to http://localhost:5000/...
