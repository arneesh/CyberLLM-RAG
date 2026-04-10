# Master Service Agreement: CyberLLM Inc. & Vertex Pharmaceuticals — ShieldLLM Enterprise

**Agreement Number:** CL-SLM-2024-0115
**Effective Date:** March 15, 2024
**Document Classification:** Confidential

---

## 1. Parties

This Master Service Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cipher Boulevard, Austin, TX 78701 ("Provider")
- **Vertex Pharmaceuticals**, a Massachusetts corporation with principal offices at 800 Helix Boulevard, Cambridge, MA 02142 ("Client")

## 2. Term

This Agreement shall be effective for **twenty-four (24) months**, from March 15, 2024, through March 14, 2026.

## 3. Product and Scope of Services

Provider shall deliver **ShieldLLM Enterprise** — AI-powered endpoint detection and response — configured for pharmaceutical and life sciences environments:

### 3.1 Endpoint Coverage
- Licensed for up to **8,000 endpoints** including corporate workstations, research lab systems, clinical trial data processing servers, and GxP-qualified systems
- Support for Windows, macOS, and Linux (RHEL, Ubuntu) operating systems
- Lightweight agent mode available for validated systems where software installation requires change control

### 3.2 Core EDR Capabilities
- AI-driven behavioral analysis, real-time threat detection, and automated response
- Advanced ransomware protection with canary file monitoring and rapid rollback capabilities
- Fileless attack detection, memory injection monitoring, and script-based attack prevention
- Endpoint forensics and investigation toolkit with full timeline reconstruction

### 3.3 Intellectual Property Protection
- Data exfiltration monitoring: detection of unusual data transfers, unauthorized cloud uploads, and USB device activity on endpoints containing R&D data
- Integration with Client's Microsoft Purview DLP for coordinated data protection alerting
- Custom detection rules targeting IP theft patterns specific to pharmaceutical research environments (e.g., bulk access to compound databases, abnormal access to clinical trial data repositories)

### 3.4 Regulatory Awareness
- Provider acknowledges Client's obligations under FDA 21 CFR Part 11 (Electronic Records; Electronic Signatures) and shall ensure ShieldLLM deployment does not interfere with validated system states.
- Agent deployment on GxP systems shall follow Client's computerized system validation (CSV) procedures. Provider shall furnish Installation Qualification (IQ) and Operational Qualification (OQ) documentation.
- Endpoint telemetry logs shall be maintained with tamper-evident integrity controls to support audit trail requirements.

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee (8,000 endpoints) | $12,000.00 |
| One-Time Deployment & Validation Support Fee | $35,000.00 |
| Additional Endpoints (beyond 8,000) | $1.75/endpoint/month |

- Monthly fees invoiced on the 1st; payment due net 30.
- Deployment fee invoiced 50% upon execution, 50% upon production deployment completion.
- Late payments accrue interest at 1.5% per month.
- Endpoint count reconciled quarterly; overages billed in the subsequent month.

## 5. Service Level Agreement

- **Agent Reporting Uptime:** 99.9% of deployed agents actively reporting, measured monthly
- **Console Availability:** 99.95% monthly
- **Detection to Alert:** Under 60 seconds for behavioral detections
- **GxP System Deployments:** Agent updates for validated systems shall be provided with 30 days' advance notice to allow Client change control review
- **SLA Credits:** 5% of monthly fee per 0.1% below agent uptime target, capped at 20%

## 6. Support

Client receives **Tier 1 — Enterprise Support**:

- 24/7/365 support from named Senior Endpoint Security Engineers
- Critical incidents: 30-minute response with immediate escalation path
- High severity: 2-hour response during business hours, 4-hour response outside business hours
- Dedicated Technical Account Manager (TAM) with bi-weekly sync calls
- Proactive monthly threat hunting using Client's endpoint telemetry, with focus on pharmaceutical-sector threats
- On-site support for critical incidents and semi-annual deployment health assessments (up to 4 visits/year)

## 7. Data Handling and Privacy

- All endpoint telemetry is encrypted at rest (AES-256) and in transit (TLS 1.3).
- Telemetry data stored in SOC 2 Type II-certified U.S. data centers.
- Provider shall not access or process any clinical trial data, patient information, or research compound data. ShieldLLM collects only security-relevant endpoint metadata.
- Provider shall comply with Client's data retention policies. Default telemetry retention: 12 months.

## 8. Confidentiality

Both parties shall maintain strict confidentiality of all proprietary information, including but not limited to research data references, security architecture, detection logic, and commercial terms. Provider acknowledges the heightened sensitivity of Client's intellectual property and agrees to limit access to Provider personnel on a need-to-know basis. Confidentiality obligations survive termination for five (5) years.

## 9. Renewal

This Agreement auto-renews for successive twelve (12) month periods unless either party provides ninety (90) days' written notice of non-renewal prior to the end of the then-current term. Price increases for renewal terms shall not exceed 5% annually.

## 10. Termination

- **For Cause:** Either party may terminate upon sixty (60) days' written notice for material breach that remains uncured.
- **For Convenience:** Client may terminate with ninety (90) days' notice, subject to an early termination fee of 35% of remaining monthly fees for the unexpired portion of the term.
- **Transition Period:** Provider shall offer a sixty (60) day transition period following notice of termination to assist with migration and agent removal.
- **Data Handling:** Upon termination, all Client telemetry data shall be securely deleted within thirty (30) days, with Certificate of Destruction provided. Audit logs required for regulatory purposes shall be made available to Client prior to deletion.

## 11. Limitation of Liability

Provider's total aggregate liability shall not exceed fees paid by Client in the twelve (12) months preceding the claim. Neither party shall be liable for indirect, incidental, or consequential damages, except in cases of breach of confidentiality involving Client's intellectual property or willful misconduct. Provider shall maintain professional liability and cyber insurance coverage of not less than $5,000,000.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | Vertex Pharmaceuticals |
|---|---|
| Signature: _________________________ | Signature: _________________________ |
| Name: Daniel Kovacs, CEO | Name: Dr. Helena Voss, SVP Information Security |
| Date: March 15, 2024 | Date: March 15, 2024 |
