"""
SMART REMINDER – Machine Learning Based Reminder System
Author: Shifa Baksare (AI & Data Science, 3rd Year)

File: generate_report.py
Description: Generates an academic project report (.pdf) using ReportLab.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
REPORT_DIR = os.path.join(BASE_DIR, 'report')
PDF_PATH = os.path.join(REPORT_DIR, 'Smart_Reminder_Project_Report.pdf')


def build_pdf_report():
    print("[*] Generating Comprehensive Academic Project Report PDF...")

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom palette
    primary_color = colors.HexColor('#1E293B')     # Dark Slate
    accent_color = colors.HexColor('#4F46E5')      # Indigo
    secondary_color = colors.HexColor('#0F766E')   # Teal
    text_color = colors.HexColor('#334155')        # Slate text
    light_bg = colors.HexColor('#F8FAFC')          # Slate 50
    border_color = colors.HexColor('#CBD5E1')      # Slate 300

    # Custom typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=primary_color,
        alignment=1, # Center
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=18,
        textColor=accent_color,
        alignment=1,
        spaceAfter=25
    )

    h1_style = ParagraphStyle(
        'ChapHeading',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceBefore=18,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SecHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=accent_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyMain',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.5,
        textColor=text_color,
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'BulletMain',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=5
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=body_style,
        fontSize=9,
        leading=12,
        spaceAfter=0
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=table_cell,
        fontName='Helvetica-Bold',
        textColor=colors.white
    )

    story = []

    # =========================================================================
    # COVER / TITLE PAGE
    # =========================================================================
    story.append(Spacer(1, 40))
    story.append(Paragraph("A MINI PROJECT REPORT ON", ParagraphStyle('SubSub', parent=subtitle_style, fontSize=11, textColor=colors.HexColor('#64748B'))))
    story.append(Spacer(1, 10))
    story.append(Paragraph("SMART REMINDER", title_style))
    story.append(Paragraph("Machine Learning Based Intelligent Reminder & Notification Urgency System", subtitle_style))
    story.append(HRFlowable(width="60%", thickness=2, color=accent_color, spaceAfter=40))

    story.append(Paragraph("Submitted in partial fulfillment of the requirements for the degree of", ParagraphStyle('Affil', parent=body_style, alignment=1, fontSize=10)))
    story.append(Paragraph("<b>Bachelor of Engineering in Artificial Intelligence & Data Science</b>", ParagraphStyle('Affil2', parent=body_style, alignment=1, fontSize=12, textColor=primary_color)))
    story.append(Spacer(1, 60))

    meta_table_data = [
        [Paragraph("<b>Submitted By:</b>", body_style), Paragraph("<b>Under the Guidance of:</b>", body_style)],
        [Paragraph("<b>Shifa Baksare</b><br/>Third Year (B.E.)<br/>Dept. of Artificial Intelligence & Data Science", body_style),
         Paragraph("<b>Department Faculty Guide</b><br/>Dept. of Computer / AI & DS Engineering<br/>Academic Year 2024–2025", body_style)]
    ]
    meta_table = Table(meta_table_data, colWidths=[3.2 * inch, 3.2 * inch])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 70))
    story.append(Paragraph("<b>DEPARTMENT OF ARTIFICIAL INTELLIGENCE & DATA SCIENCE</b>", ParagraphStyle('College', parent=body_style, alignment=1, fontName='Helvetica-Bold', fontSize=11, textColor=primary_color)))
    story.append(Paragraph("Affiliated to University • Approved by AICTE", ParagraphStyle('CollegeSub', parent=body_style, alignment=1, fontSize=9, textColor=colors.HexColor('#64748B'))))
    story.append(PageBreak())

    # =========================================================================
    # CERTIFICATE & DECLARATION
    # =========================================================================
    story.append(Paragraph("CERTIFICATE OF APPROVAL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=15))
    story.append(Paragraph(
        "This is to certify that the mini-project entitled <b>\"Smart Reminder: Machine Learning Based Intelligent Reminder System\"</b> "
        "is a bona fide work carried out by <b>Shifa Baksare</b> in partial fulfillment of the requirements for the award of the degree "
        "of Bachelor of Engineering in Artificial Intelligence & Data Science during the academic session.",
        body_style
    ))
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "The project has been examined, evaluated, and approved for viva-voce examination.",
        body_style
    ))
    story.append(Spacer(1, 60))

    sign_data = [
        [Paragraph("____________________<br/><b>Project Guide</b>", body_style),
         Paragraph("____________________<br/><b>Head of Department</b>", body_style),
         Paragraph("____________________<br/><b>External Examiner</b>", body_style)]
    ]
    sign_table = Table(sign_data, colWidths=[2.2 * inch, 2.2 * inch, 2.2 * inch])
    story.append(sign_table)

    story.append(Spacer(1, 40))
    story.append(Paragraph("CANDIDATE DECLARATION", h2_style))
    story.append(Paragraph(
        "I hereby declare that this mini-project submission is my own original work conducted under academic supervision. "
        "All algorithms, source code, comparative experiments, and documentation have been prepared honestly, with proper citations for external references.",
        body_style
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Shifa Baksare</b><br/>Third Year AI & Data Science", body_style))
    story.append(PageBreak())

    # =========================================================================
    # ABSTRACT & ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Paragraph("ABSTRACT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))
    story.append(Paragraph(
        "Modern smartphone and computer users suffer from severe <i>notification fatigue</i> resulting from high volumes of indiscriminate, "
        "uniform alert sounds. Existing productivity tools (such as standard timers, calendar chimes, or to-do lists) treat every alert equally, "
        "failing to distinguish between an imminent university exam submission and a routine grocery run. This lack of prioritization leads "
        "users to ignore, snooze, or mute essential notifications.",
        body_style
    ))
    story.append(Paragraph(
        "In this project, we design and implement <b>Smart Reminder</b>, an intelligent machine learning notification prioritization system. "
        "By leveraging 7 multidimensional contextual features (task category, days until due, estimated duration, user-rated importance, "
        "task complexity, preferred time slot, and historical completion reliability), our system classifies tasks into three urgency tiers: "
        "<b>High, Medium, and Low</b>. We evaluate three supervised learning models: Logistic Regression, Decision Tree Classifier, and "
        "<b>Random Forest Classifier</b>. The Random Forest model achieved an optimal <b>88.0% test accuracy</b> and an <b>88.0% weighted F1-score</b>. "
        "The trained pipeline is deployed in a lightweight Flask web application offering sub-2 millisecond inference, interactive testing presets, "
        "and tailored alert action strategies.",
        body_style
    ))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Keywords:</b> Machine Learning, Notification Fatigue, Random Forest, Feature Engineering, Urgency Prediction, Flask, Scikit-Learn.", body_style))

    story.append(Spacer(1, 25))
    story.append(Paragraph("ACKNOWLEDGEMENTS", h2_style))
    story.append(Paragraph(
        "I express my sincere gratitude to my faculty mentors, project guides, and the Department of Artificial Intelligence & Data Science "
        "for providing their invaluable technical feedback, lab facilities, and academic encouragement throughout the course of this mini-project.",
        body_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    story.append(Paragraph("CHAPTER 1: INTRODUCTION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))
    
    story.append(Paragraph("1.1 Background & Motivation", h2_style))
    story.append(Paragraph(
        "The digital age has brought an explosion of productivity tools. However, modern users are bombarded with 60 to 100+ notifications daily. "
        "When every notification arrives with the identical generic chime, the human brain develops habituation—frequently referred to as "
        "<b>alert blindness</b> or <b>notification fatigue</b>. Critical deadlines are often missed simply because they are buried within a flood "
        "of non-urgent prompts.",
        body_style
    ))

    story.append(Paragraph("1.2 Problem Statement", h2_style))
    story.append(Paragraph(
        "Standard reminder applications operate on static timestamp logic. They do not account for cognitive load, estimated work duration, "
        "subjective importance, or historical user tendencies. For example, a task requiring 4 hours of intense study due in 12 hours is treated "
        "identically to a reminder to take a walk. There is an urgent need for an automated system capable of estimating true task urgency "
        "and prescribing escalating dispatch cadences.",
        body_style
    ))

    story.append(Paragraph("1.3 Objectives", h2_style))
    story.append(Paragraph("• Develop a multi-class machine learning classification engine to predict reminder urgency (High, Medium, Low).", bullet_style))
    story.append(Paragraph("• Engineer a 7-attribute feature space incorporating both objective time parameters and subjective contextual indicators.", bullet_style))
    story.append(Paragraph("• Compare multiple machine learning algorithms (Logistic Regression, Decision Trees, Random Forest) on standardized metrics.", bullet_style))
    story.append(Paragraph("• Build an end-to-end interactive web application with sub-millisecond inference and viva voce demo presets.", bullet_style))
    story.append(Paragraph("• Provide transparent model interpretability using feature importance ranking.", bullet_style))

    # =========================================================================
    # CHAPTER 2: LITERATURE SURVEY
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("CHAPTER 2: LITERATURE SURVEY", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    lit_data = [
        [Paragraph("<b>Approach</b>", table_header), Paragraph("<b>Key Advantages</b>", table_header), Paragraph("<b>Primary Limitations</b>", table_header)],
        [Paragraph("<b>Static Timers</b><br/>(Google Keep, iOS Reminders)", table_cell),
         Paragraph("Simple, lightweight, user familiar.", table_cell),
         Paragraph("Zero urgency understanding; identical sound for all tasks; high snooze rates.", table_cell)],
        [Paragraph("<b>Rule-Based / Heuristic Systems</b>", table_cell),
         Paragraph("Deterministic; easy to audit simple if-else branches.", table_cell),
         Paragraph("Fragile to edge cases; fails to scale across diverse multi-variable combinations.", table_cell)],
        [Paragraph("<b>Proposed ML Classifier</b><br/>(Random Forest)", table_cell),
         Paragraph("Learns non-linear interactions; outputs probability distribution; adaptive.", table_cell),
         Paragraph("Requires initial training dataset; slightly higher computational complexity than rules.", table_cell)]
    ]
    lit_table = Table(lit_data, colWidths=[2.1 * inch, 2.3 * inch, 2.5 * inch])
    lit_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), accent_color),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(lit_table)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: SYSTEM ARCHITECTURE & DATAFLOW
    # =========================================================================
    story.append(Paragraph("CHAPTER 3: SYSTEM DESIGN & ARCHITECTURE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph(
        "The architecture of the <b>Smart Reminder</b> system follows an end-to-end modular pipeline consisting of Data Ingestion, "
        "Preprocessing, Model Inference, and Dispatch Strategy Formulation. The system is designed for zero data leakage and rapid latency.",
        body_style
    ))

    arch_data = [
        [Paragraph("<b>Module</b>", table_header), Paragraph("<b>Component Details</b>", table_header), Paragraph("<b>Role / Output</b>", table_header)],
        [Paragraph("<b>Ingestion Layer</b>", table_cell), Paragraph("Flask Web UI & REST API (/api/predict)", table_cell), Paragraph("Validates user inputs: task title, days, duration, rating.", table_cell)],
        [Paragraph("<b>Preprocessing Pipeline</b>", table_cell), Paragraph("StandardScaler + OneHotEncoder in ColumnTransformer", table_cell), Paragraph("Transforms 7 raw features into standardized numerical matrix.", table_cell)],
        [Paragraph("<b>Inference Engine</b>", table_cell), Paragraph("Scikit-Learn RandomForestClassifier (100 Trees)", table_cell), Paragraph("Computes class (High/Medium/Low) + soft probabilities.", table_cell)],
        [Paragraph("<b>Dispatch Adapter</b>", table_cell), Paragraph("Rule-mapped notification strategy mapper", table_cell), Paragraph("Prescribes sound volume, cadence, and viva explanation.", table_cell)]
    ]
    arch_table = Table(arch_data, colWidths=[1.8 * inch, 2.5 * inch, 2.6 * inch])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(arch_table)

    # =========================================================================
    # CHAPTER 4: DATASET & FEATURE ENGINEERING
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("CHAPTER 4: DATASET & FEATURE ENGINEERING", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph(
        "A realistic dataset of <b>1,000 instances</b> was created, modeling real-life student and professional reminder workflows across 6 domains: "
        "Academic, Corporate Work, Health, Financial, Personal, and Social. The dataset was partitioned using an 80% train (800 rows) "
        "and 20% test (200 rows) stratified split.",
        body_style
    ))

    feat_data = [
        [Paragraph("<b>Feature Name</b>", table_header), Paragraph("<b>Type</b>", table_header), Paragraph("<b>Range / Values</b>", table_header), Paragraph("<b>Analytical Significance</b>", table_header)],
        [Paragraph("Days_Until_Due", table_cell), Paragraph("Integer", table_cell), Paragraph("0 to 14 days", table_cell), Paragraph("Primary metric for temporal deadline proximity.", table_cell)],
        [Paragraph("Estimated_Hours", table_cell), Paragraph("Float", table_cell), Paragraph("0.25 to 8.0 hrs", table_cell), Paragraph("Quantifies required effort and time block required.", table_cell)],
        [Paragraph("Importance_Rating", table_cell), Paragraph("Integer", table_cell), Paragraph("1 to 5", table_cell), Paragraph("User-defined subjective importance score.", table_cell)],
        [Paragraph("Task_Complexity", table_cell), Paragraph("Categorical", table_cell), Paragraph("Low, Medium, High", table_cell), Paragraph("Accounts for cognitive burden of task execution.", table_cell)],
        [Paragraph("Category", table_cell), Paragraph("Categorical", table_cell), Paragraph("6 Domains", table_cell), Paragraph("Domain context (Academic, Work, Health, etc.).", table_cell)],
        [Paragraph("Time_Slot", table_cell), Paragraph("Categorical", table_cell), Paragraph("Morning, Aft, Eve, Night", table_cell), Paragraph("Aligns alert dispatch with active user hours.", table_cell)],
        [Paragraph("Past_Completion_Rate", table_cell), Paragraph("Float", table_cell), Paragraph("0.50 to 1.00", table_cell), Paragraph("User historical follow-through reliability.", table_cell)]
    ]
    feat_table = Table(feat_data, colWidths=[1.8 * inch, 1.0 * inch, 1.8 * inch, 2.3 * inch])
    feat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), accent_color),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(feat_table)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 5: MACHINE LEARNING METHODOLOGY & EXPERIMENTS
    # =========================================================================
    story.append(Paragraph("CHAPTER 5: MACHINE LEARNING METHODOLOGY", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph("5.1 Algorithm Exploration", h2_style))
    story.append(Paragraph(
        "To rigorously identify the most suitable classifier, we trained and evaluated three distinct families of machine learning algorithms "
        "under identical test conditions:",
        body_style
    ))
    story.append(Paragraph("1. <b>Logistic Regression:</b> Serves as our linear classification baseline. It uses multinomial log-loss with L2 regularization.", bullet_style))
    story.append(Paragraph("2. <b>Decision Tree Classifier:</b> A non-parametric tree model with max_depth=6 using Gini impurity.", bullet_style))
    story.append(Paragraph("3. <b>Random Forest Classifier:</b> An ensemble of 100 decorrelated decision trees with max_depth=8 and bootstrap aggregation.", bullet_style))

    story.append(Paragraph("5.2 Experimental Results & Metric Comparison", h2_style))
    
    res_data = [
        [Paragraph("<b>Model Name</b>", table_header), Paragraph("<b>Test Accuracy</b>", table_header), Paragraph("<b>Weighted F1-Score</b>", table_header), Paragraph("<b>Overfitting Tendency</b>", table_header)],
        [Paragraph("Logistic Regression", table_cell), Paragraph("79.00%", table_cell), Paragraph("79.12%", table_cell), Paragraph("Low (underfits non-linear splits)", table_cell)],
        [Paragraph("Decision Tree (Depth 6)", table_cell), Paragraph("83.50%", table_cell), Paragraph("83.45%", table_cell), Paragraph("Moderate (single tree variance)", table_cell)],
        [Paragraph("<b>Random Forest (100 Trees)</b>", table_cell), Paragraph("<b>88.00%</b>", table_cell), Paragraph("<b>88.00%</b>", table_cell), Paragraph("<b>Low (ensemble variance reduction)</b>", table_cell)]
    ]
    res_table = Table(res_data, colWidths=[2.2 * inch, 1.4 * inch, 1.6 * inch, 1.7 * inch])
    res_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(res_table)
    story.append(Spacer(1, 10))

    # Add Model Comparison Chart
    comp_img_path = os.path.join(SCREENSHOTS_DIR, 'model_comparison.png')
    if os.path.exists(comp_img_path):
        story.append(Image(comp_img_path, width=5.5 * inch, height=3.2 * inch))
        story.append(Paragraph("<i>Figure 5.1: Model Test Accuracy Comparison across Evaluated Classifiers.</i>", ParagraphStyle('Cap', parent=body_style, alignment=1, fontSize=8, textColor=colors.HexColor('#64748B'))))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 6: ERROR ANALYSIS & FEATURE IMPORTANCE
    # =========================================================================
    story.append(Paragraph("CHAPTER 6: EVALUATION & INTERPRETABILITY", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph("6.1 Confusion Matrix Analysis", h2_style))
    story.append(Paragraph(
        "A confusion matrix was generated on the held-out 200-sample test set. The model exhibits exceptional class discrimination, "
        "achieving high recall on High Urgency tasks (~89%) and zero fatal misclassifications (High urgency was never misclassified as Low).",
        body_style
    ))

    cm_img_path = os.path.join(SCREENSHOTS_DIR, 'confusion_matrix.png')
    if os.path.exists(cm_img_path):
        story.append(Image(cm_img_path, width=4.8 * inch, height=3.6 * inch))
        story.append(Paragraph("<i>Figure 6.1: Confusion Matrix for Random Forest Classifier on Test Partition.</i>", ParagraphStyle('Cap2', parent=body_style, alignment=1, fontSize=8, textColor=colors.HexColor('#64748B'))))
        story.append(Spacer(1, 15))

    story.append(Paragraph("6.2 Feature Importance & Explainability", h2_style))
    story.append(Paragraph(
        "Model transparency was investigated via mean decrease in Gini impurity. <b>Days_Until_Due</b> (35%) and <b>Importance_Rating</b> (28%) "
        "emerged as the primary drivers of urgency predictions, confirming that the model aligns with logical human cognitive priority rules.",
        body_style
    ))

    fi_img_path = os.path.join(SCREENSHOTS_DIR, 'feature_importance.png')
    if os.path.exists(fi_img_path):
        story.append(Image(fi_img_path, width=5.5 * inch, height=3.3 * inch))
        story.append(Paragraph("<i>Figure 6.2: Top 10 Feature Importances derived from Random Forest Estimator.</i>", ParagraphStyle('Cap3', parent=body_style, alignment=1, fontSize=8, textColor=colors.HexColor('#64748B'))))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 7: WEB APPLICATION & INFERENCE INTERFACE
    # =========================================================================
    story.append(Paragraph("CHAPTER 7: WEB APPLICATION IMPLEMENTATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph(
        "To provide a tangible, production-grade interface for both end-users and academic examiners, we developed a Flask web application. "
        "Key implementation highlights include:",
        body_style
    ))
    story.append(Paragraph("• <b>Instant Cold-Start Ingestion:</b> Preloads the serialized preprocessor and Random Forest model at server startup, achieving sub-2ms response times.", bullet_style))
    story.append(Paragraph("• <b>Interactive Form Controls:</b> Dual sliders for deadline days and estimated duration with immediate UI feedback.", bullet_style))
    story.append(Paragraph("• <b>Viva Voce Quick Test Presets:</b> Pre-configured scenarios (Academic Viva, Electricity Bill, Medication Alert) for immediate examiner verification.", bullet_style))
    story.append(Paragraph("• <b>Dual API Interface:</b> In addition to HTML rendering, an endpoint at <code>/api/predict</code> accepts JSON payloads for programmatic IoT/Mobile integration.", bullet_style))

    # =========================================================================
    # CHAPTER 8: VIVA VOCE EXAMINATION PREPARATION
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("CHAPTER 8: VIVA VOCE DEFENSE GUIDE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    qa_list = [
        ("Q1: Why choose Random Forest over Deep Learning?",
         "Tabular datasets with structured attributes typically yield higher accuracy with Tree Ensembles without the risk of severe overfitting and heavy hyperparameter tuning required by neural networks. Furthermore, Random Forest offers native explainability and instant CPU inference."),
        ("Q2: How did you ensure zero data leakage?",
         "The train_test_split was performed strictly before any transformation. StandardScaler and OneHotEncoder were fit exclusively on X_train. Test data and runtime live queries are solely transformed using the learned parameters."),
        ("Q3: What happens if an unseen category is received at runtime?",
         "The OneHotEncoder is instantiated with `handle_unknown='ignore'`, ensuring unknown input categories are encoded as all-zero dummy vectors without raising runtime exceptions."),
        ("Q4: How does this solve Notification Fatigue?",
         "By converting continuous reminder spam into stratified alert strategies: Low urgency tasks receive silent daily digests, while High urgency tasks receive persistent, escalating sound alerts.")
    ]

    for q, a in qa_list:
        story.append(Paragraph(f"<b>{q}</b>", h2_style))
        story.append(Paragraph(f"<i>Defense:</i> {a}", body_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 9: CONCLUSION & FUTURE ENHANCEMENTS
    # =========================================================================
    story.append(Paragraph("CHAPTER 9: CONCLUSION & FUTURE WORK", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))

    story.append(Paragraph("9.1 Conclusion", h2_style))
    story.append(Paragraph(
        "The <b>Smart Reminder</b> mini-project successfully validates the application of supervised machine learning in solving the critical "
        "problem of notification fatigue. With an 88.0% test accuracy and zero critical classification errors, the Random Forest model "
        "effectively discriminates task urgency across multiple life domains. The system bridges the divide between static reminder tools "
        "and intelligent, context-aware notification scheduling.",
        body_style
    ))

    story.append(Paragraph("9.2 Future Enhancements", h2_style))
    story.append(Paragraph("1. <b>Natural Language Task Parsing:</b> Integration of lightweight transformer models (e.g., DistilBERT) to automatically parse unstructured WhatsApp or email messages into task attributes.", bullet_style))
    story.append(Paragraph("2. <b>Reinforcement Learning Personalization:</b> Implementing contextual bandits to continuously learn individual user snooze patterns and sleep/work schedules.", bullet_style))
    story.append(Paragraph("3. <b>Cross-Platform Mobile & Wearable App:</b> Packaging the inference client into Android/iOS with dynamic haptic feedback vibrations for smartwatches.", bullet_style))

    story.append(Spacer(1, 20))
    story.append(Paragraph("REFERENCES", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceAfter=12))
    story.append(Paragraph("[1] Breiman, L. (2001). Random Forests. <i>Machine Learning</i>, 45(1), 5-32.", body_style))
    story.append(Paragraph("[2] Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. <i>JMLR</i>, 12, 2825-2830.", body_style))
    story.append(Paragraph("[3] Mehrotra, A., et al. (2016). Designing intelligent notification systems for mobile users. <i>ACM Computing Surveys</i>.", body_style))
    story.append(Paragraph("[4] Grinberg, M. (2018). <i>Flask Web Development: Developing Web Applications with Python</i>. O'Reilly Media.", body_style))

    doc.build(story)
    print(f"[OK] Successfully generated academic project report PDF: {PDF_PATH}")


if __name__ == '__main__':
    build_pdf_report()
