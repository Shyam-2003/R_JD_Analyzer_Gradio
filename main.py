from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def chat(resume_text, job_des):
    prompt = ChatPromptTemplate.from_template(
        """You are an expert career consultant. Compare the following resume and job description:
        Resume: {resume_text}
        Job Description: {job_des}

        Analyse and provide a structured JSON response with the following fields:
        1. Job Title match: How well the job title aligns with the resume
        2. Roles and Responsibilities match: How well the roles and responsibilities in the resume align with those in the job description
        3. Years of Experience match: How well the years of experience in the resume align with those required in the job description
        4. Keywords match: How well the keywords in the resume align with those in the job description
        5. Provide a score out of 10 for each of the above fields
        6. Summary: Provide a brief summary of the overall match between the resume and job description
        7. Suggestions: Provide suggestions for improving the resume to better match the job description

        Return your result in valid JSON format only.
        """
    )

    llm = Ollama(model="gpt-oss:120b-cloud", temperature=0.1)
    parser = JsonOutputParser()

    chain = prompt | llm | parser

    response = chain.invoke({
        "resume_text": resume_text,
        "job_des": job_des
    })

    return response
