[
  {
    "scheme_id": "SCH_STARTUP_UP_001",
    "scheme_name": "UP Startup Policy Seed & Prototype Grant",
    "source": "https://startup.up.gov.in",
    "ministry": "Department of IT & Electronics, Government of Uttar Pradesh",
    "government_level": "State",
    "scheme_category": ["Startup", "Innovation", "Entrepreneurship"],
    "target_beneficiary": ["Students", "Entrepreneurs"],
    "eligibility": {
      "structured": {
        "age_min": 18,
        "income_max": null,
        "occupation": ["student", "entrepreneur"],
        "startup_stage": ["idea", "prototype", "early-stage"],
        "state": ["Uttar Pradesh"],
        "gender": ["All"]
      },
      "logic_rules": [
        {"field": "state", "operator": "==", "value": "Uttar Pradesh"}
      ],
      "exceptions": ["Duplicate funding not allowed"]
    },
    "benefits": {
      "type": "Grant",
      "amount": "₹1 lakh",
      "disbursement": "Milestone-based",
      "description": "Funding for prototype development"
    },
    "documents_required": ["Aadhaar Card", "Pitch Deck", "Bank Details"],
    "application": {
      "mode": ["Online"],
      "link": "https://startup.up.gov.in",
      "steps": ["Register", "Apply", "Evaluation", "Funding"]
    },
    "ai_fields": {
      "search_text": "up startup grant prototype",
      "summary": "₹1 lakh prototype funding",
      "keywords": ["startup", "UP"]
    },
    "scoring": {
      "priority_score": 95,
      "popularity_score": 85,
      "relevance_weight": 0.92
    },
    "validity": {
      "active": true,
      "last_verified": "2025-02-15"
    }
  },

  {
    "scheme_id": "SCH_STARTUP_INDIA_002",
    "scheme_name": "Startup India Seed Fund Scheme (SISFS)",
    "source": "https://seedfund.startupindia.gov.in",
    "ministry": "DPIIT",
    "government_level": "Central",
    "scheme_category": ["Startup", "Innovation"],
    "target_beneficiary": ["Startups"],
    "eligibility": {
      "structured": {
        "age_min": 18,
        "income_max": null,
        "occupation": ["entrepreneur"],
        "startup_stage": ["idea", "prototype", "early-stage"],
        "startup_recognition": "DPIIT Registered",
        "state": ["All"],
        "gender": ["All"]
      },
      "logic_rules": [
        {
          "field": "startup_recognition",
          "operator": "==",
          "value": "DPIIT Registered"
        }
      ],
      "exceptions": ["Already funded startups excluded"]
    },
    "benefits": {
      "type": "Grant",
      "amount": "Up to ₹50 lakh",
      "disbursement": "Milestone-based",
      "description": "Funding for prototype and scaling"
    },
    "documents_required": ["Startup Certificate", "Pitch Deck", "Business Plan"],
    "application": {
      "mode": ["Online"],
      "link": "https://seedfund.startupindia.gov.in",
      "steps": ["Register", "Apply", "Evaluation", "Funding"]
    },
    "ai_fields": {
      "search_text": "startup india seed fund",
      "summary": "Up to ₹50 lakh funding",
      "keywords": ["startup", "seed fund"]
    },
    "scoring": {
      "priority_score": 98,
      "popularity_score": 95,
      "relevance_weight": 0.95
    },
    "validity": {
      "active": true,
      "last_verified": "2025-03-01"
    }
  },

  {
    "scheme_id": "SCH_STARTUP_AIM_003",
    "scheme_name": "Atal Innovation Mission",
    "source": "https://aim.gov.in",
    "ministry": "NITI Aayog",
    "government_level": "Central",
    "scheme_category": ["Innovation"],
    "target_beneficiary": ["Students", "Innovators"],
    "eligibility": {
      "structured": {
        "age_min": 15,
        "income_max": null,
        "startup_stage": ["idea", "prototype"],
        "state": ["All"],
        "gender": ["All"]
      },
      "logic_rules": [],
      "exceptions": []
    },
    "benefits": {
      "type": "Grant",
      "amount": "Up to ₹10 lakh",
      "disbursement": "Project-based",
      "description": "Supports innovation and student ideas"
    },
    "documents_required": ["Project Proposal"],
    "application": {
      "mode": ["Online"],
      "link": "https://aim.gov.in",
      "steps": ["Apply", "Evaluation"]
    },
    "ai_fields": {
      "search_text": "atal innovation mission grant",
      "summary": "Innovation funding support",
      "keywords": ["innovation"]
    },
    "scoring": {
      "priority_score": 90,
      "popularity_score": 88,
      "relevance_weight": 0.9
    },
    "validity": {
      "active": true,
      "last_verified": "2025-02-10"
    }
  },

  {
    "scheme_id": "SCH_STARTUP_INDIA_005",
    "scheme_name": "Credit Guarantee Scheme for Startups",
    "source": "https://startupindia.gov.in",
    "ministry": "DPIIT",
    "government_level": "Central",
    "scheme_category": ["Finance", "Loan"],
    "target_beneficiary": ["Startups"],
    "eligibility": {
      "structured": {
        "startup_recognition": "DPIIT Registered"
      },
      "logic_rules": [],
      "exceptions": []
    },
    "benefits": {
      "type": "Loan Guarantee",
      "amount": "Up to ₹10 crore",
      "disbursement": "Bank",
      "description": "Collateral-free loan support"
    },
    "documents_required": ["Business Plan"],
    "application": {
      "mode": ["Bank"],
      "link": "https://startupindia.gov.in",
      "steps": ["Apply loan"]
    },
    "ai_fields": {
      "search_text": "startup loan guarantee india",
      "summary": "Collateral-free loans",
      "keywords": ["loan"]
    },
    "scoring": {
      "priority_score": 92,
      "popularity_score": 87,
      "relevance_weight": 0.91
    },
    "validity": {
      "active": true,
      "last_verified": "2025-03-05"
    }
  }
]