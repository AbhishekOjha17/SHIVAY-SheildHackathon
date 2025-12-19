"""
Code Generation Agent (Optional Bonus)
Generates dynamic UI components and dashboard widgets
"""
from typing import Dict, Any, Optional, List
from loguru import logger


class CodeGenerationAgent:
    """Agent for generating code/UI components"""
    
    def __init__(self):
        """Initialize the agent"""
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Load code templates"""
        return {
            "dashboard_widget": """
export function {WidgetName}({ props }) {{
  return (
    <div className="widget">
      <h3>{Title}</h3>
      <div className="content">
        {{/* Dynamic content */}}
      </div>
    </div>
  );
}}
""",
            "chart_component": """
import {{ Chart }} from 'chart.js';

export function {ChartName}({ data }) {{
  return (
    <Chart
      type="{chartType}"
      data={data}
      options={options}
    />
  );
}}
""",
        }
    
    async def generate_dashboard_widget(
        self,
        widget_type: str,
        config: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate dashboard widget code"""
        logger.info(f"Generating dashboard widget: {widget_type}")
        
        # In a real implementation, this would use LLM to generate code
        # For now, return template-based code
        
        widget_name = config.get("name", "DynamicWidget")
        title = config.get("title", "Widget")
        
        code = self.templates.get("dashboard_widget", "").format(
            WidgetName=widget_name,
            Title=title,
        )
        
        return {
            "code": code,
            "type": "react_component",
            "widget_name": widget_name,
        }
    
    async def generate_chart_component(
        self,
        chart_type: str,
        data_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate chart component code"""
        logger.info(f"Generating chart component: {chart_type}")
        
        chart_name = data_config.get("name", "DynamicChart")
        
        code = self.templates.get("chart_component", "").format(
            ChartName=chart_name,
            chartType=chart_type,
        )
        
        return {
            "code": code,
            "type": "chart_component",
            "chart_name": chart_name,
        }

