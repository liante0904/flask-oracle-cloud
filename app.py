from flask import Flask, render_template
from collections import defaultdict

app = Flask(__name__)

# 샘플 데이터
reports = [
    {"date": "2024-12-30", "title": "증권사 레포트 제목 1", "link": "https://example.com/report1"},
    {"date": "2024-12-30", "title": "증권사 레포트 제목 2", "link": "https://example.com/report2"},
    {"date": "2024-12-29", "title": "증권사 레포트 제목 3", "link": "https://example.com/report3"},
    {"date": "2024-12-28", "title": "증권사 레포트 제목 4", "link": "https://example.com/report4"},
]

# 날짜별 그룹핑
def group_reports_by_date(reports):
    grouped = defaultdict(list)
    for report in sorted(reports, key=lambda x: x["date"], reverse=True):
        grouped[report["date"].strip()].append(report)
    return grouped

@app.route('/')
def home():
    grouped_reports = group_reports_by_date(reports)
    return render_template('index.html', grouped_reports=grouped_reports)

if __name__ == '__main__':
    app.run(debug=True)
