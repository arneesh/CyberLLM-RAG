# Master Service Agreement: CyberLLM Inc. & Spectrum Communications — IdentLLM Standard

**Agreement Number:** CL-ILM-2024-0341
**Effective Date:** July 1, 2024
**Document Classification:** Confidential

---

## 1. Parties

This Master Service Agreement ("Agreement") is entered into by and between:

- **CyberLLM Inc.**, a Delaware corporation with principal offices at 440 Cipher Boulevard, Austin, TX 78701 ("Provider")
- **Spectrum Communications**, a Colorado corporation with principal offices at 850 Signal Ridge Parkway, Denver, CO 80202 ("Client")

## 2. Term and Duration

This Agreement shall commence on July 1, 2024, and shall continue for a period of **twelve (12) months**, terminating on June 30, 2025, unless renewed or terminated in accordance with the provisions herein.

## 3. Product and Scope of Services

Provider shall deliver **IdentLLM Standard** — an AI-powered identity and access management platform — configured for a mid-size telecommunications company with approximately 800 employees. The scope includes:

- Single Sign-On (SSO) deployment integrating Client's existing Azure Active Directory tenant with Client's network operations center (NOC) tools, customer billing platform, field service management system, and corporate Microsoft 365 environment — supporting SAML 2.0 and OIDC protocols
- Multi-Factor Authentication (MFA) rollout for all 800 employees, using Microsoft Authenticator push notifications as the primary method with SMS fallback, enforced via Conditional Access policies synchronized between Azure AD and IdentLLM
- Contractor and vendor access management module enabling time-limited, scoped access for third-party field technicians and managed service providers, with automated expiration and access review workflows
- Azure AD integration layer providing bidirectional synchronization of user attributes, group memberships, and license assignments between Azure AD and IdentLLM's identity governance engine
- Self-service password reset portal reducing help desk ticket volume for password-related issues
- Monthly identity health reports summarizing MFA adoption rates, dormant accounts, over-provisioned users, and contractor access status

## 4. Fees and Payment Terms

| Fee Component | Amount |
|---|---|
| Monthly Platform Fee | $2,500.00 |
| One-Time Setup & Azure AD Integration Fee | $8,000.00 |
| Contractor Access Management Module | Included |
| Self-Service Password Reset Portal | Included |

- All fees are billed monthly in arrears. Invoices are issued on the 1st of each calendar month.
- Payment is due within thirty (30) days of invoice date.
- Late payments shall accrue interest at the rate of 1.5% per month or the maximum rate permitted by applicable law, whichever is less.
- The one-time setup fee shall be invoiced upon execution of this Agreement and is due within thirty (30) days.

## 5. Service Level Agreement (SLA)

Provider guarantees the following service levels:

- **Platform Uptime:** 99.5% measured monthly, excluding scheduled maintenance windows (maintenance performed during weekends, 12 AM–6 AM MT)
- **Authentication Latency:** SSO and MFA transactions completed within 800 milliseconds at the 95th percentile
- **Contractor Provisioning:** New contractor accounts provisioned within 1 hour of approved request submission
- **Contractor Access Revocation:** Automated revocation within 30 minutes of contract end date or manual trigger
- **SLA Credits:** For each 0.5% below the uptime guarantee, Client shall receive a credit of 5% of that month's fee, up to a maximum of 15%

## 6. Support

Client shall receive **Tier 3 — Standard Support**, which includes:

- Business hours support (Monday–Friday, 8 AM–6 PM MT) via email and support portal
- Target first response within 8 business hours for standard issues, 2 business hours for authentication outages
- Access to CyberLLM's self-service knowledge base, Azure AD integration guides, and troubleshooting documentation
- Quarterly account review call with a CyberLLM Customer Success representative
- Escalation to senior engineers for critical platform outages affecting all users

## 7. Confidentiality

Both parties agree to maintain the confidentiality of all proprietary information exchanged under this Agreement. Confidential information includes, but is not limited to, employee identity data, Azure AD configurations, network architecture details, contractor information, and financial terms. This obligation survives termination for a period of three (3) years.

## 8. Data Handling and Compliance

- All identity data shall be encrypted at rest (AES-256) and in transit (TLS 1.3)
- Provider shall maintain SOC 2 Type II certification
- Provider acknowledges Client's obligations under FCC regulations, CPNI rules, and state-level telecommunications privacy requirements, and shall not access or process customer proprietary network information (CPNI)
- User identity data shall be stored within the continental United States

## 9. Renewal

This Agreement shall automatically renew for successive twelve (12) month periods unless either party provides written notice of non-renewal at least thirty (30) days prior to the end of the then-current term. Renewal pricing shall not increase by more than 5% annually without mutual written agreement.

## 10. Termination

- Either party may terminate this Agreement for cause upon thirty (30) days' written notice if the other party materially breaches any provision and fails to cure such breach within the notice period.
- Client may terminate for convenience with sixty (60) days' written notice, subject to an early termination fee equal to 25% of the remaining monthly fees for the unexpired term.
- Upon termination, Provider shall securely destroy or return all Client identity data within thirty (30) days and provide written certification of destruction.

## 11. Limitation of Liability

Provider's aggregate liability under this Agreement shall not exceed the total fees paid by Client in the twelve (12) months preceding the claim. Neither party shall be liable for indirect, incidental, consequential, or punitive damages.

---

**IN WITNESS WHEREOF**, the parties have executed this Agreement as of the Effective Date.

| CyberLLM Inc. | Spectrum Communications |
|---|---|
| Signature: _________________________ | Signature: _________________________ |
| Name: Daniel Kovacs, CEO | Name: Brian Castellano, IT Director |
| Date: July 1, 2024 | Date: July 1, 2024 |
