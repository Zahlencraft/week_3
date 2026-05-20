import re

class SQLValidationError(Exception):
    pass

def validate_sql(sql: str):
    """
    Validates that the SQL query is a SELECT statement and does not contain
    any destructive commands.
    """
    sql_upper = sql.upper().strip()
    
    # Must start with SELECT
    if not sql_upper.startswith("SELECT"):
        raise SQLValidationError("Only SELECT queries are allowed.")
    
    # Block destructive keywords
    blocked_keywords = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE", "GRANT", "REVOKE", "COMMIT", "ROLLBACK"]
    
    # Check for whole words to avoid blocking columns like 'drop_off_date'
    for word in blocked_keywords:
        pattern = r'\b' + word + r'\b'
        if re.search(pattern, sql_upper):
            raise SQLValidationError(f"Query contains forbidden keyword: {word}")
            
    return True
