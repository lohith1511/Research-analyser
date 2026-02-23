import { BrainCircuit } from 'lucide-react';

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="logo-container">
                <BrainCircuit size={32} color="#a855f7" />
                <span className="logo-text">NeuralSearch AI</span>
            </div>
        </nav>
    );
}
