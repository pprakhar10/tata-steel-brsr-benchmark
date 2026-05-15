{
  "companyId": "jindal-stainless",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "335",
      "pdfUnit": "kilolitres / Crore INR",
      "action": "CONFIRM",
      "note": "XBRL shows 335. The PDF confirms the value is 335, but the denominator is per Crore INR (calculated as 11,681,607 kL / 34,849 Crore turnover), not per single rupee."
    },
    "Sox": {
      "pdfValue": "851.89",
      "pdfUnit": "MT",
      "action": "CONFIRM",
      "note": "Raw XBRL of 851.89 matches the PDF value. Unit in PDF is Metric Tonnes (MT)."
    },
    "Nox": {
      "pdfValue": "1980.68",
      "pdfUnit": "MT",
      "action": "CONFIRM",
      "note": "Matches XBRL raw value."
    },
    "ParticulateMatter": {
      "pdfValue": "2084.13",
      "pdfUnit": "MT",
      "action": "CONFIRM",
      "note": "Matches XBRL raw value."
    },
    "Sox_FY2024": {
      "pdfValue": "3072.064",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Value extracted from FY2024 PDF for cross-verification."
    },
    "Nox_FY2024": {
      "pdfValue": "1782.58",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Value extracted from FY2024 PDF for cross-verification."
    },
    "Sox_FY2025": {
      "pdfValue": "4580.69",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Value extracted from FY2025 PDF for cross-verification."
    },
    "Nox_FY2025": {
      "pdfValue": "2527.48",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Value extracted from FY2025 PDF for cross-verification."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "333.0085",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "FY2024 denominator remains per Crore INR, matching the XBRL value of ~333."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2025": {
      "pdfValue": "358.67",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "The FY2025 PDF shows 358.67 KL/Crore INR. The XBRL value of 0.0000359 is 358.67 divided by 10,000,000, showing the filer corrected the unit to 'per single rupee' in FY2025."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Net Zero carbon emission target",
        "metric": "GHG Emissions",
        "baseline": "None stated",
        "targetValue": "Net Zero",
        "timeline": "2050"
      },
      {
        "description": "Reduce carbon emission intensity",
        "metric": "Carbon emission intensity (tCO2e/tcs)",
        "baseline": "FY 2022 (1.91 tonnes CO2/tonnes of crude steel)",
        "targetValue": "50% reduction",
        "timeline": "2035"
      }
    ],
    "initiatives": [
      {
        "name": "Oxygen Enrichment",
        "area": "energy",
        "description": "Enrichment of oxygen in walking beam furnace to reduce the consumption of Propane/LSHS",
        "outcome": "Fuel saving by 3%"
      },
      {
        "name": "Water Fixture Replacement",
        "area": "water",
        "description": "Replaced 25 taps with efficient water fixtures (Dual Mist Foam water nozzle)",
        "outcome": "2 m3/day fresh water saved"
      },
      {
        "name": "Floor Cleaning Water Replacement",
        "area": "water",
        "description": "Cleaning of floors done by waste water and water tankers instead of soft water",
        "outcome": "50 m3/day fresh water saved"
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "2781561 MTCO2e",
      "categories": [],
      "note": "FY2023 value sourced from the comparative column in the FY2024 PDF report."
    },
    "managementCommentary": "The Company is unwavering in its dedication to creating a greener, more sustainable future, driven by a strong sense of environmental responsibility. As part of its commitment, the company has adopted an eco-conscious approach in manufacturing stainless steel. This involves utilizing scrap in an electric arc furnace, which stands as the most ecofriendly method with minimal greenhouse gas emissions. By embracing this approach, the company ensures 100% recyclability without compromising on the quality of its products, thus fostering a circular economy.",
    "awardsAndRatings": [
      {
        "name": "ISO 9001, ISO 14001, ISO 45001, ISO 50001",
        "score": null,
        "year": "2023"
      }
    ],
    "nonCompliance": [
      {
        "description": "No instances of regulatory penalties, environmental non-compliance, or fines reported in the financial year.",
        "resolution": "Nil"
      }
    ],
    "forwardLooking": [
      {
        "description": "Achieve Net Zero carbon emissions.",
        "timeline": "2050"
      },
      {
        "description": "Evaluate realistic targets for reducing waste landfilled to minimize environmental impact.",
        "timeline": "Next 1-3 years"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "The Company has an Anti-corruption and Anti-bribery policy demonstrating zero tolerance towards bribery and corrupt practices. It manages conflict of interest through annual declarations from the Board and employees.",
      "P3_ohs": "The Company implements ISO 45001:2018 for Occupational Health & Safety and adopts a 4-E principle (Engineering Control, Education, Encouragement & Enforcement) to promote an ACCIDENT-FREE STEEL culture.",
      "P6_environment": "Focuses on utilizing scrap in an electric arc furnace (EAF) to minimize GHG emissions. The company is evaluating biodiversity risk, planting native species, and ensuring Zero Liquid Discharge across facilities."
    },
    "steelProduction": {
      "value": "1581130",
      "unit": "metric tonnes",
      "note": "Derived from Total Scope 1 & 2 Emissions (3,320,373 TCO2E) divided by reported emission intensity (2.10 TCO2E/tcs)."
    },
    "reportingBoundary": "Standalone"
  }
}
{
  "companyId": "jindal-stainless",
  "year": "FY2024",
  "source": "PDF",
  "xbrlPatches": {
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "333.0085",
      "pdfUnit": "KL / Crore INR",
      "action": "CONFIRM",
      "note": "XBRL value 333 matches the PDF value. The unit is explicitly per Crore INR, not per single rupee."
    },
    "Sox": {
      "pdfValue": "3072.064",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "SOx emissions for FY2024 were missing in XBRL but successfully extracted from the PDF."
    },
    "Nox": {
      "pdfValue": "1782.58",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "NOx emissions for FY2024 were missing in XBRL but successfully extracted from the PDF."
    },
    "ParticulateMatter": {
      "pdfValue": "1313.271",
      "pdfUnit": "MT",
      "action": "CONFIRM",
      "note": "Matches XBRL raw value."
    },
    "Sox_FY2024": {
      "pdfValue": "3072.064",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Self-reference check."
    },
    "Nox_FY2024": {
      "pdfValue": "1782.58",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Self-reference check."
    },
    "Sox_FY2025": {
      "pdfValue": "4580.69",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Cross-verification value from FY2025 PDF."
    },
    "Nox_FY2025": {
      "pdfValue": "2527.48",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Cross-verification value from FY2025 PDF."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "333.0085",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "Self-reference check."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2025": {
      "pdfValue": "358.67",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "Cross-verification value from FY2025 PDF."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Achieve Net Zero emissions",
        "metric": "GHG Emissions",
        "baseline": "None stated",
        "targetValue": "Net Zero",
        "timeline": "2050"
      },
      {
        "description": "Reduce emission intensity by 50%",
        "metric": "Emission Intensity",
        "baseline": "FY 2022",
        "targetValue": "50% reduction",
        "timeline": "Not explicitly stated for the 50% (implied medium-term)"
      }
    ],
    "initiatives": [
      {
        "name": "Floating & Rooftop Solar",
        "area": "energy",
        "description": "7.3 MWp floating solar installed and 23 MWp rooftop solar under commission in Jajpur.",
        "outcome": "Generated 61,55,850 Kwh energy from onsite solar generation."
      },
      {
        "name": "Chrome Palletization Plant",
        "area": "emissions",
        "description": "Installed a state-of-the-art chrome palletization plant instead of traditional briquetting, leading to lower specific energy consumption.",
        "outcome": "Reduction in overall emission."
      },
      {
        "name": "Waste Heat Recovery Boiler (WHRB)",
        "area": "energy",
        "description": "Capturing and utilizing waste heat generated during steelmaking processes to generate steam.",
        "outcome": "Abated 298.8 tonnes of propane equivalent."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "3345443 MTCO2e",
      "categories": [],
      "note": "Scope 3 emission intensity is 1.90 MTCO2e / production (TCS)."
    },
    "managementCommentary": "The Company is unwavering in its dedication to creating a sustainable future, driven by a strong sense of environmental, social and governance responsibility. As part of its commitment, the company has adopted an eco-conscious approach in manufacturing stainless steel. This involves utilizing scrap in an electric arc furnace, which stands as the most eco-friendly method with minimal greenhouse gas emissions. The company's management is currently evaluating realistic targets for reducing waste landfilled to minimize its environmental impact in the future.",
    "awardsAndRatings": [
      {
        "name": "Responsible Steel certification (In Progress)",
        "score": null,
        "year": "2024"
      }
    ],
    "nonCompliance": [
      {
        "description": "No fines, penalties, or non-compliances reported for the year.",
        "resolution": "Nil"
      }
    ],
    "forwardLooking": [
      {
        "description": "Develop science-based targets for near-term and Net Zero GHG emissions in the long-term through the Science Based Targets initiative (SBTi).",
        "timeline": "Long-term (2050)"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "The Anti-Bribery and Anti-Corruption (ABAC) Policy ensures operations align with the highest ethical standards to prevent fraud, bribery, and corruption.",
      "P3_ohs": "Driven by a 'No Harm' philosophy, the Company implemented ISO 45001:2018. The safety culture relies on Engineering Control, Education, Encouragement, and Enforcement.",
      "P6_environment": "Operations center around the principles of Reduce, Reuse, Recycle, Recover, and Repurpose. Approximately 72% of input material consists of recycled scrap and revert."
    },
    "steelProduction": {
      "value": "1759531",
      "unit": "metric tonnes",
      "note": "Derived from Total Scope 1 & 2 Emissions (3,779,474.08 TCO2e) divided by emission intensity (2.1480 TCO2e/TCS)."
    },
    "reportingBoundary": "Standalone"
  }
}
{
  "companyId": "jindal-stainless",
  "year": "FY2025",
  "source": "PDF",
  "xbrlPatches": {
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "358.67",
      "pdfUnit": "KL / Crore INR",
      "action": "CORRECT",
      "note": "The XBRL value is 0.0000359, which is 358.67 / 10,000,000. The filer mathematically normalized the PDF value of 358.67 KL/Crore INR to 'per single rupee' in FY2025."
    },
    "Sox": {
      "pdfValue": "4580.69",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "SOx missing from XBRL; value successfully extracted from FY2025 PDF."
    },
    "Nox": {
      "pdfValue": "2527.48",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "NOx missing from XBRL; value successfully extracted from FY2025 PDF."
    },
    "ParticulateMatter": {
      "pdfValue": "1601.47",
      "pdfUnit": "MT",
      "action": "CONFIRM",
      "note": "Matches XBRL raw value."
    },
    "Sox_FY2024": {
      "pdfValue": "3072.064",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Cross-verification value from FY2024 PDF."
    },
    "Nox_FY2024": {
      "pdfValue": "1782.58",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Cross-verification value from FY2024 PDF."
    },
    "Sox_FY2025": {
      "pdfValue": "4580.69",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Self-reference check."
    },
    "Nox_FY2025": {
      "pdfValue": "2527.48",
      "pdfUnit": "MT",
      "action": "FOUND",
      "note": "Self-reference check."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "333.0085",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "Cross-verification value from FY2024 PDF."
    },
    "WaterIntensityPerRupeeOfTurnover_FY2025": {
      "pdfValue": "358.67",
      "pdfUnit": "KL / Crore INR",
      "action": "FOUND",
      "note": "Self-reference check."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Carbon emission intensity reduction",
        "metric": "Emission Intensity",
        "baseline": "FY 2022",
        "targetValue": "50% reduction",
        "timeline": "2035"
      },
      {
        "description": "Zero-Waste-to-Landfill certification",
        "metric": "Waste to landfill",
        "baseline": "None stated",
        "targetValue": "Zero",
        "timeline": "2030"
      },
      {
        "description": "Diversity and inclusion target",
        "metric": "Female workforce representation",
        "baseline": "None stated",
        "targetValue": "8%",
        "timeline": "2030"
      }
    ],
    "initiatives": [
      {
        "name": "Smart cooling control based on electrode temperature",
        "area": "energy",
        "description": "Reduced blower runtime by 4.28 hours per day without adverse impact on operations by modifying control logic.",
        "outcome": "Saved 1.66 lakh units of electricity annually (INR 10.8 lakhs)."
      },
      {
        "name": "Optimum use of chemicals, water and energy at the CPP-DM plant",
        "area": "water",
        "description": "Replaced faulty ejectors, rotameters, and valves to improve flow; optimized downflow rates and degasser levels.",
        "outcome": "12% reduction in HCl, 15% reduction in NaOH; raw water dropped by 420 m3/year."
      },
      {
        "name": "Cost saving from boiler waste water",
        "area": "water",
        "description": "Created a settling tank and extended a pipeline to the cooling tower basin to reuse DM water discharged during boiler hydro-tests.",
        "outcome": "Saved 2532 m3 of water annually."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "3216693 Metric tonnes of CO2 equivalent",
      "categories": [],
      "note": "Intensity is 1.64 MTCO2e/production (TCS). Marks a reduction from FY2024."
    },
    "managementCommentary": "JSL remains steadfast in its commitment to building a greener and more sustainable future, guided by a deep sense of environmental responsibility. Embracing an eco-conscious manufacturing approach, the company uses scrap-based production through electric arc furnaces - one of the most environmental friendly methods with low greenhouse gas emissions. To further its circular economy vision, the company promotes waste-to-value creation and a closed-loop recycling system.",
    "awardsAndRatings": [
      {
        "name": "LEED v4.1 O+M: Platinum level (Stainless Centre - Gurgaon) & Gold level (JSL Jajpur clubhouse)",
        "score": "Platinum / Gold",
        "year": "2025"
      }
    ],
    "nonCompliance": [
      {
        "description": "Zero cases of human rights violations and zero cybersecurity breaches reported.",
        "resolution": "Nil"
      }
    ],
    "forwardLooking": [
      {
        "description": "Develop science-based targets for Nature (SBTn).",
        "timeline": "Not explicitly stated"
      },
      {
        "description": "Assess 100% of suppliers on ESG criteria.",
        "timeline": "Ongoing"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "The Company implements an Anti-Bribery & Anti-Corruption Policy and a rigorous Supplier Code of Conduct, evaluating partners across all 9 BRSR principles.",
      "P3_ohs": "Driven by an Occupational Health and Safety Policy under ISO 45001:2018. Achieved an LTIFR of 0 for employees and contractors in FY25.",
      "P6_environment": "Supported by Climate Change, Water Management, and Biodiversity policies. Implements Zero Liquid Discharge (ZLD) mechanisms and sources 72.11% recycled scrap for production."
    },
    "steelProduction": {
      "value": "1955842",
      "unit": "metric tonnes",
      "note": "Derived from Total Scope 1 & 2 Emissions (3,618,309 TCO2e) divided by emission intensity (1.85 TCO2e/TCS)."
    },
    "reportingBoundary": "Standalone"
  }
}