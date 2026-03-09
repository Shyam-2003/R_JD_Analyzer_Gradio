import gradio as gr
from PyPDF2 import PdfReader
from main import chat


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
    return text


def analyze_match(resume_file, jd_file, jd_text):
    if resume_file is None:
        return "⚠️ Please upload a resume PDF."

    job_description = ""
    if jd_text and jd_text.strip():
        job_description = jd_text
    elif jd_file is not None:
        job_description = extract_text_from_pdf(jd_file)

    if not job_description:
        return "⚠️ Please upload a job description PDF or paste the text."

    resume_text = extract_text_from_pdf(resume_file)
    result = chat(resume_text, job_description)
    return result


with gr.Blocks(title="Resume Analyser") as demo:
    gr.Markdown("# Resume and Job Description Matcher")
    gr.Markdown("Upload your resume and the job description to see how well they match!")

    with gr.Row():
        resume_input = gr.File(label="Upload your Resume (PDF)", file_types=[".pdf"])
        jd_file_input = gr.File(label="Upload Job Description (PDF)", file_types=[".pdf"])

    jd_text_input = gr.Textbox(
        label="Or paste the Job Description here",
        lines=8,
        placeholder="Paste job description text here (takes priority over uploaded PDF)...",
    )

    analyze_btn = gr.Button("Analyze Match", variant="primary")

    output = gr.JSON(label="Match Analysis Result")

    analyze_btn.click(
        fn=analyze_match,
        inputs=[resume_input, jd_file_input, jd_text_input],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch(share=True)
