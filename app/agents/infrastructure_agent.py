from adk import BaseAgent
from adk.tools import Tool
import json

class InfrastructureAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Infrastructure Monitor",
            description="Monitors cloud infrastructure health and performance"
        )
        self.add_tool(self.check_resource_health)
        self.add_tool(self.analyze_performance_metrics)
    
    @Tool(description="Check health status of cloud resources")
    def check_resource_health(self, resource_type: str = "all") -> str:
        health_data = {
            "compute": {"status": "healthy", "cpu_usage": "45%", "memory": "62%"},
            "storage": {"status": "healthy", "usage": "78%", "iops": "normal"},
            "network": {"status": "healthy", "latency": "12ms", "throughput": "850Mbps"},
            "database": {"status": "warning", "connections": "85%", "query_time": "250ms"}
        }
        if resource_type == "all":
            return json.dumps(health_data, indent=2)
        return json.dumps(health_data.get(resource_type, {"error": "Resource not found"}), indent=2)
    
    @Tool(description="Analyze performance metrics and trends")
    def analyze_performance_metrics(self, timeframe: str = "1h") -> str:
        metrics = {
            "timeframe": timeframe,
            "trends": {"cpu_trend": "stable", "memory_trend": "increasing", "disk_io": "normal", "network_traffic": "peak_hours"},
            "alerts": [
                {"level": "warning", "message": "Memory usage trending upward"},
                {"level": "info", "message": "Network traffic at 80% of baseline"}
            ]
        }
        return json.dumps(metrics, indent=2)
