def analyze_logs(path):
    try:
        with open(path, "r") as f:
            logs = f.read()

        if "error" in logs.lower():
            return "🚨 Error detected in logs:\n" + logs[-500:]
        elif "warn" in logs.lower():
            return "⚠️ Warning found."
        else:
            return "✅ No major issues found."

    except Exception as e:
        return f"Failed to read logs: {str(e)}"
