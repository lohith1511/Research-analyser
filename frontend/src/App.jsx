import { useState } from 'react';
import Navbar from './components/Navbar';
import Upload from './components/Upload';
import Summary from './components/Summary';
import Chatbot from './components/Chatbot';

function App() {
    const [fileData, setFileData] = useState(null);

    const handleUploadSuccess = (data) => {
        setFileData(data);
    };

    return (
        <div className="app-container">
            <Navbar />

            {!fileData ? (
                <div style={{ maxWidth: '800px', margin: '0 auto', width: '100%', marginTop: '4rem' }}>
                    <h1 style={{ textAlign: 'center', marginBottom: '1rem', fontSize: '2.5rem' }}>
                        Multi-Disciplinary Knowledge Discovery
                    </h1>
                    <p style={{ textAlign: 'center', color: 'var(--text-secondary)', marginBottom: '3rem', fontSize: '1.2rem' }}>
                        Transform complex research papers into actionable knowledge instantly using advanced AI embeddings and NLP.
                    </p>
                    <Upload onUploadSuccess={handleUploadSuccess} />
                </div>
            ) : (
                <div className="main-grid">
                    <Summary fileData={fileData} />
                    <Chatbot />
                </div>
            )}
        </div>
    );
}

export default App;
