import { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send, Bot, User } from 'lucide-react';

export default function Chatbot() {
    const [messages, setMessages] = useState([
        { role: 'ai', content: "Hello! I've analyzed the research paper. What would you like to know?" }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const chatEndRef = useRef(null);

    const scrollToBottom = () => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMsg = input.trim();
        setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
        setInput('');
        setLoading(true);

        try {
            const res = await axios.post('http://localhost:8000/ask-question', { question: userMsg });
            setMessages(prev => [...prev, { role: 'ai', content: res.data.answer }]);
        } catch (err) {
            setMessages(prev => [...prev, { role: 'ai', content: "Sorry, I couldn't process your question." }]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="glass-panel chat-container">
            <h2>Research Q&A</h2>

            <div className="chat-history">
                {messages.map((msg, i) => (
                    <div key={i} className={`chat-message ${msg.role}`}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem', color: 'var(--text-secondary)', fontSize: '0.8rem' }}>
                            {msg.role === 'ai' ? <Bot size={14} /> : <User size={14} />}
                            {msg.role === 'ai' ? 'AI Assistant' : 'You'}
                        </div>
                        {msg.content}
                    </div>
                ))}
                {loading && (
                    <div className="chat-message ai">
                        <div className="spinner" style={{ width: '20px', height: '20px', borderWidth: '2px' }}></div>
                    </div>
                )}
                <div ref={chatEndRef} />
            </div>

            <div className="chat-input-wrapper">
                <input
                    type="text"
                    className="chat-input"
                    placeholder="Ask a question about the paper..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                />
                <button
                    className="chat-btn"
                    onClick={handleSend}
                    disabled={!input.trim() || loading}
                >
                    <Send size={18} />
                </button>
            </div>
        </div>
    );
}
