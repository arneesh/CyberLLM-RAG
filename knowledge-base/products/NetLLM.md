# NetLLM

## AI-Driven Network Security Monitoring & SIEM

NetLLM is CyberLLM's network security monitoring and Security Information and Event Management (SIEM) platform. Built for enterprises with complex, hybrid network environments, NetLLM provides deep visibility into east-west and north-south traffic, correlates events across thousands of data sources, and uses AI-driven anomaly detection to surface threats that rule-based systems miss. The platform replaces or augments legacy SIEMs (Splunk, QRadar, ArcSight) with a modern, AI-native architecture designed for the scale and speed of today's threat landscape.

NetLLM ingests data from virtually any source — firewalls, routers, switches, proxies, DNS servers, cloud VPCs, SaaS applications, endpoint agents, and custom applications — normalizing, enriching, and indexing events in real time. Its correlation engine applies both traditional rule-based detection and AI-powered behavioral analytics to identify known attack patterns (command-and-control beaconing, data exfiltration, lateral movement) as well as novel, previously unseen anomalies that deviate from learned network baselines.

The platform's customizable dashboards provide SOC analysts with real-time situational awareness, while automated playbook triggers ensure that critical events are escalated and responded to without manual intervention. NetLLM integrates natively with IncidentLLM for automated response orchestration and with ThreatLLM for real-time threat context enrichment.

## Key Features

- **AI-Driven Anomaly Detection** — Unsupervised machine learning models continuously learn normal network behavior and flag deviations. Detects C2 beaconing, DNS tunneling, data exfiltration, and lateral movement without predefined rules.
- **Deep Packet Inspection** — Full Layer 7 visibility with protocol decoding for 200+ application protocols including HTTP/S, DNS, SMB, SSH, RDP, Kerberos, and proprietary industrial protocols (Modbus, DNP3, OPC-UA).
- **Log Aggregation & Normalization** — Ingests logs from any source via Syslog, CEF, LEEF, JSON, Windows Event Forwarding, cloud-native connectors (AWS CloudTrail, Azure Activity Logs, GCP Audit Logs), and custom parsers. Normalizes events into a unified schema for cross-source correlation.
- **Correlation Engine** — Combines rule-based detection (2,000+ prebuilt detection rules mapped to MITRE ATT&CK) with AI behavioral analytics for layered threat detection. Supports custom correlation rules via a visual rule builder and a Python-based scripting interface.
- **Customizable Dashboards** — Real-time dashboards with drag-and-drop widgets for network topology maps, traffic flow visualizations, alert timelines, geolocation maps, and custom metrics. Dashboards are shareable and role-based (SOC analyst, CISO, compliance officer).
- **Automated Playbook Triggers** — When detection rules or anomaly models fire, NetLLM can automatically trigger response playbooks in IncidentLLM, create tickets in ServiceNow or Jira, send notifications via Slack or PagerDuty, or execute custom webhooks.
- **Network Forensics** — Full packet capture (PCAP) storage with indexed search. Analysts can reconstruct sessions, extract files, and replay network conversations for forensic investigation.
- **Scalable Architecture** — Distributed data pipeline built on Apache Kafka and ClickHouse, capable of ingesting and querying 500,000+ events per second with sub-second search latency. Horizontal scaling with no performance degradation.

## Pricing

| Tier | Monthly Price | Includes |
|------|--------------|----------|
| **Standard** | $4,000/mo | Up to 50 GB/day log ingestion, AI anomaly detection, 1,000 prebuilt detection rules, 5 customizable dashboards, 30-day data retention, email and Slack alerting, community support. |
| **Professional** | $9,000/mo | Up to 500 GB/day ingestion, full 2,000+ detection rules, unlimited dashboards, deep packet inspection, network forensics (7-day PCAP), automated playbook triggers, IncidentLLM integration, 90-day retention, priority support with 4-hour SLA. |
| **Enterprise** | Custom | Unlimited ingestion, all Professional features plus custom detection rule development, extended PCAP retention, dedicated data pipeline, multi-region deployment, dedicated Customer Success Manager, 1-hour SLA, on-site deployment support. |

Annual contracts receive a 15% discount. Volume discounts available for multi-product CyberLLM deployments.

## Deployment Options

- **SaaS** — Multi-tenant cloud deployment. Fastest time to value (< 7 days). Recommended for most customers.
- **Dedicated Cloud** — Single-tenant cloud instance on AWS, Azure, or GCP. Available for Professional and Enterprise tiers.
- **On-Premises** — Self-hosted deployment for air-gapped and highly regulated environments. Enterprise tier only.
- **Hybrid** — On-premises collectors with cloud-based analytics. Ideal for organizations with distributed network segments.

## Roadmap

| Milestone | Target Date | Description |
|-----------|-------------|-------------|
| **NetLLM 3.0 — AI-Generated Detection Rules** | Q3 2025 | Introduce an AI engine that analyzes network telemetry and automatically generates custom detection rules tailored to each customer's environment, reducing detection engineering effort by 80%. |
| **OT/ICS Network Monitoring** | Q1 2026 | Add purpose-built monitoring for operational technology (OT) and industrial control system (ICS) networks, including protocol support for Modbus TCP, DNP3, EtherNet/IP, and BACnet. |
| **Cloud-Native Network Detection (NDR)** | Q4 2026 | Extend network detection capabilities to cloud-native workloads with deep integration into AWS VPC Flow Logs, Azure NSG Flow Logs, and GCP VPC Flow Logs, plus container-level network monitoring for Kubernetes. |
| **NetLLM + ShieldLLM XDR Fusion** | Q2 2027 | Unify network telemetry with endpoint telemetry in a single analytics engine, enabling correlated detections that span both network and endpoint layers for true Extended Detection and Response (XDR). |

## Customers

NetLLM currently monitors networks for 4 enterprise clients across the financial services, energy, and government verticals. The platform ingests a combined 2.8 TB of log data per day and monitors over 150,000 network endpoints.

## Getting Started

Contact our sales team at [sales@cyberllm.com](mailto:sales@cyberllm.com) or visit [www.cyberllm.com/netllm](https://www.cyberllm.com/netllm) to schedule a demo.
