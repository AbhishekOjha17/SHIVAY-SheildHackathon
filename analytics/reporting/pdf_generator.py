"""
PDF Report Generator using ReportLab
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from typing import Dict, Any, List
from loguru import logger
from io import BytesIO


class PDFReportGenerator:
    """Generate PDF reports"""
    
    def generate_report(
        self,
        data: Dict[str, Any],
        output_path: str,
    ) -> bool:
        """Generate PDF report"""
        try:
            doc = SimpleDocTemplate(output_path, pagesize=A4)
            story = []
            styles = getSampleStyleSheet()
            
            # Title
            title = Paragraph("Shivay Emergency Response Report", styles["Title"])
            story.append(title)
            story.append(Spacer(1, 0.2 * inch))
            
            # Summary
            summary = Paragraph(f"Report Generated: {data.get('generated_at', 'N/A')}", styles["Normal"])
            story.append(summary)
            story.append(Spacer(1, 0.2 * inch))
            
            # Data table
            if "data" in data:
                table_data = [["Metric", "Value"]]
                for key, value in data["data"].items():
                    table_data.append([str(key), str(value)])
                
                table = Table(table_data)
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 14),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]))
                
                story.append(table)
            
            doc.build(story)
            logger.info(f"PDF report generated: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error generating PDF report: {e}")
            return False

