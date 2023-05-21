# GPT Experiments

Experimentations related to run a local ChatGPT with privacy in mind.
The goal is to try to use only open-source models/LLMs and tools to keep the data private.

Next step will be to expose the model as a service to be able to use it thru an API, and integrate it into as a ChatBot, mobile app or website.

Currently, it is written in Python, but I hope to be able to convert it in TypeScript when there will be more library available.

## Introduction

To start, I'm using [GPT4All][gpt4all-website] to run a local ChatGPT model instead of using the OpenAI API.

[GPT4All][gpt4all-website] is an open-source project that aims to provide a simple way to run a local GPT model ([GitHub][gpt4all-github]).

To provide more connectivity and features, I'm using [Langchain][langchain-website] to connect to the model and provide a simple CLI to interact with it ([GitHub][langchain-github]).

## Roadmap

- [x] Configure GPT4All to run locally
- [x] Integrate Langchain with GPT4All
- [x] Create a simple Question & Answering system (CLI)
- [ ] Ingest PDF files and ask question about the content (CLI)

## Installation

[gpt4all-website]: https://gpt4all.com/
[gpt4all-github]: https://github.com/nomic-ai/gpt4all
[langchain-website]: https://langchain.io/
[langchain-github]: https://github.com/hwchase17/langchain
