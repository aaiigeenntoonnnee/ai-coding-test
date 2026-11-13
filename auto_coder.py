import subprocess

# 1. รับคำสั่งจากผู้ใช้ (โหมดจำลอง AI เพื่อทดสอบระบบ Human-in-the-Loop และ GitHub)
filename = "result.html"
prompt = input(f"อยากให้ AI เขียนโค้ดอะไรลงใน {filename}: ")

print("\nกำลังจำลองการสร้างโค้ด HTML...")

# 2. สร้างโค้ด HTML ตัวอย่างตามคำสั่ง
code = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ทดสอบระบบ AI + GitHub</title>
    <style>
        body {{ font-family: sans-serif; background-color: #e0f2fe; text-align: center; padding-top: 80px; }}
        .card {{ background: white; max-width: 400px; margin: auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
        button {{ background-color: #0284c7; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-size: 16px; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>ผลงานจากคำสั่ง: {prompt}</h2>
        <p>สร้างไฟล์สำเร็จและผ่านการตรวจสอบจากมนุษย์แล้ว</p>
        <button onclick="alert('สวัสดี! ระบบ Human-in-the-Loop ทำงานสมบูรณ์')">กดทักทาย</button>
    </div>
</body>
</html>"""

# 3. บันทึกโค้ดลงไฟล์บนเครื่อง
with open(filename, "w", encoding="utf-8") as f:
    f.write(code)

print(f"\nสร้างไฟล์ '{filename}' เรียบร้อยแล้ว!")
print("👉 กรุณาเปิดไฟล์ดังกล่าวขึ้นมาตรวจสอบความถูกต้องก่อนยืนยัน")

# 4. หยุดรอการตรวจสอบจากมนุษย์ (Human-in-the-Loop)
confirm = input("\nกดยืนยันความถูกต้อง (Y/N): ").strip().upper()

if confirm == "Y":
    print("\nกำลังอัปโหลดขึ้น GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Add {filename} via Human-in-the-Loop"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ อัปโหลดขึ้น GitHub สำเร็จเรียบร้อย!")
    except subprocess.CalledProcessError as e:
        print(f"❌ เกิดข้อผิดพลาดในการส่งขึ้น GitHub: {e}")
else:
    print("\nยกเลิกการอัปโหลด (ไฟล์ยังคงอยู่ในเครื่องของคุณ แต่ยังไม่ถูกส่งขึ้น GitHub)")