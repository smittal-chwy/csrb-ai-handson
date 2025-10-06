# CSRB-AI-HANDSON 🚀

Hands-on exercises to learn about **LLMs, RAG, MCP and multiple topics in AI/GenAI/ML** in the Chewy Customer Service AI context.  
This repo is structured as progressive Jupyter notebooks.

---

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-org/CSRB-AI-HANDSON.git
   cd CSRB-AI-HANDSON

## Contribution
1. Fork main reposiroty
2. Create a handson/ branch.
3. Raise a pull-request with small **README** containing instructions  about the code and small documentation.

## Instruction 
- To create venv in project root `CSRB-AI-HANDSON/`
- There can be more than one-way to do setup, please feel free to run in your `handson` branch as per your requirements.
- Root branch instruction are as follows:

### Activate virtual env
```python
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### To upgrade pip root `CSRB-AI-HANDSON/`
```python
pip install --upgrade pip
```

### Install dependencies from root `CSRB-AI-HANDSON/`
```python
pip install -r requirements.txt
```
- We can install dependencies in dedicated jupyter notebooks also.


### Verify in your notebook
- for example: please refer hf_llm_basics.ipynb
```python
!which python
!pip list | grep transformers
```

## Note
- Put all token key-values  in .env script and .env(if you dont see create one in your handson branch) is included in gitignore so it wont commit.
- Also, .env is not requirememt, we can put all env params inside dedicated notebooks. Please remove the tokens during commit.
- Please avoid pusshing any token-keys and values.
