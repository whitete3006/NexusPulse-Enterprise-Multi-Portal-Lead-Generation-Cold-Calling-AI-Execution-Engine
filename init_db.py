import sqlite3

# This will automatically create the 'nexuspulse.db' file if it doesn't exist
DB_FILE = "nexuspulse.db"

def init_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create all required tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS whatsapp_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient TEXT,
            message TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competitor_intent_signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            competitor_name TEXT,
            intent_signal TEXT,
            signal_score INTEGER,
            detected_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noshow_recovery_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id TEXT,
            phone_number TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Success: 'nexuspulse.db' file and all tables created successfully!")

if __name__ == "__main__":
    init_database()