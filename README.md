## AI Soulmate

### Introduction

The project is an interactive AI character - all running locally using the Nexa SDK. We presuppose some uncensored models in the model list that perform well. Of course, you can also go to the [Nexa Model Hub](https://nexaai.com/models) to find the model you want to try or run your own local model. You can also adjust the character Settings yourself through the Streamlit UI.

- Key features:

  - Uncensored model
  - No privacy concerns


### Installation
#### Prerequisite
1. Setup [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/) and create new conda virtual environment

2. Download [Nexa SDK](https://github.com/NexaAI/nexa-sdk)
   

#### Text Only

1. Install required packages:

```
pip install -r requirements.txt
```

2. Usage:

- Run the Streamlit app: 
  ```
  streamlit run text_only/app.py
  ```
- Start a chat with text


### File Structure


  - `app.py`: main Streamlit app
  - `utils/initialize.py`: initialize chat and load model
  - `utils/gen_response.py`: handle output
  - `utils/customize.py`: allow users to customize roles


### Resources

- [NexaAI | Model Hub](https://nexaai.com/models)
- [GitHub | Nexa-SDK](https://github.com/NexaAI/nexa-sdk)
