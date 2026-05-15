{
  "companyId": "tata-steel",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput": {
      "pdfValue": null,
      "pdfUnit": null,
      "action": "NOT_FOUND",
      "note": "PDF refers to the ESG factsheet for physical intensity and does not state the value in the BRSR table. The '61' in XBRL is likely an error."
    },
    "TotalElectricityConsumption": {
      "pdfValue": "67",
      "pdfUnit": "Peta Joule",
      "action": "CONFIRM",
      "note": "PDF reports 67 Peta Joule, which equals 67,000,000 GJ."
    },
    "TotalEnergyConsumedFromRenewableAndNonRenewableSources": {
      "pdfValue": "857",
      "pdfUnit": "Peta Joule",
      "action": "CONFIRM",
      "note": "PDF reports 857 Peta Joule."
    },
    "TotalVolumeOfWaterWithdrawal": {
      "pdfValue": "201",
      "pdfUnit": "Million Kilolitres",
      "action": "CORRECT",
      "note": "PDF provides a split by entity (Tata Steel India 96, TSN 72, TSUK 31, TSTH & TSMC 2) which sums to 201 Million Kilolitres."
    },
    "WaterWithdrawalByGroundwater": {
      "pdfValue": "17",
      "pdfUnit": "Million Kilolitres",
      "action": "CORRECT",
      "note": "PDF provides a split by entity (Tata Steel India 2, TSN 15, TSUK 0, TSTH 0) summing to 17 Million Kilolitres."
    },
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "0.07",
      "pdfUnit": "litres per rupee of turnover",
      "action": "CORRECT",
      "note": "PDF reports intensity separately for different entities (India 0.07, TSN 0.12, TSUK 0.10, TSTH 0.03) rather than a single consolidated number."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Net Zero emissions for the Tata Steel Group",
        "metric": "Scope 1 and 2 emissions",
        "baseline": null,
        "targetValue": "Net Zero",
        "timeline": "2045"
      },
      {
        "description": "Achieve specific dust emission intensity of 0.43kg per tonne of crude steel in India",
        "metric": "Dust Emission Intensity",
        "baseline": null,
        "targetValue": "0.43 kg/tonne",
        "timeline": "2025"
      },
      {
        "description": "Achieve specific freshwater consumption of 2.0 m3 per tonne of crude steel across all steelmaking sites in India",
        "metric": "Freshwater consumption",
        "baseline": null,
        "targetValue": "2.0 m3/tonne",
        "timeline": "2025"
      }
    ],
    "initiatives": [
      {
        "name": "Zero Carbon Logistics programme",
        "area": "emissions",
        "description": "Reduce CO2 footprint caused by the transport of product to the customer by 30% by 2030. Modalities like Optimum Voyage used to optimise fuel efficiency.",
        "outcome": "Savings of approx 5% of CO2 emissions. Replacing road transport with rail reduced >5,000 trucks per year."
      },
      {
        "name": "Benchmarking Energy Efficiency IMPACT Centre",
        "area": "energy",
        "description": "Drive energy efficiency campaigns across the Company, ensuring rigor, visibility, and ownership.",
        "outcome": "Savings of more than Rs. 750 crore since 2015."
      },
      {
        "name": "Tata Power Renewable Energy Limited agreement",
        "area": "energy",
        "description": "Set up 950 MW solar & wind hybrid renewable power capacity under captive arrangement.",
        "outcome": "Will cater to 379 MW of power requirement and enable reduction of over 2 million tonnes of CO2 per annum."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "13.1 Million tonnes of CO2 equivalent",
      "categories": [],
      "note": "Tata Steel is one of the few companies to measure end-to-end Scope 3 emissions for all modes of transportation, giving it the same focus as Scope 1 and Scope 2 emissions."
    },
    "managementCommentary": "In line with our vision of being the steel industry benchmark in Corporate Citizenship, Tata Steel has adopted Environmental, Social & Governance goals for the organisation, which drive our initiatives across the Company. We are committed to avoiding operational activities near sites containing globally or nationally important biodiversity. The Policy aspires to achieve no Net Loss of Biodiversity.",
    "awardsAndRatings": [
      {
        "name": "JRDQV award (Benchmark Leader under TBEM Assessment)",
        "score": null,
        "year": "2021"
      },
      {
        "name": "ResponsibleSteel™ Certification",
        "score": "Certified (Jamshedpur site)",
        "year": "2022"
      }
    ],
    "nonCompliance": [],
    "forwardLooking": [
      {
        "description": "Net Zero emissions for the Tata Steel Group",
        "timeline": "2045"
      },
      {
        "description": "Cover 100% sites under Biodiversity Management Plans across India, UK and the Netherlands.",
        "timeline": "2025"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "The Anti-Bribery and Anti-Corruption (ABAC) Policy ensures operations are conducted with highest ethical standards, preventing fraud, bribery and corruption, applicable to all employees, contractors, and partners.",
      "P3_ohs": "The Safety & Occupational Health Policy commits to 'Zero Harm' and becoming an industry leader in safety and health performance through robust management and reporting systems.",
      "P6_environment": "The Biodiversity and Environmental policies integrate biodiversity into the business ecosystem, aiming for no Net Loss of Biodiversity and ensuring habitat conservation and restoration."
    },
    "steelProduction": {
      "value": null,
      "unit": "metric tonnes",
      "note": "Crude steel production volume is not explicitly stated in the extracted BRSR text, though capacity is mentioned as 35 MTPA."
    },
    "reportingBoundary": "Consolidated basis for Tata Steel Limited and its 13 key subsidiary companies."
  }
}
{
  "companyId": "tata-steel",
  "year": "FY2024",
  "source": "PDF",
  "xbrlPatches": {
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput": {
      "pdfValue": "3.1",
      "pdfUnit": "Tonnes/tonnes of crude steel",
      "action": "CONFIRM",
      "note": "Confirmed against the Standalone FY2023-24 column."
    },
    "TotalEnergyConsumedFromRenewableAndNonRenewableSources": {
      "pdfValue": "545.96",
      "pdfUnit": "PJ",
      "action": "CORRECT",
      "note": "PDF reports 545.96 PJ (Peta Joules), which translates to 545,960,000 GJ. XBRL shows the exact GJ conversion."
    },
    "TotalVolumeOfWaterWithdrawal": {
      "pdfValue": "1,02,359",
      "pdfUnit": "Million Litres",
      "action": "CORRECT",
      "note": "PDF reports 1,02,359 Million Litres, which equals 102,359,000 kL."
    },
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "0.000063",
      "pdfUnit": "Kilolitres/rupee of turnover",
      "action": "CORRECT",
      "note": "PDF reports 0.000063 Kilolitres per rupee."
    },
    "Sox_FY2024": {
      "pdfValue": "38",
      "pdfUnit": "Kilotonnes/year",
      "action": "FOUND",
      "note": "SOx not in XBRL for FY2024 — Standalone FY2023-24 value reported in PDF is 38 Kilotonnes/year."
    },
    "Nox_FY2024": {
      "pdfValue": "20",
      "pdfUnit": "Kilotonnes/year",
      "action": "FOUND",
      "note": "NOx not in XBRL for FY2024 — Standalone FY2023-24 value reported in PDF is 20 Kilotonnes/year."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Net Zero emissions for the Tata Steel Group",
        "metric": "Scope 1 and Scope 2 emissions",
        "baseline": null,
        "targetValue": "Net Zero",
        "timeline": "2045"
      },
      {
        "description": "Achieve specific freshwater consumption of <1.5 cubic metres per tonne of crude steel across all sites in India",
        "metric": "Water intensity",
        "baseline": null,
        "targetValue": "<1.5 m3/tonne",
        "timeline": "2030"
      },
      {
        "description": "Achieve 20% diversity in workforce for Tata Steel Limited",
        "metric": "Diversity",
        "baseline": null,
        "targetValue": "20%",
        "timeline": "2025"
      }
    ],
    "initiatives": [
      {
        "name": "Zero Carbon Logistics programme",
        "area": "emissions",
        "description": "Aim to reduce CO2 footprint caused by the transport of its products to the customer by 30% by 2030.",
        "outcome": "Optimum Voyage resulted in savings of approx 5% in CO2 emissions."
      },
      {
        "name": "Captive Renewable Power Sourcing",
        "area": "energy",
        "description": "Definitive agreement with Tata Power to source 379 MW of captive renewable power.",
        "outcome": "Will reduce 50 million tonnes of carbon emissions over the contract period of 25 years."
      },
      {
        "name": "Floating Solar Power Project",
        "area": "energy",
        "description": "Commissioned a 10.8 MWp floating solar power project on the upper cooling pond in Jamshedpur.",
        "outcome": "Brought total capacity to 20.34 MWp solar projects in the Jamshedpur plant."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "15 Million tonnes CO2e (Standalone)",
      "categories": [],
      "note": "Measurement of end-to-end Scope 3 emissions for all modes of transportation is highly prioritized alongside Scope 1 and 2."
    },
    "managementCommentary": "We are proud to present the second edition of our Business Responsibility and Sustainability Report (BRSR), underscoring our unwavering commitment to Environmental, Social, and Governance (ESG) stewardship. As the global shift to a low-carbon economy gains momentum, Tata Steel has been at the forefront of advancing sustainable practices by reducing greenhouse gas emissions, increasing energy efficiency, improving water management, and promoting waste recycling initiatives through innovative R&D investments.",
    "awardsAndRatings": [
      {
        "name": "TAAP Assessment",
        "score": "700-725",
        "year": "2023"
      }
    ],
    "nonCompliance": [],
    "forwardLooking": [
      {
        "description": "Net Zero emissions for the Tata Steel Group",
        "timeline": "2045"
      },
      {
        "description": "Achieve zero harm for Tata Steel Limited",
        "timeline": "2030"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "Tata Code of Conduct (TCoC) and Anti-Bribery and Anti-Corruption Policy guide fair practices and ethics for the Company, establishing a framework against fraud, bribery, and corruption.",
      "P3_ohs": "The Safety Principles and Occupational Health Policy aim to secure zero harm. The framework includes continuous monitoring and hazard assessment like the Safety Leadership Development Centres.",
      "P6_environment": "The Responsible Supply Chain Policy (RSCP) and Environmental Policy enforce tracking and mitigation of scope emissions, environmental restoration, and material efficiency goals."
    },
    "steelProduction": {
      "value": null,
      "unit": "metric tonnes",
      "note": "Not explicitly stated in the extracted BRSR text block."
    },
    "reportingBoundary": "Disclosed both on a standalone and on a consolidated basis for Tata Steel Limited (FY24 values extracted refer to Standalone)."
  }
}
{
  "companyId": "tata-steel",
  "year": "FY2025",
  "source": "PDF",
  "xbrlPatches": {
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput": {
      "pdfValue": "3.2",
      "pdfUnit": "Tonnes/tonnes of crude steel",
      "action": "CONFIRM",
      "note": "Confirmed against the Standalone FY2024-25 column."
    },
    "TotalEnergyConsumedFromRenewableAndNonRenewableSources": {
      "pdfValue": "587.56",
      "pdfUnit": "PJ",
      "action": "CORRECT",
      "note": "PDF reports 587.56 PJ (Peta Joules), matching the 587,567,890 GJ in XBRL."
    },
    "TotalVolumeOfWaterWithdrawal": {
      "pdfValue": "1,10,829",
      "pdfUnit": "Million Litres",
      "action": "CORRECT",
      "note": "PDF reports 1,10,829 Million Litres, which equals 110,829,000 kL."
    },
    "Sox_FY2025": {
      "pdfValue": "46",
      "pdfUnit": "Kilotonnes/year",
      "action": "FOUND",
      "note": "SOx not in XBRL for FY2025 — Standalone FY2024-25 value reported in PDF is 46 Kilotonnes/year."
    },
    "Nox_FY2025": {
      "pdfValue": "24",
      "pdfUnit": "Kilotonnes/year",
      "action": "FOUND",
      "note": "NOx not in XBRL for FY2025 — Standalone FY2024-25 value reported in PDF is 24 Kilotonnes/year."
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "Net Zero emissions for the Tata Steel Group",
        "metric": "Scope 1 and Scope 2 emissions",
        "baseline": null,
        "targetValue": "Net Zero",
        "timeline": "2045"
      }
    ],
    "initiatives": [
      {
        "name": "Green Mobility Fleet Expansion",
        "area": "emissions",
        "description": "Deployed 70% Electric Vehicles (EVs) in warehouse and delivery operations.",
        "outcome": "Resulted in a reduction of ~200 tons of CO2 annually."
      },
      {
        "name": "B24 Biofuel Shipments",
        "area": "emissions",
        "description": "First Indian steel company to conduct full laden leg shipments using B24 biofuel from Australia to India.",
        "outcome": "Executed 39 biofuel vessels and 5 LNG vessels, accounting for almost 18% of imported shipments."
      },
      {
        "name": "Rooftop Solar Panel",
        "area": "energy",
        "description": "Installation of a 2.2 MW rooftop solar panel at the Jamshedpur Warehouse.",
        "outcome": "Facility became energy-positive, generating 2,303 MWh against a consumption of 1,582 MWh."
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "23 Million tonnes CO2e (Standalone)",
      "categories": [],
      "note": "Emphasis is placed on Scope 3 logistics tracking, including adopting global frameworks for emissions reporting in subsidiary hubs."
    },
    "managementCommentary": "We have embraced decarbonisation not as a compulsion but as a deliberate choice with shared enthusiasm. The report highlights how we are moving decisively from intent to impact, re-engineering and future proofing the operations across the full arc of our value chain. We realise technological innovation is our bridge to the future and have accelerated efforts towards digitalisation, automation, AI enabled systems and climate smart solutions to drive sustainability led transformation.",
    "awardsAndRatings": [
      {
        "name": "ResponsibleSteel™ Certification",
        "score": "Certified (Jamshedpur, Kalinganagar, and Meramandali)",
        "year": "2024"
      }
    ],
    "nonCompliance": [
      {
        "description": "Collector of Stamps, Enforcement I and II imposed penalties of Rs 1,46,14,380 and Rs 1,28,07,700 on the Company towards belated filing of stamp-duty application related to scheme of amalgamation.",
        "resolution": "Penalty paid; no appeal preferred."
      }
    ],
    "forwardLooking": [
      {
        "description": "Net Zero emissions",
        "timeline": "2045"
      }
    ],
    "qualitativePolicies": {
      "P1_ethics": "The Tata Code of Conduct and related whistleblower/anti-bribery policies mandate transparent, accountable, and ethical behavior from all stakeholders and employees.",
      "P3_ohs": "The occupational health and safety systems aim for zero harm, relying on continuous internal reviews, 6-strategic initiative frameworks, and robust grievance redressing systems.",
      "P6_environment": "Environmental and Biodiversity policies detail commitments toward habitat protection, nature-positive solutions, emission curbs, and integration of the 4R framework across plants."
    },
    "steelProduction": {
      "value": null,
      "unit": "metric tonnes",
      "note": "Not explicitly stated in the extracted BRSR text block."
    },
    "reportingBoundary": "Disclosed both on a standalone and on a consolidated basis for Tata Steel Limited (FY25 values extracted refer to Standalone)."
  }
}