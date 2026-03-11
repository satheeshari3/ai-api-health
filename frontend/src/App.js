import { useEffect, useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [name, setName] = useState("");
  const [endpoints, setEndpoints] = useState([]);
  const [results, setResults] = useState({});

  const API = "http://127.0.0.1:5001";

  const loadEndpoints = async () => {
    const res = await fetch(`${API}/api/endpoints`);
    const data = await res.json();
    setEndpoints(data);
  };

  useEffect(() => {
    loadEndpoints();
  }, []);

  const addEndpoint = async () => {
    await fetch(`${API}/api/endpoints`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, url })
    });

    setName("");
    setUrl("");
    loadEndpoints();
  };

  const checkHealth = async (id) => {
    const res = await fetch(`${API}/api/check/${id}`);
    const data = await res.json();

    setResults({
      ...results,
      [id]: data
    });
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI API Health Monitor</h1>

      <div style={styles.form}>
        <input
          placeholder="API Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={styles.input}
        />

        <input
          placeholder="API URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={styles.input}
        />

        <button onClick={addEndpoint} style={styles.addBtn}>
          Add Endpoint
        </button>
      </div>

      <div>
        {endpoints.map((ep) => (
          <div key={ep.id} style={styles.card}>
            <div style={{ width: "70%" }}>
              <strong>{ep.name}</strong>
              <p>{ep.url}</p>

              {results[ep.id] && (
                <div style={styles.resultBox}>
                  <p><b>Status:</b> {results[ep.id].status}</p>
                  <p><b>Response Time:</b> {results[ep.id].response_time}s</p>
                  <p><b>AI Insight:</b> {results[ep.id].ai_explanation}</p>
                </div>
              )}
            </div>

            <button
              style={styles.checkBtn}
              onClick={() => checkHealth(ep.id)}
            >
              Check Health
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "750px",
    margin: "40px auto",
    fontFamily: "Arial",
  },
  title: {
    textAlign: "center",
    marginBottom: "30px"
  },
  form: {
    display: "flex",
    gap: "10px",
    marginBottom: "30px",
  },
  input: {
    padding: "10px",
    flex: 1,
    border: "1px solid #ccc",
    borderRadius: "5px"
  },
  addBtn: {
    padding: "10px 20px",
    background: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px"
  },
  card: {
    border: "1px solid #ddd",
    padding: "15px",
    marginBottom: "15px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    borderRadius: "8px",
    background: "#fafafa"
  },
  checkBtn: {
    padding: "8px 16px",
    background: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "5px"
  },
  resultBox: {
    marginTop: "10px",
    background: "#f0f0f0",
    padding: "10px",
    borderRadius: "6px",
    fontSize: "14px"
  }
};

export default App;