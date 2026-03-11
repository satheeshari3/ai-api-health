 # AI Agents in AI API Health Monitor\
\
This project uses specialized AI agents to monitor API health, analyze failures, and provide actionable insights.\
\
## Agents\
\
### 1. HealthMonitorAgent\
- **Role:** Continuously checks API endpoints for uptime, latency, and errors.\
- **Responsibilities:**\
  - Trigger API health checks on schedule\
  - Collect response data and status codes\
  - Pass logs to LoggerAgent and AI Analyzer\
- **Impact:** Automates monitoring, eliminating manual checks.\
\
### 2. LoggerAgent\
- **Role:** Stores and organizes API responses and error logs.\
- **Responsibilities:**\
  - Maintain a structured database of API responses\
  - Ensure logs are queryable for historical analysis\
  - Support AI analysis with complete context\
- **Impact:** Ensures reliable data for AI-driven insights.\
\
### 3. AI Analyzer\
- **Role:** Generates human-readable explanations for API failures.\
- **Responsibilities:**\
  - Analyze error codes, timeouts, and response anomalies\
  - Suggest potential fixes and improvements\
  - Maintain consistency using prompt rules\
- **Impact:** Converts technical errors into actionable insights.}