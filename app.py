from fastapi import FastAPI, Request, File, UploadFile,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-cover-letter/")
async def handle_form(request: Request, cv: UploadFile = File(...),job_title: str = Form(...), job_description: str = Form(...), company_name: str = Form(...)):
    # Get PDF Text
    pdf_text = read_pdf(cv.file)

    letter = generate_letter(pdf_text,job_title,job_description,company_name)
    return {"cover_letter": letter}

def generate_letter(resume,job_title,job_description,company_name):
    prompt = """
        You are a helpful assistant who's job is to write cover letters.
        You will be given a resume, job title , the company and job description information as context.
        The cover letter should have 3 concise paragraphs only.
        Be very specfic to why the resume fits the job, and use a lot of specifics about the company. 
         
        resume: {resume}
        job description: {job_description}
        title: {position}
        company: {company}

        Cover Letter:       
"""
    llm = ChatOpenAI(model_name='gpt-3.5-turbo',temperature=0.2,openai_api_key=openai_api_key)
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )

    args = {
        "resume": resume,
        "job_description": job_description,
        "position": job_title,
        "company": company_name
        }
    result = llm_chain.run(args)
    return result


def read_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)

    # Collect text from pdf
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
