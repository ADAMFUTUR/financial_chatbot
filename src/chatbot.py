import pandas as pd

# Load the financial data from the CSV file
data = pd.read_csv('data/financial_data.csv')

# Define the chatbot function
def simple_chatbot(user_query, company, year):
    """
    Responds to predefined financial queries based on the user input.
    
    Parameters:
    - user_query: str, the financial question asked by the user
    - company: str, the name of the company (e.g., "Microsoft", "Tesla", "Apple")
    - year: int, the fiscal year for the data (e.g., 2023, 2022)

    Returns:
    - str, the chatbot's response based on the predefined data
    """
    # Check for total revenue query
    if user_query == "What is the total revenue?":
        revenue = data[(data['Company'] == company) & (data['Fiscal Year'] == year)]['Total Revenue'].values[0]
        return f"The total revenue for {company} in {year} was ${revenue:,}."

    # Check for net income change query
    elif user_query == "How has net income changed over the last year?":
        current_year_income = data[(data['Company'] == company) & (data['Fiscal Year'] == year)]['Net Income'].values[0]
        last_year_income = data[(data['Company'] == company) & (data['Fiscal Year'] == year - 1)]['Net Income'].values[0]
        change = (current_year_income - last_year_income) / last_year_income * 100
        return f"The net income for {company} changed by {change:.2f}% from {year - 1} to {year}."

    # Additional queries can be added here
    else:
        return "Sorry, I can only provide information on predefined queries."

# Interactive session for testing
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        company = input("Enter the company (Microsoft, Tesla, Apple): ")
        year = int(input("Enter the fiscal year: "))
        print(simple_chatbot(query, company, year))
