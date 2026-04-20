# Finance Copilot MCP

A personalized finance copilot that helps users answer questions about spending, surplus, affordability, savings goals, and investment allocation.

## Features

- Ingest and categorize financial transactions
- Analyze spending patterns and monthly surplus
- Check affordability of purchases
- Track progress towards savings goals
- Suggest spending cuts
- Recommend investment allocation
- Forecast spending trends
- MCP server for tool-based interactions
- Streamlit demo UI

## Tech Stack

- Python
- Pandas for data processing
- Scikit-learn for ML (categorization)
- Prophet for forecasting
- Streamlit for UI
- MCP SDK for server

## Installation

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app/main.py`

## Usage

Upload a CSV of transactions, view dashboard, ask questions to the assistant.

## Architecture

- `src/`: Core logic (parser, analysis, planner, etc.)
- `mcp_server/`: MCP server exposing tools
- `app/`: UI and agent logic
- `data/`: Sample data and configs

## Evaluation

Tool accuracy tested on sample queries.

## Future Work

- PDF parsing
- Multi-bank support
- Stock market integration