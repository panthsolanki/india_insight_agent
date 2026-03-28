Since you are a **Frontend Engineer**, you probably appreciate a README that is not only functional but also visually structured and "scannable." 

Here is a professionally formatted `README.md` for the **India Insight Agent**. I've added a **"Quick Start"** section and a **"Deployment"** guide specifically tailored to the `uv` and **Cloud Run** workflow we built.

---

# 🇮🇳 India Insight Agent

An AI-powered analytical engine that connects directly to the **Ministry of Statistics and Programme Implementation (MoSPI)** via the **Model Model Context Protocol (MCP)**. This agent fetches live development data and provides deep, data-driven insights into India's growth sectors.

---

## 🚀 Key Features
* **Live Data Retrieval:** Connects to the official [mcp.mospi.gov.in](https://mcp.mospi.gov.in) endpoint via SSE.
* **Sequential Reasoning:** Uses a two-stage "Researcher → Analyst" flow to ensure accuracy before interpretation.
* **Cloud Native:** Fully containerized with a multi-stage Docker build, optimized for **Google Cloud Run**.
* **Built with ADK:** Leverages Google's **Agent Development Kit** for seamless LLM orchestration.

---

## 📁 Project Structure

```text
india-insight-agent/
├── src/
│   ├── main.py             # App entry point (ADK Web/API)
│   ├── agent/
│   │   ├── insight_agent.py # Core logic: SequentialAgent definition
│   │   └── prompts.py      # Specialized System Prompts for MoSPI
│   └── tools/
│       └── mospi_client.py  # MCP SSE Client connection logic
├── Dockerfile              # Optimized multi-stage build using 'uv'
├── pyproject.toml          # Dependency and project configuration
└── .env                    # Local environment variables
```

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Package Manager** | [uv](https://astral.sh/uv) |
| **Agent Framework** | Google ADK |
| **Protocol** | MCP (Model Context Protocol) |
| **Infrastructure** | Google Cloud Run |

---

## ⚙️ Local Setup

### 1. Install `uv`
If you don't have it yet, install the faster Python package manager:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Initialize and Install
```bash
# Sync dependencies from pyproject.toml
uv sync
```

### 3. Configure Environment
Create a `.env` file in the root directory:
```text
GOOGLE_API_KEY=your_gemini_api_key
PORT=8080
```

### 4. Run the Agent
```bash
uv run src/main.py
```
Access the interface at `http://localhost:8080`.

---

## ☁️ Deployment to Cloud Run

Deploy directly from your source code. Cloud Run will use the `Dockerfile` to build the image automatically.

```bash
gcloud run deploy india-insight-agent \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_gemini_key_here \
  --max-instances 3
```

---

## 🤖 Agent Logic
The `IndiaInsightAgent` follows a strict **Fetch-then-Analyze** pattern:

1.  **DataResearcher:** Uses MoSPI tools to find indicators (GDP, CPI, Energy, etc.) and fetches the latest 5-10 years of raw data.
2.  **TrendAnalyst:** Receives the raw JSON, calculates growth rates (CAGR), and interprets the data within the context of India's development goals.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

