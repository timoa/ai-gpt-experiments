# -*- coding: utf-8 -*-
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

####################
# Model
####################

# Select the model
local_path = '../../models/ggml-gpt4all-j-v1.3-groovy.bin'

####################
# Prompt
####################

# Create the prompt template
template = """Question: {question}

Answer: Let's think step by step.

"""

# Use the template to create a prompt
prompt = PromptTemplate(template=template, input_variables=['question'])

####################
# Callbacks
####################

# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]

# Verbose is required to pass to the callback manager
llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

####################
# Chains
####################

# Link the language model with our prompt template
llm_chain = LLMChain(prompt=prompt, llm=llm)

####################
# Question
####################

# Hardcoded question
question = """
What Formula 1 pilot won the championship in the year
 Leonardo di Caprio was born?"""

# User input question...
# question = input("Enter your question: ")

####################
# Run
####################

# Run the query and get the results
llm_chain.run(question)
