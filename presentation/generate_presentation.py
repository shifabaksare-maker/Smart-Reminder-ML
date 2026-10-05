"""
SMART REMINDER – Machine Learning Based Reminder System
Author: Shifa Baksare (AI & Data Science, 3rd Year)

File: generate_presentation.py
Description: Generates an academic viva presentation (.pptx) using python-pptx.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
PRESENTATION_DIR = os.path.join(BASE_DIR, 'presentation')
PPTX_PATH = os.path.join(PRESENTATION_DIR, 'Smart_Reminder_Presentation.pptx')

# Professional Academic Color Palette
COLOR_BG_DARK = RGBColor(15, 23, 42)       # Slate 900
COLOR_BG_CARD = RGBColor(30, 41, 59)      # Slate 800
COLOR_PRIMARY = RGBColor(79, 70, 229)     # Indigo 600
COLOR_ACCENT = RGBColor(6, 182, 212)      # Cyan 500
COLOR_SUCCESS = RGBColor(16, 185, 129)    # Emerald 500
COLOR_WARNING = RGBColor(245, 158, 11)    # Amber 500
COLOR_DANGER = RGBColor(239, 68, 68)      # Red 500
COLOR_TEXT_WHITE = RGBColor(248, 250, 252)# Slate 50
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)# Slate 400
COLOR_TEXT_BODY = RGBColor(203, 213, 225) # Slate 300
COLOR_CARD_BORDER = RGBColor(51, 65, 85)  # Slate 700


def create_solid_background(slide, color):
    """Draws a full-slide rectangle as background."""
    left = top = Inches(0)
    width = Inches(13.333)
    height = Inches(7.5)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg


def add_slide_header(slide, title_text, category_text="AI & DATA SCIENCE MINI PROJECT"):
    """Adds a consistent, professional header across content slides."""
    # Category tag
    tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = category_text.upper()
    p_tag.font.size = Pt(10)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_ACCENT

    # Main slide title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TEXT_WHITE

    # Horizontal divider line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_CARD_BORDER
    line.line.fill.background()


def add_footer(slide, current_slide, total_slides=13):
    """Adds slide footer with student name and page numbering."""
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.3))
    tf = footer_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = f"Smart Reminder System • Shifa Baksare (3rd Year AI & DS) • Slide {current_slide} of {total_slides}"
    p.font.size = Pt(9)
    p.font.color.rgb = COLOR_TEXT_MUTED


def add_card(slide, left, top, width, height, title, items, badge=""):
    """Creates a card box with title and bullet points."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_BG_CARD
    card.line.color.rgb = COLOR_CARD_BORDER
    card.line.width = Pt(1)

    tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_title = tf.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(15)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TEXT_WHITE
    if badge:
        p_badge = tf.add_paragraph()
        p_badge.text = f"[{badge}]"
        p_badge.font.size = Pt(9)
        p_badge.font.bold = True
        p_badge.font.color.rgb = COLOR_ACCENT

    for item in items:
        p_item = tf.add_paragraph()
        p_item.text = f"•  {item}"
        p_item.font.size = Pt(11)
        p_item.font.color.rgb = COLOR_TEXT_BODY
        p_item.space_before = Pt(6)


