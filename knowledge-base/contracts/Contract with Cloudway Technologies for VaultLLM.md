# Enterprise Master Services Agreement: CyberLLM Inc. and Cloudway Technologies — VaultLLM Enterprise (Multi-Cloud)

**Document ID:** CL-VLM-2024-0412  
**Effective Date:** May 1, 2024  
**Prepared By:** CyberLLM Enterprise & Cloud Solutions

---

## 1. Parties

This Enterprise Master Services Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cyber Ridge Boulevard, Austin, TX 78701 ("Provider")
- **Cloudway Technologies**, a Delaware corporation headquartered at 2200 Innovation Drive, San Jose, CA 95134 ("Client")

## 2. Term and Effective Date

- **Effective Date:** May 1, 2024
- **Initial Term:** Thirty-six (36) months, concluding April 30, 2027
- **Contract Value (Initial Term):** $504,000

## 3. Scope of Services

Provider shall deliver the **VaultLLM Enterprise** platform configured for cloud-native, multi-cloud SaaS environments, including:

- Unified encryption and key management across Client's **Amazon Web Services (AWS)**, **Microsoft Azure**, and **Google Cloud Platform (GCP)** deployments
- Centralized key lifecycle management for over **five hundred (500) microservices**, supporting automated key rotation, revocation, and audit logging
- Hardware Security Module (HSM) integration with cloud-native HSM services (AWS CloudHSM, Azure Dedicated HSM, Google Cloud HSM) for root key protection
- SOC 2 Type II compliance automation including continuous control monitoring, evidence collection, and auditor-ready report generation
- Bring Your Own Key (BYOK) and Hold Your Own Key (HYOK) capabilities across all three cloud providers
- Secrets management integration with Client's CI/CD pipelines (GitHub Actions, ArgoCD) and container orchestration (Kubernetes) environments
- Real-time encryption posture dashboard with multi-cloud visibility showing encryption coverage, key health, and compliance status
- Data tokenization services for Client's customer PII processed across distributed microservices
- Quarterly penetration testing of the VaultLLM deployment by Provider's internal red team, with findings shared under mutual NDA

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee | $14,000 |
| One-Time Multi-Cloud Deployment Fee | $60,000 |
| Annual Penetration Testing (included) | Included in monthly fee |

- Invoices are issued on the first business day of each calendar month and are payable within **thirty (30) days** of the invoice date.
- Late payments are subject to a finance charge of **1.5% per month** or the maximum rate allowed by law.
- The one-time deployment fee shall be invoiced in three installments: 40% upon execution, 30% upon completion of first cloud integration, and 30% upon full multi-cloud deployment acceptance.

## 5. Service Level Agreement (SLA)

- **Platform Uptime:** 99.99% measured monthly across all cloud regions
- **Key Management API Latency:** P99 response time under 50 milliseconds
- **Critical Incident Response:** Within fifteen (15) minutes, 24/7/365
- **High-Severity Response:** Within one (1) hour
- **Standard Response:** Within four (4) business hours
- **SLA Credit:** 10% of the monthly fee for each 0.01% below the 99.99% uptime target, capped at 30%. Sustained latency violations exceeding the P99 target for more than four (4) consecutive hours shall also trigger a 5% credit for the affected month.

## 6. Support

- **Tier:** Platinum Enterprise Support
- **Dedicated Team:** Named Technical Account Manager, Cloud Security Architect, and designated escalation engineer
- **Support Channels:** 24/7 phone, encrypted Slack channel, video conferencing on demand, secure ticketing portal
- **Architecture Reviews:** Semi-annual joint architecture reviews to optimize encryption strategy as Client's microservices footprint evolves
- **Escalation:** Severity-1 incidents escalate to CyberLLM CTO within one (1) hour

## 7. Confidentiality

Both parties shall maintain the confidentiality of all non-public information exchanged under this Agreement, including but not limited to Client's cloud architecture, encryption key hierarchies, microservice topology, and customer data schemas. Provider shall maintain SOC 2 Type II certification for its own operations throughout the term of the Agreement. All Provider personnel accessing Client environments shall undergo annual background checks and complete Client's security awareness training. Confidentiality obligations shall survive termination for a period of five (5) years.

## 8. Renewal

This Agreement shall automatically renew for successive **twenty-four (24) month** periods unless either party provides written notice of non-renewal at least **ninety (90) days** prior to the end of the then-current term. Renewal pricing is subject to negotiation, with annual increases not to exceed **3%** unless the scope of services materially changes.

## 9. Termination

- Either party may terminate for cause upon **sixty (60) days** written notice if the other party commits a material breach and fails to cure within that period.
- Client may terminate for convenience with **one hundred twenty (120) days** written notice, subject to an early termination fee equal to **six (6) months** of the monthly platform fee.
- In the event of termination, Provider shall execute a key migration plan to transfer all encryption keys and secrets to Client's designated successor solution, at Provider's expense, within ninety (90) days.
- Provider shall certify complete destruction of all Client key material and data from its systems within thirty (30) days following the completion of the migration.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | Cloudway Technologies |
|---|---|
| Signature: _________________ | Signature: _________________ |
| Name: David Nakamura | Name: Mei-Lin Zhou |
| Title: Chief Revenue Officer | Title: Chief Technology Officer |
| Date: May 1, 2024 | Date: May 1, 2024 |
