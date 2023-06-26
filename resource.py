from langchain import PromptTemplate, LLMChain
from huggingface_hub import hf_hub_download
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os

# This file handles the prompt and GPT modules to install locally if you're using this locally you need to change the path of the model to work

template ="""
You are a friendly chatbot assistant you are going to evaluate a Github Repo i analysed all the repos and made a report
i'm gonna give a report you just refer the below table

Table:

score                 Risk
1 - 5                 Low - Simple block
6 - 10                Low - Well structured and stable block
11 - 20               Moderate - Slightly complex block
21 - 30               More than moderate - More complex block
31 - 40               High - Complex block, alarming
41+                   Very high - Error-prone, unstable block

based on the score and you have to return only one most complex repo which has more score from report 
when the score is high thats the complex repo and
if all the repos are at the same score choose randomly one

Report: {question}

Answer:"""


prompt = PromptTemplate(template=template, input_variables=["question"])

#hf_hub_download(repo_id="dnato/ggml-gpt4all-j-v1.3-groovy.bin", filename="ggml-gpt4all-j-v1.3-groovy.bin", local_dir="/code")
local_path= os.getcwd() + "/ggml-gpt4all-j-v1.3-groovy.bin"
llm = GPT4All(model=local_path,callbacks=[StreamingStdOutCallbackHandler()] )
llm_chain = LLMChain(prompt=prompt, llm=llm)




