# Master Service Agreement: CyberLLM Inc. & Nexus Cloud Services — PenLLM Enterprise

**Agreement Number:** CL-PLM-2024-0203
**Effective Date:** April 15, 2024
**Document Classification:** Confidential

---

## 1. Parties

This Master Service Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cipher Boulevard, Austin, TX 78701 ("Provider")
- **Nexus Cloud Services**, a Washington corporation with principal offices at 7700 Cumulus Way, Seattle, WA 98101 ("Client")

## 2. Term and Duration

This Agreement shall commence on April 15, 2024, and shall continue for a period of **thirty-six (36) months**, terminating on April 14, 2027, unless renewed or terminated in accordance with the provisions herein.

## 3. Product and Scope of Services

Provider shall deliver **PenLLM Enterprise** — an AI-driven vulnerability management and penetration testing platform — with a custom configuration designed for multi-tenant cloud hosting environments. The scope includes:

- Multi-tenant vulnerability management engine capable of scanning Client's shared infrastructure and isolated customer environments without cross-tenant data leakage
- Continuous CI/CD pipeline security integration via native plugins for GitHub Actions, GitLab CI, and Jenkins, performing automated security gate checks on every deployment
- Customer-facing security posture reports generated on-demand, white-labeled with Nexus Cloud branding, suitable for distribution to Client's end customers
- Bug bounty triage integration module connecting to Client's HackerOne program, with automated duplicate detection and severity scoring powered by CyberLLM's AI engine
- Infrastructure-as-Code (IaC) scanning for Terraform, CloudFormation, and Kubernetes manifests across Client's provisioning pipelines
- API security testing covering Client's public-facing REST and GraphQL endpoints, with OWASP API Top 10 coverage
- Dedicated threat modeling workshops (2 per year) led by CyberLLM's Application Security team

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee (Custom Enterprise) | $15,000.00 |
| One-Time Setup, Integration & Customization Fee | $60,000.00 |
| Annual IaC Policy Library Update | Included |
| White-Label Report Module | Included |

- All fees are billed monthly in arrears. Invoices are issued on the 1st of each calendar month.
- Payment is due within thirty (30) days of invoice date.
- Late payments shall accrue interest at the rate of 1.5% per month or the maximum rate permitted by applicable law, whichever is less.
- The one-time setup fee may be paid in two equal installments: 50% upon execution, 50% upon completion of initial deployment (estimated 45 days).

## 5. Service Level Agreement (SLA)

Provider guarantees the following service levels:

- **Platform Uptime:** 99.95% measured monthly, excluding scheduled maintenance windows (maintenance limited to 4 hours/month, announced 72 hours in advance)
- **CI/CD Scan Latency:** Security gate results returned within 90 seconds for standard pipeline scans
- **Critical Vulnerability Notification:** Within 30 minutes of validated discovery for internet-facing assets
- **Bug Bounty Triage SLA:** Submitted reports scored and deduplicated within 4 hours
- **SLA Credits:** For each 0.1% below the uptime guarantee, Client shall receive a credit of 5% of that month's fee, up to a maximum of 30%

## 6. Support

Client shall receive **Tier 1 — Dedicated Enterprise Support**, which includes:

- 24/7/365 access to CyberLLM's Cloud Security Operations team via phone, encrypted Slack channel, and support portal
- Named Senior Security Engineer assigned to the Nexus Cloud account
- Weekly sync calls during the first 90 days of deployment; bi-weekly thereafter
- Escalation to CyberLLM's Principal Engineers within 2 hours for platform-impacting issues
- On-site support available upon request (up to 6 visits per year, travel expenses billed separately)

## 7. Confidentiality

Both parties agree to maintain the confidentiality of all proprietary information exchanged under this Agreement. Confidential information includes, but is not limited to, vulnerability data, customer-facing reports, multi-tenant architecture details, CI/CD pipeline configurations, and financial terms. Provider shall not access, store, or process any of Client's end-customer data beyond what is strictly necessary for vulnerability scanning. This obligation survives termination for a period of five (5) years.

## 8. Data Handling and Compliance

- All scan data shall be encrypted at rest (AES-256) and in transit (TLS 1.3)
- Multi-tenant scan results shall be logically isolated with enforced access controls preventing cross-tenant visibility
- Provider shall maintain SOC 2 Type II and ISO 27001 certifications
- Provider shall support Client's compliance with SOC 2, ISO 27001, and CSA STAR audit requirements by providing evidence artifacts upon request

## 9. Renewal

This Agreement shall automatically renew for successive twelve (12) month periods unless either party provides written notice of non-renewal at least ninety (90) days prior to the end of the then-current term. Renewal pricing shall not increase by more than 5% annually without mutual written agreement.

## 10. Termination

- Either party may terminate this Agreement for cause upon sixty (60) days' written notice if the other party materially breaches any provision and fails to cure such breach within the notice period.
- Client may terminate for convenience with one hundred twenty (120) days' written notice, subject to an early termination fee equal to 50% of the remaining monthly fees for the unexpired term.
- Upon termination, Provider shall securely destroy or return all Client data, including scan results and white-label report templates, within thirty (30) days and provide written certification of destruction.

## 11. Limitation of Liability

Provider's aggregate liability under this Agreement shall not exceed the total fees paid by Client in the twelve (12) months preceding the claim. Neither party shall be liable for indirect, incidental, consequential, or punitive damages. This limitation shall not apply to breaches of confidentiality obligations or gross negligence.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | Nexus Cloud Services |
|---|---|
| Signature: _________________________ | Signature: _________________________ |
| Name: Daniel Kovacs, CEO | Name: Rajesh Anand, CTO |
| Date: April 15, 2024 | Date: April 15, 2024 |
