from adk import BaseAgent
from adk.tools import Tool
import json

class SecurityAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Security Monitor",
            description="Monitors security threats, vulnerabilities, and compliance"
        )
        self.add_tool(self.scan_vulnerabilities)
        self.add_tool(self.check_compliance)
    
    @Tool(description="Scan for security vulnerabilities")
    def scan_vulnerabilities(self, scan_type: str = "full") -> str:
        vulnerabilities = {
            "scan_type": scan_type,
            "critical": 2,
            "high": 5,
            "medium": 12,
            "low": 8,
            "findings": [
                {"severity": "critical", "type": "SQL Injection", "component": "web-api"},
                {"severity": "high", "type": "Outdated Dependencies", "component": "frontend"}
            ]
        }
        return json.dumps(vulnerabilities, indent=2)
    
    @Tool(description="Check compliance status")
    def check_compliance(self, framework: str = "SOC2") -> str:
        compliance = {
            "framework": framework,
            "overall_score": "87%",
            "controls": {
                "access_control": "compliant",
                "data_encryption": "compliant", 
                "audit_logging": "non_compliant",
                "backup_recovery": "compliant"
            },
            "recommendations": [
                "Enable comprehensive audit logging",
                "Review access permissions quarterly"
            ]
        }
        return json.dumps(compliance, indent=2)
