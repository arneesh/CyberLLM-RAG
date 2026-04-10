# Master Service Agreement: CyberLLM Inc. & MetroGov Municipal Authority — IdentLLM Enterprise

**Agreement Number:** CL-ILM-2024-0099
**Effective Date:** March 15, 2024
**Document Classification:** Controlled — For Official Use Only

---

## 1. Parties

This Master Service Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cipher Boulevard, Austin, TX 78701 ("Provider")
- **MetroGov Municipal Authority**, a municipal government entity organized under the laws of the State of Illinois, with principal offices at 200 Civic Center Plaza, Chicago, IL 60601 ("Client")

## 2. Term and Duration

This Agreement shall commence on March 15, 2024, and shall continue for a period of **forty-eight (48) months**, terminating on March 14, 2028, unless renewed or terminated in accordance with the provisions herein. This extended term reflects the complexity of multi-agency deployment and the Client's procurement cycle requirements.

## 3. Product and Scope of Services

Provider shall deliver **IdentLLM Enterprise** — an AI-powered identity and access management and Zero Trust platform — configured for municipal government operations supporting approximately 12,000 employees across multiple city agencies. The scope includes:

- Citizen-facing identity verification module enabling secure authentication for online permit applications, utility account management, public records requests, and municipal court filings, supporting NIST IAL2/AAL2 identity proofing standards
- Multi-agency Single Sign-On (SSO) federation connecting the Department of Public Works, Parks & Recreation, Finance, Public Safety (non-sworn), Health Services, and City Clerk's Office — supporting SAML 2.0 and OIDC protocols
- Multi-Factor Authentication (MFA) rollout for all 12,000 municipal employees, with phishing-resistant authentication (FIDO2/WebAuthn) for privileged accounts and mobile push for standard users
- FedRAMP High-equivalent security controls implemented across the IdentLLM platform to satisfy CISA and state-level cybersecurity mandates
- Automated identity lifecycle management with integration into Client's PeopleSoft HCM system, including civil service rule-based provisioning and inter-agency transfer workflows
- Privileged access management for critical infrastructure systems including SCADA/ICS water treatment and traffic management networks
- Comprehensive audit logging and compliance reporting aligned with NIST SP 800-63-3, CJIS Security Policy (for non-sworn Public Safety staff), and Illinois FOIA requirements

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee (Custom Enterprise) | $10,000.00 |
| One-Time Deployment, Integration & Agency Onboarding Fee | $75,000.00 |
| Citizen-Facing Identity Verification Module | Included |
| Privileged Access Management Module | Included |

- All fees are billed monthly in arrears. Invoices are issued on the 1st of each calendar month.
- Payment is due within sixty (60) days of invoice date, in accordance with the Illinois Local Government Prompt Payment Act (50 ILCS 505/).
- Late payments shall accrue interest in accordance with applicable state prompt payment statutes.
- The one-time deployment fee shall be paid in four equal quarterly installments, beginning upon execution of this Agreement.

## 5. Service Level Agreement (SLA)

Provider guarantees the following service levels:

- **Platform Uptime:** 99.95% measured monthly for employee authentication; 99.9% for citizen-facing identity services, excluding scheduled maintenance windows
- **Authentication Latency:** Employee SSO/MFA transactions completed within 400 milliseconds at the 99th percentile; citizen identity verification completed within 3 seconds
- **Employee Provisioning:** Automated account creation within 30 minutes of HR trigger; inter-agency transfers within 2 hours
- **Critical Security Alert Response:** Identity-based threats (credential compromise, privilege escalation attempts) escalated within 15 minutes
- **SLA Credits:** For each 0.1% below the uptime guarantee, Client shall receive a credit of 5% of that month's fee, up to a maximum of 25%. SLA credits shall be applied as offsets to future invoices.

## 6. Support

Client shall receive **Tier 1 — Dedicated Enterprise Support (Government)**, which includes:

- 24/7/365 emergency support for authentication platform outages; business hours support (Monday–Friday, 7 AM–6 PM CT) for standard issues
- Named Government Account Manager and Technical Architect assigned to the MetroGov account
- Monthly program review meetings with Client's Chief Information Officer and agency IT leads
- Escalation to CyberLLM's Director of Government Programs within 2 hours for critical incidents
- On-site support at Client's Civic Center offices and agency locations available upon request (up to 10 visits per year, inclusive of travel)
- Designated help desk liaison to support Client's internal IT service desk with Tier 2 escalations

## 7. Confidentiality

Both parties agree to maintain the confidentiality of all proprietary information exchanged under this Agreement. Confidential information includes, but is not limited to, employee identity data, citizen PII, network architecture details, critical infrastructure access policies, and financial terms. Provider acknowledges that certain information may be subject to the Illinois Freedom of Information Act (5 ILCS 140/) and shall cooperate with Client's FOIA compliance obligations. This obligation survives termination for a period of five (5) years.

## 8. Data Handling and Compliance

- All identity data shall be encrypted at rest (AES-256) and in transit (TLS 1.3), with FIPS 140-2 validated cryptographic modules
- Provider shall maintain FedRAMP High authorization (or demonstrate equivalent controls via independent third-party assessment) and SOC 2 Type II certification
- Provider shall comply with CJIS Security Policy requirements for any systems accessible by Public Safety personnel
- Citizen PII shall be handled in compliance with the Illinois Personal Information Protection Act (815 ILCS 530/) and applicable municipal privacy ordinances
- All data shall be stored and processed within the continental United States
- Provider shall undergo annual penetration testing and make results available to Client's IT Security team upon request

## 9. Renewal

This Agreement shall automatically renew for successive twenty-four (24) month periods unless either party provides written notice of non-renewal at least one hundred twenty (120) days prior to the end of the then-current term, subject to Client's appropriation of sufficient funds and compliance with applicable procurement regulations. Renewal pricing shall not increase by more than 3% per annum absent mutual written agreement.

## 10. Termination

- Either party may terminate this Agreement for cause upon sixty (60) days' written notice if the other party materially breaches any provision and fails to cure such breach within the notice period.
- Client may terminate for convenience with ninety (90) days' written notice. Given the public sector nature of this engagement, no early termination fee shall apply if termination results from loss of budgetary appropriation or mandate from the City Council.
- In all other convenience termination scenarios, an early termination fee equal to 25% of the remaining monthly fees for the unexpired term shall apply.
- Provider shall provide a transition assistance period of up to one hundred twenty (120) days following termination to support Client's migration, billed at Provider's then-current professional services rates.
- Upon termination, Provider shall securely destroy or return all Client data within thirty (30) days of migration completion and provide written certification of destruction.

## 11. Limitation of Liability

Provider's aggregate liability under this Agreement shall not exceed the total fees paid by Client in the twelve (12) months preceding the claim. Neither party shall be liable for indirect, incidental, consequential, or punitive damages. This limitation shall not apply to breaches of data protection obligations, confidentiality, or violations of applicable law. Nothing in this Agreement shall be construed to waive Client's governmental immunity.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | MetroGov Municipal Authority |
|---|---|
| Signature: _________________________ | Signature: _________________________ |
| Name: Daniel Kovacs, CEO | Name: Denise Okafor, Chief Information Officer |
| Date: March 15, 2024 | Date: March 15, 2024 |
