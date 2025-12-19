"""
CSV Report Generator
"""
import csv
from typing import Dict, Any, List
from loguru import logger


class CSVReportGenerator:
    """Generate CSV reports"""
    
    def generate_report(
        self,
        data: List[Dict[str, Any]],
        output_path: str,
    ) -> bool:
        """Generate CSV report"""
        try:
            if not data:
                return False
            
            # Get all keys from first item
            fieldnames = list(data[0].keys())
            
            with open(output_path, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            logger.info(f"CSV report generated: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error generating CSV report: {e}")
            return False

