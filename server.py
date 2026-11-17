
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os
import requests

app = FastAPI(title="Xióngmāo Investment Portfolio API")

# Database initialization
DB_FILE = "investors.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS investors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            whatsapp_number TEXT NOT NULL,
            momo_number TEXT NOT NULL,
            momo_name TEXT NOT NULL,
            investment_amount REAL NOT NULL,
            schedule_type TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class InvestorRegistration(BaseModel):
    full_name: str
    whatsapp_number: str
    momo_number: str
    momo_name: str
    investment_amount: float
    schedule_type: str

@app.get("/", response_class=HTMLResponse)
async def read_index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Xióngmāo Investment Portfolio</h1><p>Frontend template not found. Please place index.html in the root directory.</p>"

@app.post("/api/register")
async def register_investor(data: InvestorRegistration):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO investors (full_name, whatsapp_number, momo_number, momo_name, investment_amount, schedule_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data.full_name, data.whatsapp_number, data.momo_number, data.momo_name, data.investment_amount, data.schedule_type))
        conn.commit()
        investor_id = cursor.lastrowid
        conn.close()
        
        return {"status": "success", "message": "Registration received successfully", "investor_id": investor_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/investors")
async def get_investors():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM investors ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
