# test_chatbot.py
from src.chatbot import simple_chatbot

def test_total_revenue():
    assert simple_chatbot("What is the total revenue?", "Microsoft", 2023) == "The total revenue for Microsoft in 2023 was 200000."

def test_net_income_change():
    assert "The net income for Tesla changed" in simple_chatbot("How has net income changed over the last year?", "Tesla", 2023)

# Run tests
if __name__ == "__main__":
    test_total_revenue()
    test_net_income_change()
    print("All tests passed!")
