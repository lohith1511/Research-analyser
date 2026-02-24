import { useState } from 'react';
import { UploadCloud, FileText } from 'lucide-react';
import axios from 'axios';

export default function Upload({ onUploadSuccess }) {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileChange = (e) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
            setError(null);
        }
    };

    const handleUpload = async () => {
        if (!file) return;
        setLoading(true);
        setError(null);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const res = await axios.post('http://localhost:9090/upload-paper', formData);
            onUploadSuccess(res.data);
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to upload file');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="glass-panel">
            <h2>Upload Research Paper</h2>
            <p style={{ color: "var(--text-secondary)", marginBottom: "1.5rem" }}>
                Upload a PDF paper to extract insights, generate summaries, and ask questions.
            </p>

            <div className="upload-container" onClick={() => document.getElementById('file-upload').click()}>
                <input
                    id="file-upload"
                    type="file"
                    accept="application/pdf"
                    className="hidden"
                    onChange={handleFileChange}
                />
                {file ? (
                    <>
                        <FileText size={48} className="upload-icon" />
                        <h3>{file.name}</h3>
                        <p style={{ color: "var(--text-secondary)" }}>{(file.size / 1024 / 1024).toFixed(2)} MB</p>
                    </>
                ) : (
                    <>
                        <UploadCloud size={48} className="upload-icon" />
                        <h3>Click to upload or drag & drop</h3>
                        <p style={{ color: "var(--text-secondary)" }}>PDF files only (max 10MB)</p>
                    </>
                )}
            </div>

            {error && <p style={{ color: "#ef4444", marginTop: "1rem" }}>{error}</p>}

            <div style={{ marginTop: "1.5rem", display: "flex", justifyContent: "flex-end" }}>
                <button
                    className="btn-primary"
                    onClick={handleUpload}
                    disabled={!file || loading}
                >
                    {loading ? 'Processing...' : 'Analyze Paper'}
                </button>
            </div>
        </div>
    );
}
