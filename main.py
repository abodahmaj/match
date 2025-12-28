from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from weasyprint import HTML

app = FastAPI(title="نظام الكنترول المدرسي")

@app.get("/")
def home():
    return {
        "message": "النظام يعمل بنجاح",
        "note": "نسخة تجريبية"
    }

@app.get("/web", response_class=HTMLResponse)
def web_app():
    return """
    <html dir="rtl">
    <head>
      <meta charset="UTF-8">
      <title>نظام الكنترول المدرسي</title>
    </head>
    <body style="font-family:Tahoma;text-align:center">
      <h2>نظام الكنترول المدرسي</h2>
      <p>تطبيق ويب تجريبي</p>
      <a href="/kashf">🧾 توليد كشف مناداة</a>
    </body>
    </html>
    """

@app.get("/kashf")
def kashf():
    html = """
    <html dir="rtl">
    <body style="font-family:Amiri">
    <h2 style="text-align:center">كشف مناداة</h2>
    <table border="1" width="100%">
    <tr><th>الاسم</th><th>رقم الجلوس</th></tr>
    <tr><td>محمد أحمد</td><td>12</td></tr>
    </table>
    </body>
    </html>
    """
    HTML(string=html).write_pdf("kashf.pdf")
    return {"pdf": "تم إنشاء كشف مناداة"}
