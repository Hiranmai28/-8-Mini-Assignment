#8-Mini-Assignment
CS 5340 #8 Mini Coding Assignment.
# Greetings with Hugging Face

A simple interactive Streamlit application that uses the Hugging Face Inference API (GPT-2) to generate a creative "Hello World" message. This project demonstrates how to integrate generative AI into a web app, securely manage API keys, and deploy the application on Streamlit Cloud.

## Overview
This project is built with Python and Streamlit. It leverages the Hugging Face Inference API to generate a greeting message based on a simple prompt. Sensitive API credentials are managed securely using environment variables and the secrets management feature on Streamlit Cloud.

## Task Details

### 1. API Selection

- **API Choice:**  
  The project utilizes the Hugging Face Inference API with the GPT-2 model (`openai-community/gpt2`).

- **Access and Authentication:**  
  An API token is required to access the Hugging Face API. During development, the token is stored in a local `.env` file. For production, Streamlit Cloud Secrets are used to ensure the token remains secure.

### 2. Application Development

- **Technology Stack:**  
  - Python  
  - [Streamlit](https://streamlit.io/) for the interactive web interface  
  - [requests](https://docs.python-requests.org/) for HTTP calls  
  - [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management

- **Functionality:**  
  The application sends a prompt to the Hugging Face API and displays the generated "Hello!" message on a simple interactive page.

### 3. "Hello World" Generative Task

- **Prompt:**  
  The prompt used is:  
  "Hello! Welcome to the interactive page. How are you doing?"

- **Response Handling:**  
The app processes the API's response. If the generated text starts with the original prompt, it returns the prompt; otherwise, it returns the full generated text.

### 4. Documentation

- **Code Comments:**  
The code is well-documented witsh inline comments explaining key steps such as API call construction, error handling, and response parsing.

- **Setup Instructions:**  
Detailed instructions for setting up the project locally and deploying on Streamlit Cloud are provided in this README.

### 5. Reflection

- **Experience:**  
This project provided valuable insights into integrating generative AI into a web application. It also highlighted the importance of secure API key management.

- **Challenges:**  
One of the main challenges was ensuring that sensitive credentials were not exposed. This was mitigated by using environment variables locally and Streamlit Cloud secrets for production.

- **Future Applications:**  
The skills and lessons learned here can be applied to more complex AI-driven projects, allowing for secure and scalable integrations with generative APIs.
