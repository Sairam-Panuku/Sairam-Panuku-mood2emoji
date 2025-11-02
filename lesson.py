from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Create PDF
pdf_path = "lesson_plan.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
style_heading = ParagraphStyle('Heading', parent=styles['Heading1'], spaceAfter=12, textColor=colors.darkblue)
style_subheading = ParagraphStyle('SubHeading', parent=styles['Heading2'], spaceAfter=10, textColor=colors.darkred)
style_body = styles['Normal']

content = []

# Title
content.append(Paragraph("Lesson Plan — Mood2Emoji App (Ages 12–16)", style_heading))
content.append(Spacer(1, 12))

# Introduction
intro_text = """
<b>Topic:</b> Introduction to Text Classification using Mood2Emoji<br/>
<b>Duration:</b> 60 minutes<br/>
<b>Objective:</b><br/>
Students will learn how AI can detect mood from text and build a simple Streamlit web app that returns an emoji for their sentence.
"""
content.append(Paragraph(intro_text, style_body))
content.append(Spacer(1, 12))

# Topics Introduced
content.append(Paragraph("<b>Topics Introduced:</b>", style_subheading))
topics = """
- What is sentiment analysis?<br/>
- How text polarity works (positive, neutral, negative).<br/>
- Role of data cleaning and safety filters.<br/>
- Ethical use of AI for kids.
"""
content.append(Paragraph(topics, style_body))
content.append(Spacer(1, 12))

# Detailed Lesson Flow Table
content.append(Paragraph("<b>Detailed Lesson Flow:</b>", style_subheading))
table_data = [
    ["Time", "Step", "Activity"],
    ["0–10 min", "Introduction", "Teacher explains sentiment analysis using emojis and real-life examples (‘I love pizza!’, ‘I’m tired today.’)."],
    ["10–20 min", "Demo", "Show the Mood2Emoji app and how it works."],
    ["20–40 min", "Hands-On Activity", "Students open Streamlit, type their own sentences, and observe mood changes."],
    ["40–50 min", "Teacher Mode", "Explain the polarity scale (-1 to +1). Show logic diagram."],
    ["50–60 min", "Wrap-Up", "Discussion: Can AI really ‘feel’? Where do we use this in real life (chatbots, social media)?"]
]
table = Table(table_data, colWidths=[70, 100, 330])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP')
]))
content.append(table)
content.append(Spacer(1, 12))

# Learning Outcomes
content.append(Paragraph("<b>Learning Outcomes:</b>", style_subheading))
outcomes = """
- Understand how AI reads emotions through text.<br/>
- Learn basic programming logic and flow.<br/>
- Recognize ethical AI use (avoiding harmful content).<br/>
- Gain curiosity about Natural Language Processing (NLP).
"""
content.append(Paragraph(outcomes, style_body))
content.append(Spacer(1, 20))

# Conclusion
content.append(Paragraph("This 60-minute session encourages creativity, digital literacy, and responsible AI exploration in a fun and safe learning environment.", style_body))

# Build PDF
doc.build(content)
pdf_path
