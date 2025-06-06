# 🚀 Project Overview

This project consists of four main components:

- **FastAPI Backend**  
  A simple backend API managing product data (serial number, manufacturing date).  
  Supports CRUD operations (Create, Read, Update, Delete) on products.

- **MCP Server**  
  A dedicated protocol server that exposes FastAPI endpoints as tools for LLMs.  
  It abstracts backend APIs into a tool-calling interface compatible with LLMs' function calling or OpenAPI-based tooling.

- **LLM Agent**  
  An intelligent agent powered by large language models (e.g., OpenAI GPT-4, LLaMA3 via Ollama, or Gemini).  
  The agent interprets user queries and decides which MCP tools to invoke to fulfill requests.

- **Web-based Chat UI**  
  A front-end interface (e.g., OpenWebUI) allowing users to chat with the agent in natural language.  
  Integrates seamlessly with the agent and MCP to deliver real-time responses backed by live data.

---

# 🏗️ Architecture Diagram

User <---> Web Chat UI (OpenWebUI) <---> LLM Agent <--calls--> MCP Server <--calls--> FastAPI Backend <---> Database


- The LLM Agent receives user queries from the chat UI.  
- It calls MCP Server tool endpoints (e.g., `add_product`, `list_products`).  
- The MCP Server translates calls to backend REST API calls.  
- The FastAPI backend processes requests against the database and returns results.  
- Responses flow back through the chain to the user.

---

# 🛠️ Technologies Used

| Component     | Technology / Library                 | Purpose                                           |
|---------------|-----------------------------------|--------------------------------------------------|
| Backend API   | FastAPI, Pydantic, SQLAlchemy/SQLite | Manage product data and business logic           |
| MCP Server    | FastAPI, JSON Schema, OpenAI Tool Spec | Tool interface exposing backend to LLM           |
| LLM Agent     | OpenAI GPT-4/GPT-3.5, Ollama, Gemini API | Natural language understanding + tool calls      |
| Chat UI       | OpenWebUI (Dockerized)             | Web-based chat interface for users                |
| Environment   | Docker, Docker Compose             | Containerization and deployment                    |
| Secrets Management | `.env` files, environment variables | Secure API keys and configuration                 |

---

# 🔧 Features Demonstrated

- Agentic LLM tool-calling: LLM can call backend functions as tools with structured JSON inputs and outputs.  
- Modular backend separation: MCP server acts as a protocol gateway, separating concerns and allowing flexible orchestration.  
- Multiple LLM providers: Support for OpenAI API, Ollama local LLaMA models, and Gemini API.  
- Containerized deployment: All components run in Docker containers with easy orchestration via `docker-compose`.  
- Web UI integration: Users interact with the system naturally via chat, powered by OpenWebUI or alternatives.

---

# 📦 Getting Started

## Prerequisites

- Docker & Docker Compose installed  
- `.env` file with API keys (e.g. OpenAI)

## Running the System

```bash
docker-compose up -d
```

This starts:

- FastAPI backend on port 8000
- MCP server on port 8500
- OpenWebUI chat UI on port 3000

🛠️ Development Notes

FastAPI backend exposes /products API with CRUD operations.
MCP server exposes tool endpoints wrapping backend APIs, with JSON schema for tool calling.
LLM agent calls MCP tools via OpenAI function calling or compatible protocols.
OpenWebUI connects to LLM provider and serves as the front-end chat interface.
API keys are injected via environment variables for security.