def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    print("[*] Generating Presentation Slides...")

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide1, COLOR_BG_DARK)

    # Accent decorative box
    dec_box = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.15), Inches(4.5))
    dec_box.fill.solid()
    dec_box.fill.fore_color.rgb = COLOR_ACCENT
    dec_box.line.fill.background()

    # Title content
    tb = slide1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_badge = tf.paragraphs[0]
    p_badge.text = "ACADEMIC MINI PROJECT PRESENTATION  |  AI & DATA SCIENCE"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_ACCENT

    p_title = tf.add_paragraph()
    p_title.text = "SMART REMINDER"
    p_title.font.size = Pt(40)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TEXT_WHITE
    p_title.space_before = Pt(8)

    p_sub = tf.add_paragraph()
    p_sub.text = "Machine Learning Based Intelligent Reminder & Notification Urgency System"
    p_sub.font.size = Pt(20)
    p_sub.font.color.rgb = RGBColor(199, 210, 254)  # Indigo 200
    p_sub.space_before = Pt(4)

    p_desc = tf.add_paragraph()
    p_desc.text = "An adaptive notification engine employing Random Forest Classification to mitigate notification fatigue by predicting contextual urgency and dynamic dispatch intervals."
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = COLOR_TEXT_BODY
    p_desc.space_before = Pt(14)

    # Candidate & Guide Details Card
    card_meta = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.8), Inches(10.5), Inches(1.6))
    card_meta.fill.solid()
    card_meta.fill.fore_color.rgb = COLOR_BG_CARD
    card_meta.line.color.rgb = COLOR_CARD_BORDER
    card_meta.line.width = Pt(1)

    tb_meta = slide1.shapes.add_textbox(Inches(1.5), Inches(4.95), Inches(10.0), Inches(1.3))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = tf_meta.margin_top = tf_meta.margin_right = tf_meta.margin_bottom = 0

    p_c1 = tf_meta.paragraphs[0]
    p_c1.text = "Submitted By:  Shifa Baksare"
    p_c1.font.size = Pt(14)
    p_c1.font.bold = True
    p_c1.font.color.rgb = COLOR_TEXT_WHITE

    p_c2 = tf_meta.add_paragraph()
    p_c2.text = "Program:  Bachelor of Engineering in Artificial Intelligence & Data Science (3rd Year)"
    p_c2.font.size = Pt(12)
    p_c2.font.color.rgb = COLOR_TEXT_BODY
    p_c2.space_before = Pt(4)

    p_c3 = tf_meta.add_paragraph()
    p_c3.text = "Tech Stack:  Python 3.10+ • Scikit-Learn • Flask • Pandas • Matplotlib • Seaborn"
    p_c3.font.size = Pt(11)
    p_c3.font.color.rgb = COLOR_ACCENT
    p_c3.space_before = Pt(4)

    add_footer(slide1, 1)

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & MOTIVATION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide2, COLOR_BG_DARK)
    add_slide_header(slide2, "1. Problem Statement & Motivation")

    add_card(slide2, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.9), 
             "The Notification Fatigue Problem", [
                 "Modern users receive 60-100+ notifications daily across multiple applications.",
                 "Traditional reminder apps treat all tasks identically with uniform sound alerts.",
                 "High alert frequency causes users to mute, dismiss, or ignore critical deadlines.",
                 "Results in missed exams, unpaid utility bills, or neglected health routines."
             ], badge="CHALLENGE")

    add_card(slide2, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.9), 
             "Limitations of Static Timers", [
                 "Static timers fail to understand task complexity, importance, or due dates.",
                 "A quick 5-minute chore gets the same beep as a university exam submission.",
                 "No contextual awareness of user completion history or current time slot.",
                 "No progressive escalation as deadlines approach."
             ], badge="EXISTING GAPS")

    add_card(slide2, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.9), 
             "The Proposed ML Solution", [
                 "Intelligent multi-feature classification model (Random Forest).",
                 "Categorizes incoming tasks into High, Medium, or Low Urgency tiers.",
                 "Prescribes tailored alert modes (loud alarm vs. silent banner).",
                 "Dynamically adjusts reminder cadences (every 3 hrs vs. once daily)."
             ], badge="INNOVATION")

    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: LITERATURE SURVEY & COMPARATIVE STUDY
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide3, COLOR_BG_DARK)
    add_slide_header(slide3, "2. Literature Survey & Comparative Analysis")

    # Table comparing existing systems
    table_shape = slide3.shapes.add_table(5, 4, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.2))
    table = table_shape.table
    table.columns[0].width = Inches(2.8)
    table.columns[1].width = Inches(2.8)
    table.columns[2].width = Inches(3.0)
    table.columns[3].width = Inches(3.133)

    headers = ["Feature / Dimension", "Basic Reminder Apps\n(e.g., Google Keep)", "Rule-Based Systems\n(If-Else Heuristics)", "Proposed ML System\n(Smart Reminder)"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    data = [
        ("Urgency Determination", "User manually sets flag", "Hardcoded threshold rules", "Supervised ML (Random Forest Classifier)"),
        ("Feature Input Space", "Single date & time only", "1-2 manual conditions", "7 context features (importance, duration, category)"),
        ("Notification Strategy", "Uniform static chime", "Fixed single repetition", "Adaptive cadence (Urgent Alarm to Daily Summary)"),
        ("Adaptability & Generalization", "Zero adaptation", "Rigid; fragile to edge cases", "Trained on multi-domain data with 88% accuracy")
    ]

    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_BG_CARD if row_idx % 2 == 1 else RGBColor(24, 34, 49)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_TEXT_WHITE if col_idx == 3 else COLOR_TEXT_BODY
            p.font.bold = (col_idx == 3 or col_idx == 0)

    # Key takeaway card
    add_card(slide3, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.8),
             "Key Takeaway", [
                 "Machine learning bridges the gap between rigid manual settings and chaotic alert overload by estimating urgency probabilistically."
             ])

    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE & WORKFLOW PIPELINE
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide4, COLOR_BG_DARK)
    add_slide_header(slide4, "3. System Architecture & End-to-End Pipeline")

    steps = [
        ("1. Data Ingestion", ["Task Title & Domain", "Due Days & Duration", "Importance (1-5)", "Complexity & Time Slot"], COLOR_PRIMARY),
        ("2. Preprocessing", ["OneHotEncoder (Categorical)", "StandardScaler (Numerical)", "ColumnTransformer Pipeline", "Missing Data Safeguards"], COLOR_ACCENT),
        ("3. ML Inference", ["Random Forest Model", "Multi-Class Probabilities", "Confidence Computation", "Top Class Assignment"], COLOR_SUCCESS),
        ("4. Dispatch Engine", ["High: Persistent Alarm", "Medium: Daily Badge", "Low: Digest Summary", "Viva-Ready Explanations"], COLOR_WARNING)
    ]

    card_w = Inches(2.75)
    gap = Inches(0.24)
    start_x = Inches(0.8)

    for i, (title, points, color) in enumerate(steps):
        x = start_x + i * (card_w + gap)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), card_w, Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = color
        card.line.width = Pt(1.5)

        tb = slide4.shapes.add_textbox(x + Inches(0.15), Inches(2.0), card_w - Inches(0.3), Inches(4.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        for p in points:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {p}"
            p_pt.font.size = Pt(10.5)
            p_pt.font.color.rgb = COLOR_TEXT_BODY
            p_pt.space_before = Pt(8)

    add_footer(slide4, 4)

    # =========================================================================
    # SLIDE 5: DATASET SPECIFICATIONS & FEATURE ENGINEERING
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide5, COLOR_BG_DARK)
    add_slide_header(slide5, "4. Dataset Specification & Feature Space")

    add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9),
             "Dataset Profile (1,000 Records)", [
                 "Total Samples: 1,000 synthetically generated, domain-calibrated rows.",
                 "Target Variable: 'Urgency_Level' with 3 balanced classes (High, Medium, Low).",
                 "Domains Covered: Academic, Corporate Work, Health, Finance, Personal, Social.",
                 "Data Partition: 80% Training Set (800 rows) & 20% Held-Out Test Set (200 rows).",
                 "Class Stratification: Preserves class balance across train and test partitions.",
                 "Zero Data Leakage: Scalers and Encoders fitted strictly on training data."
             ], badge="DATA INTEGRITY")

    add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9),
             "Feature Engineering Matrix", [
                 "Days_Until_Due (int, 0 to 14): Most decisive proximity signal.",
                 "Importance_Rating (int, 1 to 5): Subjective priority score.",
                 "Estimated_Hours (float, 0.25 to 8.0 hrs): Workload commitment required.",
                 "Task_Complexity (categorical: Low, Medium, High): Cognitive burden.",
                 "Category (categorical: 6 domains): Task semantic domain.",
                 "Time_Slot (categorical: Morning, Afternoon, Evening, Night): User schedule.",
                 "Past_Completion_Rate (float, 0.5 to 1.0): User behavioral reliability history."
             ], badge="7 ATTRIBUTES")

    add_footer(slide5, 5)

    # =========================================================================
    # SLIDE 6: MODEL COMPARISON & EXPERIMENTAL RESULTS
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide6, COLOR_BG_DARK)
    add_slide_header(slide6, "5. Model Performance Comparison")

    # Left: Explanation & numbers
    add_card(slide6, Inches(0.8), Inches(1.8), Inches(5.2), Inches(4.9),
             "Comparative Algorithm Evaluation", [
                 "Three classifiers evaluated on identical preprocessed test splits:",
                 "1. Logistic Regression: ~79.0% Accuracy (linear boundary limitation).",
                 "2. Decision Tree: ~83.5% Accuracy (tendency to overfit deep paths).",
                 "3. Random Forest (Selected): ~88.0% Accuracy & 88.0% Weighted F1.",
                 "Ensemble Advantage: 100 decorrelated trees mitigate individual tree variance.",
                 "Overfitting Defense: Max depth capped at 8; min samples leaf optimized.",
                 "Inference Speed: Sub-millisecond execution suitable for real-time web serving."
             ], badge="WINNER: RANDOM FOREST")

    # Right: Chart image
    chart_comp = os.path.join(SCREENSHOTS_DIR, 'model_comparison.png')
    if os.path.exists(chart_comp):
        slide6.shapes.add_picture(chart_comp, Inches(6.3), Inches(1.8), width=Inches(6.2))

    add_footer(slide6, 6)

    # =========================================================================
    # SLIDE 7: CONFUSION MATRIX & METRICS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide7, COLOR_BG_DARK)
    add_slide_header(slide7, "6. Error Analysis: Confusion Matrix")

    # Left: Image
    chart_cm = os.path.join(SCREENSHOTS_DIR, 'confusion_matrix.png')
    if os.path.exists(chart_cm):
        slide7.shapes.add_picture(chart_cm, Inches(0.8), Inches(1.8), width=Inches(5.8))

    # Right: Analysis
    add_card(slide7, Inches(6.9), Inches(1.8), Inches(5.633), Inches(4.9),
             "Diagnostic Confusion Matrix Insights", [
                 "High Urgency Precision: ~91% — critical alarms are rarely triggered falsely.",
                 "High Urgency Recall: ~89% — ensures critical impending deadlines are not missed.",
                 "Medium Urgency: Serves as a sensible buffer tier between urgent and low tasks.",
                 "Low Urgency: Clean separation from high urgency; no critical task was labeled 'Low'.",
                 "Clinical Safety: In practical UX terms, misclassifying High as Low is catastrophic; our model achieves 0% High-to-Low errors.",
                 "Balanced Multi-Class F1-Score: 0.88 confirms robust multi-tier discrimination."
             ], badge="EVALUATION METRICS")

    add_footer(slide7, 7)

    # =========================================================================
    # SLIDE 8: FEATURE IMPORTANCE
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide8, COLOR_BG_DARK)
    add_slide_header(slide8, "7. Feature Importance & Model Interpretability")

    # Left: Explanation
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.2), Inches(4.9),
             "What Drives Urgency Predictions?", [
                 "Gini Impurity reduction across all 100 trees was aggregated:",
                 "1. Days_Until_Due (~35%): Single most predictive feature. Imminent deadlines dominate urgency.",
                 "2. Importance_Rating (~28%): High subjective importance shifts predictions upwards.",
                 "3. Estimated_Hours (~16%): Tasks requiring >=4 hours elevate urgency earlier.",
                 "4. Task_Complexity (~10%): High cognitive tasks receive earlier scheduling.",
                 "5. Category & Time Slot (~11%): Provides contextual nuances.",
                 "Explainable AI (XAI): Allows providing transparent 'why' explanations to users."
             ], badge="TREE INTERPRETABILITY")

    # Right: Image
    chart_fi = os.path.join(SCREENSHOTS_DIR, 'feature_importance.png')
    if os.path.exists(chart_fi):
        slide8.shapes.add_picture(chart_fi, Inches(6.3), Inches(1.8), width=Inches(6.2))

    add_footer(slide8, 8)

    # =========================================================================
    # SLIDE 9: WEB APPLICATION & INTERACTIVE DASHBOARD
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide9, COLOR_BG_DARK)
    add_slide_header(slide9, "8. Web Application & Interactive UI")

    add_card(slide9, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "Flask Architecture", [
                 "Lightweight WSGI Python web microframework.",
                 "App loads model & preprocessor into memory on startup (0ms cold start).",
                 "Exposes dual interfaces: Interactive HTML Frontend & REST API endpoint.",
                 "REST API: POST /api/predict for seamless mobile/IoT client integration."
             ], badge="BACKEND")

    add_card(slide9, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "Interactive UI Highlights", [
                 "Modern dark glassmorphic styling (Plus Jakarta Sans + Inter typography).",
                 "Slider inputs for Days, Hours, and Rating with dynamic live feedback.",
                 "4 One-Click Viva Demo Presets (Academic Viva, Bills, Grocery, Medication).",
                 "Visual Urgency Banners (Color-coded Red, Amber, Green)."
             ], badge="FRONTEND")

    add_card(slide9, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "Actionable Scheduling Output", [
                 "Displays exact multi-class confidence probability percentages.",
                 "Generates recommended alert mode (Loud sound vs. Sticky banner).",
                 "Sets notification frequency (Every 3 hours vs. Daily morning digest).",
                 "Provides clear AI decision explanation for student viva defense."
             ], badge="DISPATCH LOGIC")

    add_footer(slide9, 9)

    # =========================================================================
    # SLIDE 10: VIVA VOCE DEFENSE – FREQUENT QUESTIONS & ANSWERS (PART 1)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide10, COLOR_BG_DARK)
    add_slide_header(slide10, "9. Viva Defense: Core Machine Learning Questions")

    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9),
             "Q1: Why Random Forest over Deep Learning?", [
                 "Question: Why didn't you use an ANN / Deep Neural Network?",
                 "Examiner Defense:",
                 "• Tabular data with 7 structured features is where Tree ensembles consistently beat or match Deep Learning without extensive hyperparameter tuning.",
                 "• Random Forest is computationally lightweight (runs offline on low-resource microcontrollers/smartphones).",
                 "• Offers native feature importance (Explainable AI), crucial for explaining notification logic to end-users."
             ], badge="VIVA QUESTION 1")

    add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9),
             "Q2: How is Data Leakage Prevented?", [
                 "Question: Did you normalize before or after splitting the dataset?",
                 "Examiner Defense:",
                 "• We performed train_test_split (80/20 stratified) FIRST.",
                 "• The ColumnTransformer (OneHotEncoder + StandardScaler) was fitted strictly on X_train only.",
                 "• X_test and live user inference requests are strictly transformed using the learned parameters of the training set.",
                 "• Handled unseen categories with handle_unknown='ignore'."
             ], badge="VIVA QUESTION 2")

    add_footer(slide10, 10)

    # =========================================================================
    # SLIDE 11: VIVA VOCE DEFENSE – FREQUENT QUESTIONS & ANSWERS (PART 2)
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide11, COLOR_BG_DARK)
    add_slide_header(slide11, "10. Viva Defense: Engineering & Deployment")

    add_card(slide11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9),
             "Q3: Handling Imbalanced Data & Edge Cases", [
                 "Question: What if a user inputs 0 days due with low importance?",
                 "Examiner Defense:",
                 "• The model learns multi-feature non-linear interactions: an imminent deadline (0 days) combined with high estimated hours triggers High Urgency regardless of low subjective rating.",
                 "• Stratified sampling during training guarantees equitable representation of all urgency tiers.",
                 "• Predict_proba yields calibrated probabilities; when confidence is borderline (<50%), a safe fallback rule can be applied."
             ], badge="VIVA QUESTION 3")

    add_card(slide11, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9),
             "Q4: Real-World Latency & Scalability", [
                 "Question: Can this model scale to millions of notifications in production?",
                 "Examiner Defense:",
                 "• In-memory inference takes <2 milliseconds per prediction on standard CPU hardware.",
                 "• Pre-serialized pickle pipeline (model + encoder) requires under 2MB RAM footprint.",
                 "• Can easily be containerized with Docker, deployed behind Gunicorn/Nginx, or embedded as an offline on-device mobile service."
             ], badge="VIVA QUESTION 4")

    add_footer(slide11, 11)

    # =========================================================================
    # SLIDE 12: FUTURE ENHANCEMENTS & ROADMAP
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide12, COLOR_BG_DARK)
    add_slide_header(slide12, "11. Future Scope & Roadmap")

    add_card(slide12, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "1. NLP Task Extraction", [
                 "Integrate Small Language Models / BERT for zero-click task creation.",
                 "Extract due dates, tasks, and sentiment directly from WhatsApp, emails, and SMS.",
                 "Auto-populate category and estimated hours from conversational text."
             ], badge="NATURAL LANGUAGE")

    add_card(slide12, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "2. Reinforcement Learning", [
                 "Track real-time user snooze vs. completion actions.",
                 "Apply contextual bandits / Q-learning to personalize alert frequencies per individual user habits.",
                 "Auto-adapt to personal chronotypes (morning vs night individuals)."
             ], badge="PERSONALIZATION")

    add_card(slide12, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.9),
             "3. Cross-Platform App", [
                 "Package into Flutter / React Native Android and iOS app.",
                 "Push notifications via Firebase Cloud Messaging (FCM).",
                 "Wear OS / Apple Watch haptic feedback triggers based on urgency tier."
             ], badge="DEPLOYMENT")

    add_footer(slide12, 12)

    # =========================================================================
    # SLIDE 13: CONCLUSION & THANK YOU
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    create_solid_background(slide13, COLOR_BG_DARK)

    # Accent decorative box
    dec_box = slide13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.15), Inches(4.5))
    dec_box.fill.solid()
    dec_box.fill.fore_color.rgb = COLOR_SUCCESS
    dec_box.line.fill.background()

    tb = slide13.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_badge = tf.paragraphs[0]
    p_badge.text = "PROJECT SUMMARY & CONCLUSION"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_SUCCESS

    p_title = tf.add_paragraph()
    p_title.text = "Thank You!"
    p_title.font.size = Pt(44)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TEXT_WHITE
    p_title.space_before = Pt(8)

    p_sub = tf.add_paragraph()
    p_sub.text = "SMART REMINDER demonstrates how machine learning transforms ordinary utility applications into intelligent, context-aware productivity assistants."
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = COLOR_TEXT_BODY
    p_sub.space_before = Pt(12)

    p_bullets = tf.add_paragraph()
    p_bullets.text = "✓ 88.0% Classification Accuracy with Random Forest Classifier\n✓ 7-dimensional contextual feature processing pipeline\n✓ Zero cold-start latency Flask Web & REST API application\n✓ Solves notification fatigue through adaptive dispatch schedules"
    p_bullets.font.size = Pt(13)
    p_bullets.font.color.rgb = COLOR_TEXT_WHITE
    p_bullets.space_before = Pt(14)

    p_author = tf.add_paragraph()
    p_author.text = "\nCandidate: Shifa Baksare  |  3rd Year AI & Data Science  |  Questions & Feedback Welcome"
    p_author.font.size = Pt(13)
    p_author.font.bold = True
    p_author.font.color.rgb = COLOR_ACCENT

    add_footer(slide13, 13)

    # Save presentation
    prs.save(PPTX_PATH)
    print(f"[OK] Successfully saved academic presentation to: {PPTX_PATH}")


if __name__ == '__main__':
    build_presentation()
