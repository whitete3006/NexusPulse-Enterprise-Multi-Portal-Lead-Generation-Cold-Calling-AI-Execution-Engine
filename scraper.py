import sqlite3
import datetime

DB_FILE = "nexuspulse.db"

def init_leads_table():
    """Ensures the leads table exists in SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraped_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            contact_name TEXT,
            email TEXT,
            phone_number TEXT,
            source TEXT,
            status TEXT DEFAULT 'new',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def ingest_sample_leads():
    """
    Simulates a multi-portal scrap session (Apollo, LinkedIn SalesNav, Google Maps)
    and populates fresh prospect data directly into SQLite.
    """
    init_leads_table()
    
    # Sample scraped target records (e.g., tech and growth companies)
    new_leads = [
        ("CloudScale Technologies", "Sarah Jenkins", "s.jenkins@cloudscale.io", "+14155550192", "Apollo.io"),
        ("Apex Digital Inc", "Marcus Vance", "marcus@apexdigital.com", "+14155552671", "LinkedIn SalesNav"),
        ("SaaSFlow Global", "Elena Rostova", "elena@saasflow.net", "+14155558833", "Google Maps Sourcing"),
        ("Vanguard Systems", "David Chen", "dchen@vanguardsys.co", "+14155554910", "Apollo.io")
    ]
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    inserted_count = 0
    for company, contact, email, phone, source in new_leads:
        # Check if email already exists to prevent duplicates
        cursor.execute("SELECT id FROM scraped_leads WHERE email = ?", (email,))
        existing = cursor.fetchone()
        
        if not existing:
            cursor.execute(
                """
                INSERT INTO scraped_leads (company_name, contact_name, email, phone_number, source, status)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (company, contact, email, phone, source, "new")
            )
            inserted_count += 1

    conn.commit()
    conn.close()
    
    print(f"[+] Successfully scraped and ingested {inserted_count} new target leads into '{DB_FILE}'.")

if __name__ == "__main__":
    print("--- NexusPulse Multi-Portal Scraper Engine ---")
    ingest_sample_leads()