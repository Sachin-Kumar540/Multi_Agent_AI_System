# Multi-Agent AI Travel Booking System

An end-to-end AI travel planning application built with LangGraph and Streamlit. This system takes a plain-English trip request (e.g., "Plan a 7-day Japan trip under ₹2L") and produces a fully formatted itinerary by passing the query through a linear, four-agent pipeline. 

It features real-time UI updates, cross-session persistent memory via PostgreSQL, and dynamically generated markdown itineraries powered by Groq's LLaMA 3 model.

## 🚀 Key Features

*   **Linear Multi-Agent Pipeline:** A structured LangGraph `StateGraph` that sequentially passes data through four specialized agents (Flight, Hotel, Itinerary, Final).
*   **Persistent User Memory:** Utilizes LangGraph's Postgres checkpointer to save conversation state via `thread_id`, allowing users to resume planning sessions without losing context.
*   **Interactive Streamlit UI:** A dark-themed frontend featuring quick-destination chips, live streaming of agent statuses during generation, LLM call metrics, and one-click markdown exports of the final itinerary.
*   **Graceful Degradation:** Tools like the Tavily search integration are built defensively; if the API is missing or fails, the app falls back to placeholder data instead of crashing.

## 🧠 System Architecture

The core of the application is a LangGraph state machine. Agents do not route dynamically; they execute in a fixed sequence, reading and writing to a shared `TravelState` TypedDict.

**Pipeline Flow:**
`START → Flight Agent → Hotel Agent → Itinerary Agent → Final Agent → END`

**Shared State (`TravelState`):**
*   `messages`: Running conversation log (appends via `operator.add`).
*   `user_query`, `flight_results`, `hotel_results`, `itinerary`: Individual agent outputs.
*   `llm_calls`: Counter for tracking processing metrics.

### The Agents
1.  **✈️ Flight Agent:** Calls `search_flights()` to retrieve live flight data via the AviationStack API.
2.  **🏨 Hotel Agent:** Calls `tavily_search()` using the Tavily web-search API for real-time hotel discovery.
3.  **🗺️ Itinerary Agent:** The primary LLM step. Feeds flight and hotel data into Groq's `llama-3.3-70b-versatile` model to draft a comprehensive, day-by-day itinerary.
4.  **💬 Final Agent:** Synthesizes all gathered data and the drafted itinerary into a polished, user-facing final response.

## 🛠️ Tech Stack

*   **Orchestration:** LangGraph, LangChain
*   **LLM Inference:** Groq (LLaMA 3.3 70B)
*   **Frontend:** Streamlit
*   **Database:** PostgreSQL (for LangGraph Checkpointing)
*   **External APIs:** AviationStack, Tavily

## 💻 Local Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/Sachin-Kumar540/Multi_Agent_AI_System.git](https://github.com/Sachin-Kumar540/Multi_Agent_AI_System.git)
cd Multi_Agent_AI_System
