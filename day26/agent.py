import json
import os
from typing import TypedDict

from langgraph.graph import StateGraph, END

MEMORY_FILE = "memory.json"

class AgentState(TypedDict):
    question: str
    reasoning: str
    tool_result: str
    final_answer: str
    history: list

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"preferred_airline": "Any", "preferred_seat": "Aisle"}

def save_memory(memory_data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory_data, file, indent=2)

def search_flights_tool(state):
    question = state["question"].lower()
    if "hyderabad" in question and "bangalore" in question:
        return "Flight A: 8:00 AM, 4500 INR; Flight B: 11:30 AM, 5200 INR"
    if "flight" in question or "search" in question or "book" in question:
        return "Flight A: 8:00 AM, 4500 INR; Flight B: 11:30 AM, 5200 INR"
    return "No flights found"

def reason_node(state):
    memory = load_memory()
    state["history"].append("Reason: decide what to do next")
    question = state["question"].lower()

    if "seat" in question:
        state["reasoning"] = f"Use memory preference: {memory.get('preferred_seat', 'Aisle')} seat"
    elif "airline" in question:
        state["reasoning"] = f"Use memory preference: {memory.get('preferred_airline', 'Any')} airline"
    elif any(word in question for word in ["flight", "book", "search", "time", "when"]):
        state["reasoning"] = "Need to search for flights first"
    else:
        state["reasoning"] = "This question does not need the flight tool"

    return state

def act_node(state):
    state["history"].append("Act: call search tool")
    state["tool_result"] = search_flights_tool(state)
    return state

def observe_node(state):
    state["history"].append("Observe: read tool result")
    return state

def final_node(state):
    if "No flights found" in state["tool_result"]:
        state["final_answer"] = "I could not find flights based on the tool result."
    elif state["reasoning"].startswith("Use memory preference:"):
        state["final_answer"] = state["reasoning"]
    elif state["reasoning"] == "This question does not need the flight tool":
        state["final_answer"] = "I only handle flight-related questions in this demo."
    else:
        state["final_answer"] = f"Best options found: {state['tool_result']}"
    return state

def should_act(state):
    if "need to search" in state["reasoning"].lower():
        return "act"
    return "final"

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("reason", reason_node)
    graph.add_node("act", act_node)
    graph.add_node("observe", observe_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("reason")
    graph.add_conditional_edges("reason", should_act, {"act": "act", "final": "final"})
    graph.add_edge("act", "observe")
    graph.add_edge("observe", "final")
    graph.add_edge("final", END)

    return graph.compile()

def main():
    question = input("Ask the agent: ")
    graph = build_graph()
    initial_state = {
        "question": question,
        "reasoning": "",
        "tool_result": "",
        "final_answer": "",
        "history": []
    }

    result = graph.invoke(initial_state)
    print("\nHistory:")
    for item in result["history"]:
        print("-", item)

    print("\nFinal answer:")
    print(result["final_answer"])

if __name__ == "__main__":
    main()