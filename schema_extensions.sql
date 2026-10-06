-- WhatsApp Messages Table
CREATE TABLE whatsapp_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id),
    message_body TEXT NOT NULL,
    direction VARCHAR(20) CHECK (direction IN ('inbound', 'outbound')),
    status VARCHAR(30) DEFAULT 'sent',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Competitor Intent Radar Signals
CREATE TABLE competitor_intent_signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id),
    competitor_name VARCHAR(100) NOT NULL,
    signal_source VARCHAR(50) NOT NULL, -- e.g., 'G2', 'Capterra', 'LinkedIn'
    intent_strength INT CHECK (intent_strength BETWEEN 1 AND 100),
    detected_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Email Warmup & SMTP Pool Table
CREATE TABLE smtp_inboxes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    domain_name VARCHAR(150) NOT NULL,
    smtp_user VARCHAR(255) NOT NULL,
    warmup_status VARCHAR(30) DEFAULT 'warming',
    reputation_score INT DEFAULT 100,
    daily_limit INT DEFAULT 100,
    sent_today INT DEFAULT 0
);

-- Meeting No-Show Recovery Log
CREATE TABLE noshow_recovery_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id),
    recovery_channel VARCHAR(30) CHECK (recovery_channel IN ('sms', 'ai_voice', 'whatsapp')),
    status VARCHAR(30) DEFAULT 'triggered',
    rescheduled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Revenue Attribution Table
CREATE TABLE revenue_attribution (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    deal_id UUID REFERENCES leads(id),
    sourcing_channel VARCHAR(50) NOT NULL,
    email_subject_used VARCHAR(255),
    cold_call_script_used VARCHAR(100),
    closed_revenue DECIMAL(12, 2) NOT NULL,
    closed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);