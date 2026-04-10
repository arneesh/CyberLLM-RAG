# Master Service Agreement: CyberLLM Inc. & NovaTech Industries — ShieldLLM Enterprise

**Agreement Number:** CL-SLM-2024-0052
**Effective Date:** February 1, 2024
**Document Classification:** Confidential

---

## 1. Parties

This Master Service Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cipher Boulevard, Austin, TX 78701 ("Provider")
- **NovaTech Industries**, an Ohio corporation with principal offices at 1100 Automation Drive, Cleveland, OH 44114 ("Client")

## 2. Term and Duration

This Agreement is effective from February 1, 2024, for a period of **thirty-six (36) months**, ending January 31, 2027.

## 3. Product and Scope of Services

Provider shall deliver **ShieldLLM Enterprise** — an AI-powered endpoint detection and response (EDR) platform — covering Client's IT and OT environments:

### 3.1 Endpoint Coverage
- Licensed for up to **25,000 endpoints** including Windows, macOS, Linux workstations and servers, and supported OT endpoint agents for manufacturing control systems
- OT endpoint coverage includes monitoring of HMI stations, engineering workstations, and data historians connected to Client's manufacturing execution systems (MES)

### 3.2 Core EDR Capabilities
- AI-driven behavioral analysis for malware detection, lateral movement identification, and fileless attack prevention
- Real-time endpoint telemetry collection and centralized analysis
- Automated threat containment: network isolation, process termination, and file quarantine
- Forensic data collection and timeline reconstruction for incident investigations

### 3.3 Incident Response Retainer
- Dedicated incident response (IR) retainer of 200 hours annually, pre-paid and included in the monthly fee
- IR team on-call 24/7 with 30-minute mobilization for critical incidents
- Post-incident reports delivered within 5 business days of incident closure
- Unused retainer hours do not roll over between contract years

### 3.4 Integrations
- Integration with Client's CrowdStrike Falcon (legacy, to be phased out), Microsoft Defender for Endpoint (coexistence mode), and Palo Alto Cortex XSOAR for automated playbook execution
- Syslog forwarding to Client's Splunk SIEM

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee (25,000 endpoints + IR retainer) | $18,000.00 |
| One-Time Deployment Fee | $50,000.00 |
| Additional Endpoints (beyond 25,000) | $0.85/endpoint/month |

- Monthly invoices issued on the 1st; payment due net 30.
- Deployment fee invoiced in two equal installments: upon execution and upon completion of production rollout.
- Late payments accrue interest at 1.5% per month.
- Endpoint count audited quarterly. Overages billed in the following month's invoice.

## 5. Service Level Agreement

- **Agent Uptime:** 99.95% of deployed agents reporting to the management console, measured monthly
- **Detection Latency:** Threats detected and alerts generated within 60 seconds of malicious behavior on endpoints
- **Management Console Uptime:** 99.9% monthly
- **IR Mobilization:** Critical incidents: within 30 minutes; High severity: within 2 hours
- **SLA Credits:** 5% of monthly fee per 0.1% below the agent uptime target, capped at 25%

## 6. Support

Client receives **Tier 1 — Dedicated Enterprise Support**:

- 24/7/365 support with named Senior Endpoint Security Engineers assigned to Client
- Dedicated Slack channel, secure ticketing portal, and direct phone line
- Weekly operational review calls and monthly executive briefings
- Proactive threat hunting campaigns: at least one targeted hunt per month leveraging Client's endpoint telemetry
- On-site support available for critical incidents and quarterly deployment health checks (up to 6 visits/year)

## 7. OT-Specific Provisions

- Provider shall ensure ShieldLLM agents deployed in OT environments operate in monitoring-only mode by default to prevent unintended disruption to manufacturing processes.
- Any automated response actions in OT zones require explicit Client approval via a change management workflow integrated with Client's existing ITSM platform.
- Provider shall maintain awareness of Client's Purdue Model network segmentation and restrict agent communications accordingly.

## 8. Confidentiality

All proprietary information, including endpoint telemetry, detection logic, manufacturing process data, and contract terms, shall be treated as confidential. Unauthorized disclosure is prohibited. This obligation survives termination for five (5) years. Provider personnel with access to Client's OT environment data shall be subject to additional background verification.

## 9. Renewal

Auto-renews for successive twenty-four (24) month terms unless either party provides ninety (90) days' written notice of non-renewal. Annual price increases during renewal terms shall not exceed 4% without mutual agreement.

## 10. Termination

- **For Cause:** Either party may terminate upon sixty (60) days' notice for uncured material breach.
- **For Convenience:** Client may terminate with one hundred twenty (120) days' notice, subject to an early termination fee equal to 40% of remaining monthly fees for the unexpired term.
- **Transition Assistance:** Provider shall offer up to sixty (60) days of transition support to facilitate migration to an alternative solution.
- Upon termination, Provider shall remove all agents from Client endpoints and securely delete all Client telemetry data within forty-five (45) days.

## 11. Limitation of Liability

Provider's aggregate liability is limited to fees paid during the twelve (12) months preceding the claim. Neither party is liable for indirect, incidental, or consequential damages, except for breaches of confidentiality or willful misconduct. Provider shall carry cyber liability insurance of at least $10,000,000.

---

**IN WITNESS WHEREOF**, the parties execute this Agreement as of the Effective Date.

| CyberLLM Inc. | NovaTech Industries |
|---|---|
| Signature: _________________________ | Signature: _________________________ |
| Name: Daniel Kovacs, CEO | Name: Catherine Weiss, CTO |
| Date: February 1, 2024 | Date: February 1, 2024 |
