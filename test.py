# testing the tavily tool
from tools.tavily_tool import tavily_search
# res = tavily_search("best hotels in india")
# print(res)


# testing all flight tools
from tools.flight_tool import search_flights
# res = search_flights("plan a 7 days japan trip from india ")
# print(res)

# testing travel agent tool 
from backend import run_travel_agent
user_input = input("enter travel request: ")
response = run_travel_agent(
        user_input=user_input,
        thread_id = "test_user"
)

print("\n FINAL RESPONSE: \n")
print(response["answer"])