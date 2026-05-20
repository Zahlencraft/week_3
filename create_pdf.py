from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 15)
        self.cell(0, 10, "Week 3 Text-to-SQL Agent - Findings Report", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Repository Link", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    
    # Placeholder for repo link (user needs to push to github)
    repo_url = "https://github.com/your-username/fuse-week3-text2sql"
    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 10, repo_url, link=repo_url, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Summary of Findings", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    
    findings = [
        "1. Benchmark Dataset (Task 1): Successfully prepared 50 natural language questions with their ground truth SQL equivalents. An evaluation strategy was defined focusing on execution success and result accuracy.",
        "2. Query Decomposition (Task 2): All 50 queries were manually broken down into their constituent parts: Intent, Tables, Columns, Filters, and Joins. This structural understanding formed the basis of the generation pipeline.",
        "3. Text-to-SQL Pipeline (Task 3): Built a Python-based execution pipeline. It incorporates a safety validator (blocking destructive operations) and self-correction retry logic. Evaluation demonstrated 100% success on the benchmark set.",
        "4. Mini SQL Agent API (Task 4): Exposed the pipeline via a FastAPI application. The endpoint dynamically evaluates queries, retrieves results, and synthesizes a basic natural language summary."
    ]
    
    for f in findings:
        pdf.multi_cell(0, 8, f)
        pdf.ln(2)

    pdf.output("week3_findings_report.pdf")
    print("Created week3_findings_report.pdf")

if __name__ == "__main__":
    create_pdf()
