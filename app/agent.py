# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import json
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


# Multi-Agent DevOps Intelligence Functions
def get_infrastructure_report() -> str:
    """Get comprehensive infrastructure health and performance report."""
    health_data = {
        "compute": {"status": "healthy", "cpu_usage": "45%", "memory": "62%"},
        "storage": {"status": "healthy", "usage": "78%", "iops": "normal"},
        "network": {"status": "healthy", "latency": "12ms", "throughput": "850Mbps"},
        "database": {"status": "warning", "connections": "85%", "query_time": "250ms"}
    }
    
    metrics = {
        "timeframe": "1h",
        "trends": {"cpu_trend": "stable", "memory_trend": "increasing", "disk_io": "normal", "network_traffic": "peak_hours"},
        "alerts": [
            {"level": "warning", "message": "Memory usage trending upward"},
            {"level": "info", "message": "Network traffic at 80% of baseline"}
        ]
    }
    
    report = {
        "timestamp": "2024-09-16T10:30:00Z",
        "health_status": health_data,
        "performance_metrics": metrics
    }
    return json.dumps(report, indent=2)


def get_security_report() -> str:
    """Get comprehensive security and compliance report."""
    vulnerabilities = {
        "scan_type": "full",
        "critical": 2, "high": 5, "medium": 12, "low": 8,
        "findings": [
            {"severity": "critical", "type": "SQL Injection", "component": "web-api"},
            {"severity": "high", "type": "Outdated Dependencies", "component": "frontend"}
        ]
    }
    
    compliance = {
        "framework": "SOC2", "overall_score": "87%",
        "controls": {"access_control": "compliant", "data_encryption": "compliant", "audit_logging": "non_compliant", "backup_recovery": "compliant"},
        "recommendations": ["Enable comprehensive audit logging", "Review access permissions quarterly"]
    }
    
    report = {
        "timestamp": "2024-09-16T10:30:00Z",
        "vulnerability_scan": vulnerabilities,
        "compliance_status": compliance
    }
    return json.dumps(report, indent=2)


def get_deployment_status() -> str:
    """Get current deployment and pipeline status."""
    pipeline_status = {
        "pipeline": "main", "status": "running", "stage": "testing", "progress": "75%",
        "stages": {"build": "completed", "test": "running", "security_scan": "pending", "deploy": "pending"},
        "estimated_completion": "5 minutes"
    }
    
    report = {
        "timestamp": "2024-09-16T10:30:00Z",
        "pipeline_status": pipeline_status
    }
    return json.dumps(report, indent=2)


def emergency_rollback(environment: str = "production") -> str:
    """Execute emergency rollback in specified environment."""
    rollback_result = {
        "action": "emergency_rollback", "environment": environment, "status": "initiated",
        "rollback_id": "rb-2024-001", "estimated_duration": "3 minutes"
    }
    return json.dumps(rollback_result, indent=2)


root_agent = Agent(
    name="devops_intelligence_hub",
    model="gemini-2.5-flash",
    instruction="""You are the DevOps Intelligence Hub Orchestrator, coordinating multiple specialist capabilities:

1. Infrastructure Monitoring: Cloud resources, performance, and health
2. Security Analysis: Vulnerabilities, compliance, and threat detection  
3. Deployment Management: CI/CD pipelines and release automation

Provide comprehensive DevOps intelligence by combining insights from all domains.""",
    tools=[
        get_weather, 
        get_current_time,
        get_infrastructure_report,
        get_security_report, 
        get_deployment_status,
        emergency_rollback
    ],
)
