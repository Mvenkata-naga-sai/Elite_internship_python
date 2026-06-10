from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json

doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

content = []

content.append(Paragraph("Weather Data Report", styles['Title']))
content.append(Spacer(1, 20))

with open("weather_data.json") as f:
    data = json.load(f)

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]

content.append(Paragraph(f"Temperature: {temp} °C", styles['Normal']))
content.append(Paragraph(f"Humidity: {humidity} %", styles['Normal']))

doc.build(content)

print("Report generated successfully")
