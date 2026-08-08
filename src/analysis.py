from datetime import datetime
import psutil


def run_analysis():

    # Get current system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    # Demo error count
    # Later we can connect this to real application/system logs
    errors = 0

    # Calculate risk score
    risk_score = 0

    if cpu >= 90:
        risk_score += 40
    elif cpu >= 75:
        risk_score += 25
    elif cpu >= 60:
        risk_score += 15

    if memory >= 90:
        risk_score += 40
    elif memory >= 75:
        risk_score += 25
    elif memory >= 60:
        risk_score += 15

    if errors >= 10:
        risk_score += 20
    elif errors >= 5:
        risk_score += 10

    # Limit score to 100
    risk_score = min(risk_score, 100)

    # Determine risk level
    if risk_score >= 80:
        risk_level = "CRITICAL"
        prediction = "System failure likely soon"

    elif risk_score >= 50:
        risk_level = "HIGH"
        prediction = "System performance may degrade"

    elif risk_score >= 25:
        risk_level = "MEDIUM"
        prediction = "System showing moderate stress"

    else:
        risk_level = "LOW"
        prediction = "System operating normally"

    # Root causes
    root_causes = []

    if cpu >= 75:
        root_causes.append("High CPU utilization")

    if memory >= 75:
        root_causes.append("High memory consumption")

    if errors >= 5:
        root_causes.append("Frequent system errors")

    if not root_causes:
        root_causes.append("No major issues detected")

    # Error types
    error_types = []

    if cpu >= 75:
        error_types.append("CPU overload risk")

    if memory >= 75:
        error_types.append("Memory pressure risk")

    if errors >= 5:
        error_types.append("Application or service errors")

    if not error_types:
        error_types.append("No significant errors detected")

    # Recommended action
    if risk_level == "CRITICAL":
        action = "Investigate immediately and restart affected services"

    elif risk_level == "HIGH":
        action = "Monitor system closely and investigate resource usage"

    elif risk_level == "MEDIUM":
        action = "Monitor CPU and memory usage"

    else:
        action = "No immediate action required"

    # Summary
    summary = f"""
--- SYSTEM ANALYSIS ---
Time: {datetime.now().strftime("%H:%M:%S")}
CPU Usage: {cpu}%
Memory Usage: {memory}%
Error Count: {errors}
Risk Score: {risk_score}/100
Risk Level: {risk_level}
Prediction: {prediction}
"""

    return {
        "summary": summary,
        "cpu": cpu,
        "memory": memory,
        "errors": errors,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "root_causes": root_causes,
        "error_types": error_types,
        "prediction": prediction,
        "action": action
    }