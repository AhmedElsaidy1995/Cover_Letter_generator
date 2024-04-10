# Cover Letter Generator

## Overview
The **Cover Letter Generator** is a web-based application that allows users to create personalized cover letters using the **FastAPI** framework and **Langchain**, which interacts with the **OpenAI API**. Whether you're applying for jobs, internships, or other opportunities, this tool streamlines the cover letter writing process.

## Features
- **FastAPI Framework**: FastAPI is an efficient web framework for building APIs with Python 3.7+ based on standard Python type hints. It provides automatic validation, serialization, and documentation.
- **Langchain Integration**: Langchain is used to interact with OpenAI's language model. It generates context-aware cover letters based on user input.
- **OpenAI API**: The powerful language model from OpenAI ensures high-quality and contextually relevant cover letters.

### Prerequisites
- **OpenAI API Key**: Obtain an API key from OpenAI.

### Installation
1. Clone this repository:
 ```bash
 git clone <repository_url>
 cd cover-letter-generator
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your OpenAI API key:
Create a .env file in the project root.
Add your API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

### Usage
Access the application at http://localhost:8000.
Enter your details (job title, company,job description) and upload your resume.
Click the “Submit” button.
The application will use Langchain and OpenAI to create a customized cover letter for you.

                                                
