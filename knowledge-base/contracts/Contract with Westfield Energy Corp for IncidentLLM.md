# SaaS Services Agreement: CyberLLM Inc. and Westfield Energy Corp. — IncidentLLM Platform

**Effective Date:** July 1, 2025
**Contract Number:** IL-WEC-2025-0078

---

## 1. Parties

- **Provider:** CyberLLM Inc., a Delaware corporation, with principal offices at 440 Security Boulevard, Suite 1200, Austin, TX 78701 ("CyberLLM").
- **Client:** Westfield Energy Corp., a Texas corporation and registered utility operator, with principal offices at 1400 Smith Street, Suite 3200, Houston, TX 77002 ("Client").

## 2. Term and Effective Date

This Agreement shall commence on July 1, 2025 and continue for an initial term of eighteen (18) months, expiring on December 31, 2026 (the "Initial Term"), unless earlier terminated in accordance with Section 8.

## 3. Subscription Tier and Monthly Fee

- **Tier:** IncidentLLM Advanced
- **Monthly Subscription Fee:** $10,000.00 USD
- **One-Time Setup and OT Integration Fee:** $18,000.00 USD (due upon execution)

## 4. Scope of Services and Features

CyberLLM shall provide Client access to the IncidentLLM Advanced platform with operational technology (OT) incident response capabilities:

- OT-specific incident response playbooks covering SCADA system compromise, HMI tampering, PLC logic manipulation, and industrial control system (ICS) network intrusions.
- NERC Critical Infrastructure Protection (CIP) incident reporting automation, including CIP-008-6 incident identification, classification, and reporting to the Electricity Information Sharing and Analysis Center (E-ISAC) within mandated timelines.
- Integration with Client's existing SCADA monitoring infrastructure (OSIsoft PI, GE iFIX) via read-only OPC-UA connectors deployed in the IT/OT demilitarized zone (DMZ).
- Purdue Model-aware incident containment workflows that respect network segmentation boundaries between IT (Levels 4-5) and OT (Levels 0-3) environments.
- Automated incident escalation to the Cybersecurity and Infrastructure Security Agency (CISA) per TSA Security Directive Pipeline-2021-02 requirements.
- Threat intelligence enrichment from ICS-CERT advisories, Dragos WorldView threat intelligence, and Client's commercial feeds.
- Digital forensics support for OT environments including safe evidence collection procedures that do not disrupt process control operations.
- Post-incident recovery playbooks with phased OT system restoration procedures and safety validation checklists.

## 5. Service Level Agreement (SLA)

- **Platform Uptime:** CyberLLM guarantees 99.9% monthly uptime.
- **Critical OT Incident Response:** Initial triage within thirty (30) minutes, 24/7/365, by analysts with ICS/OT incident response experience.
- **High-Priority Incidents:** Response within two (2) hours.
- **Standard Incidents:** Response within eight (8) business hours.
- **SLA Credits:** 3% of monthly fee per full hour of unscheduled downtime, capped at 25%. Critical OT incident SLA breaches: $3,000 credit per occurrence.

## 6. Payment Terms

- Subscription fees are invoiced monthly on the first business day of each month.
- Payment is due within thirty (30) days of invoice date via ACH or wire transfer.
- Late payments shall accrue interest at 1.5% per month on the outstanding balance.
- The setup and integration fee is invoiced at execution and is non-refundable.

## 7. Support

- **Support Tier:** Advanced Support with OT Specialization
- **Channels:** Priority phone, encrypted email, in-platform ticketing, and a 24/7 OT incident hotline.
- **Response Times:** Critical OT within 30 minutes; high within 2 hours; medium within 8 hours; low within 2 business days.
- **OT Advisory Services:** Client shall receive up to eight (8) hours per quarter of OT security advisory consultation with CyberLLM's ICS Security Practice.
- **Training:** One (1) on-site training session at Client's operational control center, plus two (2) remote sessions for IT/OT SOC staff.

## 8. Termination

- Either party may terminate for cause upon sixty (60) days' written notice following a material breach that remains uncured for thirty (30) days.
- Client may terminate for convenience upon sixty (60) days' written notice, subject to an early termination fee equal to three (3) months of subscription fees.
- CyberLLM shall not disconnect or degrade services during an active incident response engagement, regardless of contract termination status, until the incident is resolved or Client provides written release.
- Upon termination, CyberLLM shall export all incident records, forensic artifacts, and playbook configurations within thirty (30) days.

## 9. Renewal

This Agreement shall automatically renew for successive twelve (12) month periods unless either party provides written notice of non-renewal at least sixty (60) days prior to the end of the then-current term. Renewal pricing may increase by up to 5% per year with sixty (60) days' advance notice.

## 10. Confidentiality and Critical Infrastructure Protection

All Client data—including network topology, SCADA configurations, and incident details—constitutes Critical Infrastructure Information (CII) and shall be treated with the highest level of confidentiality. CyberLLM shall comply with NERC CIP standards, TSA cybersecurity directives, and DOE Cybersecurity Capability Maturity Model (C2M2) guidelines. CyberLLM personnel accessing OT environment data shall undergo background checks and sign individual NDAs.

## 11. Limitation of Liability

Neither party's aggregate liability shall exceed the total fees paid or payable during the twelve (12) months preceding the claim. This cap excludes liability for breaches of CII confidentiality, willful misconduct, or gross negligence resulting in physical safety incidents.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | Westfield Energy Corp. |
|---|---|
| Signature: _________________ | Signature: _________________ |
| Name: David Keane, VP of Sales | Name: Robert Clarkson, VP of Cybersecurity & OT Risk |
| Date: July 1, 2025 | Date: July 1, 2025 |
