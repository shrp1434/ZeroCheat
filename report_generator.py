"""
report_generator.py
Generates a PDF exam report using ReportLab.
Includes: identity results, risk graph, behaviour timeline, event log.
"""

import os
import time
import matplotlib
matplotlib.use("Agg")  # non-GUI backend for server use
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, HRFlowable
)
from reportlab.lib import colors
from database import (
    get_connection, get_risk_scores_for_session,
    get_events_for_session
)

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)


def _generate_risk_graph(session_id: int, output_path: str):
    """Generate a matplotlib line graph of risk score over time."""
    rows = get_risk_scores_for_session(session_id)
    if not rows:
        return None

    timestamps    = list(range(len(rows)))
    risk_scores   = [r["risk_score"]        for r in rows]
    cheat_probs   = [r["cheating_probability"] for r in rows]
    identity_conf = [r["identity_confidence"] * 100 for r in rows]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(timestamps, risk_scores,   label="Risk Score",         color="red",    linewidth=2)
    ax.plot(timestamps, cheat_probs,   label="Cheating Prob (%)",  color="orange", linewidth=2)
    ax.plot(timestamps, identity_conf, label="Identity Conf (%)",  color="green",  linewidth=2)
    ax.set_xlabel("Time (samples)")
    ax.set_ylabel("Score / Probability (%)")
    ax.set_title(f"Session {session_id} - Risk Analysis Over Time")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 110)
    plt.tight_layout()
    plt.savefig(output_path, dpi=100)
    plt.close()
    return output_path


def generate_report(session_id: int, user_id: int) -> str:
    """
    Generate a full PDF report for the given session.
    Returns the path to the saved PDF.
    """
    pdf_path = os.path.join(REPORTS_DIR, f"report_session_{session_id}.pdf")
    graph_path = os.path.join(REPORTS_DIR, f"graph_{session_id}.png")

    # Generate risk graph image
    _generate_risk_graph(session_id, graph_path)

    # Get session info
    conn = get_connection()
    session = dict(conn.execute(
        "SELECT es.*, u.username, u.full_name FROM exam_sessions es "
        "JOIN users u ON es.user_id = u.id WHERE es.id=?", (session_id,)
    ).fetchone() or {})
    conn.close()

    events     = get_events_for_session(session_id)
    risk_rows  = get_risk_scores_for_session(session_id)
    final_risk = risk_rows[-1]["risk_score"]        if risk_rows else 0
    final_prob = risk_rows[-1]["cheating_probability"] if risk_rows else 0

    # Build PDF
    doc    = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story  = []

    # Title
    story.append(Paragraph("🎓 Exam Integrity Report", styles["Title"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 0.5 * cm))

    # Session Details
    story.append(Paragraph("Session Information", styles["Heading2"]))
    info_data = [
        ["Candidate",   session.get("full_name", "Unknown")],
        ["Username",    session.get("username", "Unknown")],
        ["Session ID",  str(session_id)],
        ["Start Time",  str(session.get("start_time", "N/A"))],
        ["End Time",    str(session.get("end_time",   "N/A"))],
        ["Final Risk Score",     f"{final_risk:.1f} / 100"],
        ["Cheating Probability", f"{final_prob:.1f}%"],
    ]
    table = Table(info_data, colWidths=[5 * cm, 12 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("FONTNAME",   (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE",   (0, 0), (-1, -1), 10),
        ("GRID",       (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING",    (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 1 * cm))

    # Risk Graph
    if os.path.exists(graph_path):
        story.append(Paragraph("Risk Analysis Graph", styles["Heading2"]))
        story.append(Image(graph_path, width=16 * cm, height=7 * cm))
        story.append(Spacer(1, 1 * cm))

    # Event Log
    story.append(Paragraph("Alert Events", styles["Heading2"]))
    if events:
        event_data = [["Time", "Event", "Severity", "Description"]]
        for e in events:
            event_data.append([
                str(e["timestamp"])[:19],
                e["event_type"],
                e["severity"],
                e["description"][:50],
            ])
        etable = Table(event_data, colWidths=[4 * cm, 3.5 * cm, 2.5 * cm, 7 * cm])
        etable.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
            ("FONTNAME",   (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE",   (0, 0), (-1, -1), 8),
            ("GRID",       (0, 0), (-1, -1), 0.3, colors.grey),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.lightyellow]),
            ("PADDING",    (0, 0), (-1, -1), 4),
        ]))
        story.append(etable)
    else:
        story.append(Paragraph("No alert events recorded.", styles["Normal"]))

    # Footer
    story.append(Spacer(1, 1 * cm))
    story.append(HRFlowable(width="100%", thickness=0.5))
    story.append(Paragraph(
        f"Report generated automatically by AI Exam Monitor System.",
        styles["Italic"]
    ))

    doc.build(story)

    # Save report record to DB
    conn = get_connection()
    conn.execute(
        "INSERT INTO reports (session_id, user_id, pdf_path) VALUES (?,?,?)",
        (session_id, user_id, pdf_path)
    )
    conn.commit()
    conn.close()

    print(f"[Report] PDF saved to {pdf_path}")
    return pdf_path
