

AI API Health Monitor

Developer-focused monitoring tool that checks API health and explains failures using AI.

This project provides a simple dashboard where developers can add API endpoints, run health checks, measure response time, and receive AI-generated insights explaining why an API might be failing.

Problem

Developers often see errors like:

500 Internal Server Error

404 Not Found

Timeouts

Slow API responses

But identifying why an API failed still requires manual debugging.

This tool solves that by combining API monitoring + AI insights to quickly explain potential issues.

Solution

AI API Health Monitor provides a lightweight dashboard that:

• Tracks API endpoint health
• Measures response latency
• Detects client/server errors
• Generates developer-friendly explanations using AI

## Dashboard Preview

![AI API Health Monitor](assets/screenshot.png)

Key Features

• Add and manage API endpoints
• Run real-time health checks
• Measure API response time
• Detect client errors (4xx)
• Detect server errors (5xx)
• AI-generated explanations for failures
• Clean React dashboard UI

Tech Stack

Frontend

React

Fetch API

Simple dashboard UI

Backend

Python

Flask REST API

Requests library

AI Integration

Groq LLM API

Database

SQLite

System Architecture
React Frontend
      │
      │ HTTP Requests
      ▼
Flask Backend API
      │
      ├── Endpoint Management
      ├── Health Check Service
      ├── Response Time Measurement
      │
      ▼
AI Service (Groq)
      │
      ▼
Failure Explanation
Project Structure
ai-api-health

backend/
 ├── app.py
 ├── routes/
 ├── services/
 ├── models/

frontend/
 ├── src/
 ├── public/

README.md
.gitignore
Running the Project
1. Clone the repository
git clone https://github.com/satheeshari3/ai-api-health.git
cd ai-api-health
2. Start Backend
cd backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py

Backend runs at

http://127.0.0.1:5001
3. Start Frontend
cd frontend

npm install
npm start

Frontend runs at

http://localhost:3000
Demo APIs to Test

Working API

https://api.github.com

Client Error

https://httpstat.us/404

Server Error

https://httpstat.us/500

Broken API

https://this-api-does-not-exist.com
How It Works

User adds an API endpoint

Backend performs an HTTP request to the endpoint

Response status and latency are captured

If a failure occurs, the AI service generates a potential explanation

Results are displayed in the monitoring dashboard

Future Improvements

• Automated periodic health checks
• API uptime monitoring
• Historical response time tracking
• Failure alerts and notifications
• Visual analytics dashboard

Author

Satheeswaran Harikrishnan