import { useState } from 'react';
import axios from 'axios';
import { FileSearch } from 'lucide-react';
import Loader from './Loader';

export default function Summary({ fileData }) {
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const generateSummary = async () => {
        setLoading(true);
        setError(null);
        try {
            const res = await axios.post('http://localhost:8000/summarize');
            setSummary(res.data.summary);
        } catch (err) {
            setError('Failed to generate summary');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="glass-panel">
            <h2>Document Analysis</h2>

            {!summary && !loading && (
                <div style={{ textAlign: "center", padding: "2rem" }}>
                    <FileSearch size={48} style={{ color: "var(--text-secondary)", marginBottom: "1rem" }} />
                    <h3>Ready for extraction</h3>
                    <p style={{ color: "var(--text-secondary)", marginBottom: "1rem" }}>
                        The AI model has processed the text and embeddings.
                    </p>
                    <button className="btn-primary" onClick={generateSummary}>Generate AI Summary</button>
                </div>
            )}

            {loading && <Loader text="Abstracting core concepts and generating summary..." />}

            {error && <p style={{ color: "#ef4444" }}>{error}</p>}

            {summary && (
                <div style={{ marginTop: "1rem" }}>
                    <h3>AI Summary</h3>
                    <div style={{ padding: "1.5rem", background: "var(--bg-dark)", borderRadius: "8px", marginTop: "1rem" }}>
                        <p className="summary-text">{summary}</p>
                    </div>
                </div>
            )}

            {fileData?.keywords && fileData.keywords.length > 0 && (
                <div className="keywords-wrapper">
                    <h3>Extracted Concepts & Keywords</h3>
                    <div className="keywords-container">
                        {fileData.keywords.map((kw, i) => (
                            <span key={i} className="keyword-chip">{kw}</span>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
