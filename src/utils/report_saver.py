
from pathlib import Path
from datetime import datetime

from src.schemas.research_report import ResearchReport


def save_report_json(report: ResearchReport) -> str:

    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"research_report_{timestamp}.json"

    file_path = reports_dir / filename

    json_data = report.model_dump_json(indent=4)

    file_path.write_text(json_data, encoding="utf-8")

    return str(file_path)
