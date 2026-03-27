import pandas as pd
import os
import sys

# Add the project directory to sys.path to import analyst.views
sys.path.append(os.getcwd())

# Mock Django settings for matplotlib backend
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'statbot_pro.settings')
import django
django.setup()

from analyst.views import StatBotAgent

def test_agent():
    df = pd.read_csv('test_data.csv')
    agent = StatBotAgent(df)

    queries = [
        "How many rows?",
        "Average of Sales",
        "Bar chart of Values",
        "Pie chart of Category by Quantity",
        "Line chart of Sales",
        "What is the sum of Quantity?",
        "Show a plot of Category and Sales"
    ]

    print(f"{'Query':<40} | {'Response Type':<15} | {'Result'}")
    print("-" * 80)
    for q in queries:
        response = agent.run(q)
        resp_type = "Dict (Chart)" if isinstance(response, dict) else "String"
        resp_val = response['text'] if isinstance(response, dict) else response
        print(f"{q:<40} | {resp_type:<15} | {resp_val}")

if __name__ == "__main__":
    test_agent()
