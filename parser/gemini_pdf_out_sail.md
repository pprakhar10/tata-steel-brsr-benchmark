{
  "companyId": "sail",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "TotalElectricityConsumption": {
      "pdfValue": "1,40,372.3",
      "pdfUnit": "TJ (Terajoules)",
      "action": "CONFIRM",
      "note": "Matches XBRL (140,372,300 GJ = 140,372.3 TJ)."
    },
    "Sox": {
      "pdfValue": "3 to 76",
      "pdfUnit": "mg/Nm³",
      "action": "CORRECT",
      "note": "XBRL range is correct, but unit is mg/Nm³ (mass concentration) as per standard air quality reporting for stack emissions."
    },
    "Nox": {
      "pdfValue": "3 to 87",
      "pdfUnit": "mg/Nm³",
      "action": "CORRECT",
      "note": "Matches range in XBRL; unit is mg/Nm³."
    },
    "ParticulateMatter": {
      "pdfValue": "31 to 99",
      "pdfUnit": "mg/Nm³",
      "action": "CORRECT",
      "note": "Matches range in XBRL; unit is mg/Nm³."
    },
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "5.33",
      "pdfUnit": "KL / Rs. Crore",
      "action": "CORRECT",
      "note": "PDF reports 5.33 KL per Crore of turnover. XBRL value of 0.05 is likely a unit-scaling difference (e.g., KL per Lakh)."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Eco-restoration of mined-out areas and waste dumps at Meghahatuburu Iron Ore Mines",
        "metric": "Area restored",
        "baseline": "New nursery established",
        "targetValue": "30,000 seedlings raised",
        "timeline": "2025-26"
      }
    ],
    "initiatives": [
      {
        "name": "SAIL Sarathi",
        "area": "governance",
        "description": "AI-based Chatbot launched on the website to enhance customer engagement and service.",
        "outcome": "One of the most advanced bots in the steel industry."
      },
      {
        "name": "Zero Liquid Discharge (ZLD)",
        "area": "water",
        "description": "Implementation of ZLD projects across Integrated Steel Plants including ISP, DSP, and RSP.",
        "outcome": "Pioneering projects towards 100% water recycling."
      },
      {
        "name": "CO2 Capture & Mineralization",
        "area": "emissions",
        "description": "R&D project with IIT Bombay for sustainable, low-energy consuming technology.",
        "outcome": "Part of decarbonization effort."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": null,
      "categories": [],
      "note": "The report mentions starting a study to prepare a comprehensive GHG inventory including Scope 3."
    },
    "managementCommentary": "We had made a decision to work on focus areas: to maximize capacity utilization and provide the best value to customers. Strategic interventions were made in ramping up production and focusing on Decarbonisation and Sustainability. We achieved record Crude Steel capacity utilization of about 94%. We continue to engage with stakeholders and proactively stay ahead of the curve.",
    "awardsAndRatings": [
      { "name": "Greentech Environment Award", "score": "Winner", "year": "2022" },
      { "name": "National Energy Conservation Award", "score": "1st Prize (RSP)", "year": "2022" }
    ],
    "nonCompliance": [
      { "description": "Non-compliance of environmental standards at IISCO Steel Plant (ISP).", "resolution": "Direction issued by WBPCB; corrective measures implemented with a time-bound action plan." }
    ],
    "forwardLooking": [
      { "description": "Expansion of Capacity and Intensifying Digitisation", "timeline": "Next decade" },
      { "description": "Green fuel adoption and decarbonisation efforts", "timeline": "Upcoming years" }
    ],
    "qualitativePolicies": {
      "P1_ethics": "Upholds highest ethical standards in business conduct through transparency and accountability.",
      "P3_ohs": "ISO 45001 certified; Hazard Identification and Risk Assessment (HIRA) conducted for most activities.",
      "P6_environment": "Corporate Environmental Policy emphasizes going beyond compliance to preserve ecological balance."
    },
    "steelProduction": {
      "value": "18,289,000",
      "unit": "metric tonnes",
      "note": "Reported as 18.289 MT Crude Steel production."
    },
    "reportingBoundary": "Standalone"
  }
}
{
  "companyId": "sail",
  "year": "FY2024",
  "source": "PDF",
  "xbrlPatches": {
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput_FY2024": {
      "pdfValue": "2.8",
      "pdfUnit": "tCO2e/tcs",
      "action": "FOUND",
      "note": "XBRL reports 0; PDF confirms 2.8 tonnes of CO2 equivalent per tonne of crude steel."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "5.49",
      "pdfUnit": "KL / Rs. Crore",
      "action": "FOUND",
      "note": "XBRL shows 52.33; PDF confirms 5.49 KL per Crore. The jump in XBRL is a denominator error."
    },
    "Sox_FY2024": {
      "pdfValue": "0.53",
      "pdfUnit": "kg/tcs",
      "action": "FOUND",
      "note": "Reported as mass intensity per tonne of crude steel."
    },
    "Nox_FY2024": {
      "pdfValue": "0.55",
      "pdfUnit": "kg/tcs",
      "action": "FOUND",
      "note": "Reported as mass intensity per tonne of crude steel."
    },
    "ParticulateMatter": {
      "pdfValue": "0.58",
      "pdfUnit": "kg/tcs",
      "action": "CONFIRM",
      "note": "Matches XBRL value of 0.58; unit is kg/tcs."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Achieve Zero Liquid Discharge across all SAIL plants",
        "metric": "Water Recycling %",
        "baseline": null,
        "targetValue": "100%",
        "timeline": "Continuous"
      }
    ],
    "initiatives": [
      {
        "name": "SAIL Green Tiles Plant",
        "area": "waste",
        "description": "Utilization of slag for manufacturing green tiles at Bhilai.",
        "outcome": "Utilized 5.3 MT of slag."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": null,
      "categories": [],
      "note": "Scope 3 emission is partially covered and identification is ongoing."
    },
    "managementCommentary": "Focused on smart steel and sustainable growth. The reporting boundary excludes subsidiaries and focuses on integrated and special steel plants on a standalone basis.",
    "awardsAndRatings": [
      { "name": "Productivity Excellence Award", "score": "5 Star Rating", "year": "2023" }
    ],
    "nonCompliance": [
      { "description": "Specific environmental non-compliances mentioned for integrated plants.", "resolution": "Corrective actions underway via revamped pollution control equipment." }
    ],
    "forwardLooking": [
      { "description": "Expansion of renewable energy footprint and decarbonization.", "timeline": "Next 3 years" }
    ],
    "qualitativePolicies": {
      "P1_ethics": "Policies cover NGRBC principles; ethics monitored by Board.",
      "P3_ohs": "100% of plants and offices assessed for health and safety practices.",
      "P6_environment": "Dedicated environmental management division oversees restoration and treatment."
    },
    "steelProduction": {
      "value": "19,667,396",
      "unit": "metric tonnes",
      "note": "Derived from total emissions (55.07M tCO2e) and intensity (2.8 tCO2e/tcs)."
    },
    "reportingBoundary": "Standalone"
  }
}
{
  "companyId": "sail",
  "year": "FY2025",
  "source": "PDF",
  "xbrlPatches": {
    "TotalVolumeOfWaterWithdrawal_FY2025": {
      "pdfValue": "12,95,77,216",
      "pdfUnit": "kL",
      "action": "CONFIRM",
      "note": "Genuine doubling confirmed. Increase is due to expanded operations and inclusion of new reporting units."
    },
    "Sox_FY2025": {
      "pdfValue": "0.61",
      "pdfUnit": "kg/tcs",
      "action": "FOUND",
      "note": "Reported as mass intensity."
    },
    "Nox_FY2025": {
      "pdfValue": "0.61",
      "pdfUnit": "kg/tcs",
      "action": "FOUND",
      "note": "Reported as mass intensity."
    },
    "TotalScope2Emissions": {
      "pdfValue": "47,96,073",
      "pdfUnit": "tCO2e",
      "action": "CONFIRM",
      "note": "Genuine increase due to arrangements for green power import from grid (DVC) at DSP and ISP."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Reduction of Specific Particulate Matter (PM) Emission Load",
        "metric": "kg/tcs",
        "baseline": "0.58 in FY24",
        "targetValue": "0.56 achieved",
        "timeline": "FY 2024-25"
      }
    ],
    "initiatives": [
      {
        "name": "Green Power Import",
        "area": "energy",
        "description": "Arrangement for green power import from DVC at Durgapur and IISCO plants.",
        "outcome": "Significant increase in renewable energy TJ (from 266 to 1400 TJ)."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": null,
      "categories": [],
      "note": "The entity is in the process of identifying all relevant Scope 3 categories."
    },
    "managementCommentary": "Reduced emissions align with global climate goals and enhance SAIL's competitiveness in green steel markets. Sustainability leads to carbon credits and green bond opportunities.",
    "awardsAndRatings": [],
    "nonCompliance": [
      { "description": "Bhilai Steel Plant: Inefficient operation of Sewage Treatment Plant (STP) in violation of Water Act 1974.", "resolution": "Direction issued by CECB; corrective actions being taken." }
    ],
    "forwardLooking": [
      { "description": "Implementation of Solid State Interlocking (SSI) and automation up-gradation.", "timeline": "2025-26" }
    ],
    "qualitativePolicies": {
      "P1_ethics": "Anti-corruption and ethics policies covered under NGRBC framework.",
      "P3_ohs": "Occupational Health & Safety is critical for maintaining uninterrupted operations.",
      "P6_environment": "Action plan in place for PM reduction and ZLD implementation."
    },
    "steelProduction": {
      "value": "18,928,478",
      "unit": "metric tonnes",
      "note": "Derived from total emissions (56.97M tCO2e) and intensity (3.01 tCO2e/tcs)."
    },
    "reportingBoundary": "Standalone"
  }
}