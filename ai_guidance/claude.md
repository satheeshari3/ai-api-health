## Guidelines\
\
1. Always identify:\
   - API endpoint\
   - Error type (e.g., 500, timeout, slow response)\
   - Timestamp of the failure\
\
2. Provide human-readable explanation:\
   - Describe the likely cause of the failure\
   - Suggest practical steps for resolution\
   - Avoid technical jargon if possible\
\
3. Maintain clarity:\
   - Keep explanations concise (max 3\'965 sentences)\
   - Use bullet points for clarity if multiple issues exist\
\
4. Safety:\
   - Never generate misleading information\
   - Recommend safe debugging practices\
\
## Example Prompt\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Analyze the following API response logs and provide a clear explanation of why the API failed and how to fix it.\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 \
\
**Output Example:**\
- The API returned `500 Internal Server Error`, likely due to missing authentication headers.  \
- Recommendation: Verify authentication token and retry request.  \
- Response time exceeded 2 seconds; consider optimizing endpoint logic.\
\
\pard\pardeftab720\partightenfactor0

\f1\fs24 \cf3 \strokec3 \
