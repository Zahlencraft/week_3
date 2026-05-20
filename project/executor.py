import time
from database import execute_query
from sql_generator import SQLGenerator
from validator import validate_sql, SQLValidationError

generator = SQLGenerator()

def run_pipeline(question: str, max_retries=3):
    logs = []
    
    start_time = time.time()
    
    # Step 1: Understand (Decompose)
    decomposition = generator.decompose(question)
    logs.append({"step": "decomposition", "status": "success", "data": decomposition})
    
    # Step 2: Generate Initial SQL
    sql = generator.generate_sql(question, decomposition)
    logs.append({"step": "generation", "status": "success", "sql": sql})
    
    attempt = 0
    final_result = None
    final_sql = sql
    success = False
    
    while attempt <= max_retries:
        try:
            # Validate
            validate_sql(final_sql)
            
            # Execute
            db_res = execute_query(final_sql)
            if db_res["success"]:
                final_result = db_res["data"]
                success = True
                logs.append({"step": f"execution_attempt_{attempt}", "status": "success"})
                break
            else:
                raise Exception(db_res["error"])
                
        except Exception as e:
            error_msg = str(e)
            logs.append({"step": f"execution_attempt_{attempt}", "status": "failed", "error": error_msg})
            
            if attempt < max_retries:
                # Retry: Fix SQL
                final_sql = generator.fix_sql(question, final_sql, error_msg)
                logs.append({"step": f"retry_{attempt+1}_generation", "sql": final_sql})
            
        attempt += 1

    end_time = time.time()
    execution_time_ms = round((end_time - start_time) * 1000, 2)
    
    return {
        "question": question,
        "sql": final_sql,
        "result": final_result if success else [],
        "status": "success" if success else "failed",
        "retries_used": attempt if not success else attempt, # if success, attempt is exactly retries used.
        "logs": logs,
        "execution_time_ms": execution_time_ms
    }
