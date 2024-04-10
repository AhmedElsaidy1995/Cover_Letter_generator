# Cover Letter Generator

## Overview
The **Cover Letter Generator** is a web-based application that allows users to create personalized cover letters using the **FastAPI** framework and **Langchain**, which interacts with the **OpenAI API**. Whether you're applying for jobs, internships, or other opportunities, this tool streamlines the cover letter writing process.

## Features
- **FastAPI Framework**: FastAPI is an efficient web framework for building APIs with Python 3.7+ based on standard Python type hints. It provides automatic validation, serialization, and documentation.
- **Langchain Integration**: Langchain is used to interact with OpenAI's language model. It generates context-aware cover letters based on user input.
- **OpenAI API**: The powerful language model from OpenAI ensures high-quality and contextually relevant cover letters.

## Getting Started
To get started with the Cover Letter Generator, follow these steps:

### Prerequisites
Make sure you have the following installed:
- **Python 3.7+**: You'll need Python to run the application.
- **FastAPI**: Install FastAPI using pip:
pip install fastapi

- **Uvicorn**: Uvicorn is used to serve the FastAPI application. Install it with:

pip install uvicorn

- **Langchain**: Set up Langchain to communicate with the OpenAI API.
- **OpenAI API Key**: Obtain an API key from OpenAI.

### Installation
1. Clone this repository:
 ```bash
 git clone <repository_url>
 cd cover-letter-generator

2. Install the required dependencies:
pip install -r requirements.txt

3. Configure your OpenAI API key:
Create a .env file in the project root.
Add your API key:
OPENAI_API_KEY=your_api_key_here

4. Run the application:
uvicorn main:app --reload

### Usage
Access the application at http://localhost:8000.
Enter your details (e.g., name, job title, company) and any specific context for the cover letter.
Click the “Generate Cover Letter” button.
The application will use Langchain and OpenAI to create a customized cover letter for you.

                                                