export default function Loader({ text }) {
    return (
        <div className="loader-container">
            <div className="spinner"></div>
            <p style={{ color: "var(--text-secondary)" }}>{text || "Loading..."}</p>
        </div>
    );
}
