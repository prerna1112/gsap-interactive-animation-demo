from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pathlib import Path

OUT = Path(__file__).parent.parent.parent / "output" / "pdf" / "signal-motion-gsap-case-study.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

INK = HexColor('#15121b'); PAPER = HexColor('#f5f2ed'); VIOLET = HexColor('#6d43d8'); VIOLET_DARK = HexColor('#362065'); LIME = HexColor('#c7ff4a'); MUTED = HexColor('#716b78')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
    def draw_page_number(self, page_count):
        self.setFillColor(MUTED); self.setFont('Helvetica', 8)
        self.drawRightString(7.75*inch, .38*inch, f"SIGNAL MOTION  /  {self._pageNumber} OF {page_count}")

def draw_mockup(c, doc):
    x, y, w, h = 4.7*inch, .35*inch, 2.85*inch, 1.8*inch
    c.saveState(); c.setFillColor(VIOLET_DARK); c.roundRect(x, y, w, h, 6, fill=1, stroke=0)
    c.setFillColor(HexColor('#cfc4ec')); c.setFont('Helvetica', 6.5); c.drawString(x+14, y+h-19, 'LIVE SIGNAL')
    c.setFillColor(LIME); c.drawRightString(x+w-14, y+h-19, '+18.2%')
    c.setStrokeColor(HexColor('#7665a0')); c.setLineWidth(.5)
    for i in range(1,5): c.line(x+14, y+35+i*31, x+w-14, y+35+i*31)
    pts=[(x+14,y+43),(x+56,y+69),(x+97,y+61),(x+143,y+101),(x+185,y+88),(x+232,y+133),(x+w-14,y+166)]
    c.setStrokeColor(LIME); c.setLineWidth(2); p=c.beginPath(); p.moveTo(*pts[0])
    for px,py in pts[1:]: p.lineTo(px,py)
    c.drawPath(p); c.setFillColor(LIME)
    for px,py in pts: c.circle(px,py,2.3,fill=1,stroke=0)
    c.restoreState()

def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=.62*inch, leftMargin=.62*inch, topMargin=.58*inch, bottomMargin=.58*inch)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Eyebrow', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=VIOLET, spaceAfter=8, tracking=1.1))
    styles.add(ParagraphStyle(name='TitleX', fontName='Helvetica-Bold', fontSize=28, leading=28, textColor=INK, spaceAfter=10))
    styles.add(ParagraphStyle(name='Deck', fontName='Helvetica', fontSize=10.5, leading=15, textColor=MUTED, spaceAfter=8))
    styles.add(ParagraphStyle(name='H2X', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=INK, spaceBefore=12, spaceAfter=6))
    styles.add(ParagraphStyle(name='BodyX', fontName='Helvetica', fontSize=8.8, leading=12, textColor=INK, spaceAfter=4))
    styles.add(ParagraphStyle(name='SmallX', fontName='Helvetica', fontSize=7.7, leading=10, textColor=MUTED))
    styles.add(ParagraphStyle(name='CodeX', fontName='Courier', fontSize=7, leading=9, textColor=VIOLET_DARK))
    story=[]
    story += [Paragraph('GSAP + SCROLLTRIGGER / CAPABILITY DEMO', styles['Eyebrow']), Paragraph('Signal Motion', styles['TitleX']), Paragraph('A focused, responsive scroll narrative for dashboard and product-interface work.', styles['Deck'])]
    meta = [[Paragraph('<b>Live demo</b><br/>gsap-interactive-animation-demo.vercel.app', styles['SmallX']), Paragraph('<b>Repository</b><br/>github.com/prerna1112/gsap-interactive-animation-demo', styles['SmallX']), Paragraph('<b>Stack</b><br/>HTML / CSS / GSAP 3.12.5', styles['SmallX'])]]
    t=Table(meta, colWidths=[2.2*inch,2.65*inch,1.9*inch]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#ece8e2')),('BOX',(0,0),(-1,-1),.5,HexColor('#d9d3ca')),('INNERGRID',(0,0),(-1,-1),.5,HexColor('#d9d3ca')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)])); story += [t, Spacer(1,10)]
    story += [Paragraph('The brief', styles['H2X']), Paragraph('This prototype demonstrates the riskiest part of a small GSAP starter task: a polished sequence that responds to scrolling, stays responsive, and remains maintainable. It uses dummy analytics values only and is intentionally bounded to one reusable interaction story.', styles['BodyX'])]
    story += [Spacer(1,2), Paragraph('What is working', styles['H2X'])]
    bullets=['ScrollTrigger progress rail, one-time reveals, and hero parallax.','SVG chart line/area drawing with staggered data points.','Animated metric counters and progress bars.','Responsive layout and reduced-motion fallback.','Pulse control with immediate feedback and no backend dependency.']
    bullet_rows=[[Paragraph('• '+b, styles['BodyX'])] for b in bullets]
    bt=Table(bullet_rows, colWidths=[3.45*inch]); bt.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)])); story.append(bt)
    story += [Paragraph('Implementation notes', styles['H2X']), Paragraph('Animation orchestration lives in <font name="Courier">app.js</font>; layout and visual states remain in <font name="Courier">styles.css</font>. Only transform and opacity are animated for the main reveals. The CDN dependency is documented as a deliberate demo trade-off; a production handoff can bundle and pin GSAP through the client build system.', styles['BodyX'])]
    story += [Paragraph('Verification', styles['H2X']), Paragraph('<b>Automated:</b> 3 Node tests pass for asset loading, plugin registration, reduced-motion guard, viewport metadata, and the accessible button. <b>Browser:</b> live URL returns HTTP 200; scroll state verified at page end (counters 98 / 184 / 12, chart line revealed); pulse action verified with status feedback.', styles['BodyX'])]
    story += [Spacer(1,7), Paragraph('Honest context', styles['Eyebrow']), Paragraph('New application-specific prototype — not represented as previous paid client work.', styles['SmallX'])]
    def on_page(c, d):
        c.setFillColor(PAPER); c.rect(0,0,letter[0],letter[1],fill=1,stroke=0)
        c.setFillColor(LIME); c.rect(0, letter[1]-.12*inch, letter[0], .12*inch, fill=1, stroke=0)
        draw_mockup(c,d)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page, canvasmaker=NumberedCanvas)
    print(OUT)

if __name__=='__main__': build()
