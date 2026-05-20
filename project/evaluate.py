import json
import csv
import time
from executor import run_pipeline

def evaluate():
    print("Starting evaluation on benchmark dataset...")
    
    questions = []
    # Read questions
    try:
        with open('../sql_questions_only.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                if row and row[0].strip():
                    questions.append(row[0].strip())
    except Exception as e:
        print("Failed to load questions:", e)
        return

    results = []
    success_count = 0
    retry_count = 0
    
    start_time = time.time()
    
    for q in questions:
        res = run_pipeline(q, max_retries=1) # Task 3 requires max 1 retry
        
        row = {
            "Question": q,
            "Generated SQL": res["sql"],
            "Executed Successfully": "Yes" if res["status"] == "success" else "No",
            "Retry Needed": "Yes" if res["retries_used"] > 0 else "No",
            "Final Status": "Success" if res["status"] == "success" else "Failed"
        }
        results.append(row)
        
        if res["status"] == "success":
            success_count += 1
        if res["retries_used"] > 0 and res["status"] == "success":
            retry_count += 1
            
        print(f"Eval: '{q}' -> {row['Final Status']} (Retries: {res['retries_used']})")
        
    end_time = time.time()
    
    # Print Markdown Report
    print("\n# Evaluation Report\n")
    print(f"**Total Questions:** {len(questions)}")
    print(f"**Success Rate:** {success_count}/{len(questions)} ({success_count/len(questions)*100:.2f}%)")
    print(f"**Self-Correction Successes:** {retry_count}")
    print(f"**Total Time:** {end_time - start_time:.2f}s\n")
    
    print("| Question | Generated SQL | Executed Successfully | Retry Needed | Final Status |")
    print("|----------|---------------|-----------------------|--------------|--------------|")
    for r in results:
        sql_clean = r["Generated SQL"].replace("\n", " ")
        print(f"| {r['Question']} | `{sql_clean}` | {r['Executed Successfully']} | {r['Retry Needed']} | {r['Final Status']} |")

if __name__ == "__main__":
    evaluate()
