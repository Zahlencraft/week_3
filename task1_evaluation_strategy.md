# Evaluation Strategy for Text-to-SQL Agents

To evaluate the effectiveness of a Text-to-SQL agent, a multi-dimensional approach is necessary. Assessing just the exact match of the generated SQL is insufficient, as multiple SQL queries can yield the same correct result.

## Evaluation Dimensions

### 1. SQL Correctness (Execution Success)
The most fundamental metric is whether the query executes against the database without returning a syntax or semantic error.
- **Metric**: Execution Success Rate (%)
- **Definition**: Number of successful queries / Total queries.

### 2. Result Accuracy (Data Equivalence)
Instead of matching the generated SQL string against a ground truth string, we execute both queries and compare the resulting datasets.
- **Metric**: Result Exact Match Rate (%)
- **Definition**: Does the generated query result exactly match the ground truth query result? Order dependency should be ignored unless sorting is explicitly requested.

### 3. Structural Accuracy
To evaluate the model's understanding of the database schema, we check if it correctly selected the necessary tables and columns.
- **Metric**: F1 Score for Tables and Columns
- **Definition**: How well do the `FROM/JOIN` and `SELECT` clauses match the ground truth decomposition.

### 4. Error Handling & Retry Performance
An agentic system's value is in self-correction.
- **Metric**: Self-Correction Success Rate (%)
- **Definition**: (Number of queries fixed after a retry) / (Total queries that initially failed).
- **Metric**: Average Retries per Query
- **Definition**: Total number of retries / Total queries.

### 5. Latency & Performance
The time taken to generate, execute, and potentially retry the query.
- **Metric**: End-to-End Latency (ms)
- **Metric**: Query Execution Time (ms) - Is the generated query efficient?

## Evaluation Implementation for Task 3 & 4

For the pipeline built in this project, we will use the following evaluation workflow:
1. Iterate over the benchmark dataset.
2. For each natural language question, generate the SQL using the agent.
3. Track if it succeeded on the first try, or if a retry was needed (and how many).
4. Compare the SQL output execution results with the ground truth SQL execution results.
5. Generate a final report detailing the Success Rate, Result Accuracy, and Average Retries.
