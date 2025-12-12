
# **Cyber Threat Intelligence Analysis of the Lazarus Group Using MISP**



## **📌 1. Introduction**

This project demonstrates the complete Cyber Threat Intelligence (CTI) lifecycle using **MISP (Malware Information Sharing Platform)**.
It simulates a real-world investigation of the **Lazarus Group**, a well-known Advanced Persistent Threat (APT) associated with:

* Ransomware operations
* Financial theft
* Cryptocurrency attacks
* Espionage campaigns

The project includes:

* Event creation
* Indicators of Compromise (IOC) collection
* MITRE ATT&CK mapping
* OSINT feed integration
* Python automation
* Threat statistics
* Email notification system
* Grafana visualization
* Full documentation

---

## **📌 2. Tools & Environment**

The analysis was conducted using:

* **Kali Linux**
* **Docker**
* **MISP** (deployed in Docker containers to simulate a SOC environment)

---

## **📌 3. Threat Actor Overview — Lazarus Group**

Lazarus is a **state-sponsored APT group** linked to major global incidents. Their activities include:

* Ransomware distribution (e.g., Ryuk)
* Banking credential theft
* Cryptocurrency theft
* Long-term cyber espionage

---

## **📌 4. Event Creation in MISP**

A dedicated threat event was created with:

* **Name:** *Lazarus Group – Financial & Ransomware Campaigns*
* **Threat Level:** High
* **Analysis Level:** Initial
* **Distribution:** Organization Only

This event serves as the main container for all intelligence related to Lazarus.

---

## **📌 5. Tagging, Classification & MITRE ATT&CK Mapping**

### **5.1 Event Tags**

The following classification tags were applied:

* `threat-actor:lazarus-group`
* `tlp:red`
* `attack-type:ransomware`
* `sector:finance`
* `veris:actor:motive="Espionage"`
* `veris:actor:motive="Financial"`
* `c2-infrastructure`

### **5.2 MITRE ATT&CK Galaxy Mappings**

Four ATT&CK techniques were mapped:

1. **Command Shell Execution**
2. **T1059.003 – Windows Command Shell**
3. **Credential Access from Browser Password Stores**
4. **Server-Side Execution via SQL Stored Procedures**

These mappings align Lazarus’ known behaviors with standardized ATT&CK techniques.

---

## **📌 6. ASN Enrichment (ipasn Module)**

The IP address **185.172.110.41**, associated with Lazarus operations, was enriched using the `ipasn` module.

Added intelligence included:

* **Last-seen timestamp**
* **Autonomous System Number (ASN)**
* **Announced subnet**

This enriches context for:

* Infrastructure attribution
* Hosting analysis
* Correlation with OSINT data
* Monitoring and pivoting

---

## **📌 7. Indicators of Compromise (IOCs)**

Five IOCs were added:

1. **IP Address:** 185.172.110.41
2. **Domain:** update-secure-login.com
3. **Malware Name:** Ryuk
4. **SHA256 Hash:** e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
5. **IP Address:** 45.142.215.12

These represent attacker infrastructure, malware payloads, and C2 nodes.

---

## **📌 8. OSINT Feed Integration**

Two external OSINT feeds were enabled:

* **CIRCL OSINT Feed**
* **Botvrij OSINT Feed**

Due to background worker limitations, feeds were synchronized manually:

```
./app/Console/cake Server fetchFeed 1 all
```

Warnings confirming previously existing events verified successful ingestion.

---

## **📌 9. Python Feed Parsing & Unification**

A Python script **feed_parser.py** was created to:

* Fetch multiple OSINT feeds
* Unify them into a single JSON file
* Save them as **unified_feeds.json**

This centralizes feed data for analysis.

---

## **📌 10. Feed Statistics Generation**

A second script **feed_stats.py** analyzed the unified feeds.

Results:

* **CIRCL indicators:** 20
* **Botvrij indicators:** 20
* **Total:** 40

These statistics verify successful parsing.

---

## **📌 11. Email Alert System (SMTP + SWAKS Testing)**

MISP was configured to send **email alerts** using Gmail SMTP over TLS.

Validation was done using **SWAKS** inside the Docker container to confirm:

* Successful authentication
* TLS negotiation
* Message delivery

User notification settings were adjusted to ensure analysts receive alerts when events are published.

---

## **📌 12. Grafana Visualization of OSINT Feed Statistics**

Grafana was integrated to visualize feed metrics using Prometheus.

### **12.1 Why Grafana?**

Grafana provides:

* SOC-style dashboards
* Real-time feed monitoring
* IOC trend visualization
* Quick validation of automated pipelines

### **12.2 Data Source: Prometheus**

Metrics retrieved:

* `feed_indicators{feed="circl"}`
* `feed_indicators{feed="botvrij"}`
* `feed_indicators_total`

### **12.3 Created Dashboard Panels**

1. **Total Indicators (Stat Panel)**
2. **CIRCL Indicators (Time-Series)**
3. **Botvrij Indicators (Time-Series)**

### **12.4 Visualization Results**

* CIRCL Indicators: **3**
* Botvrij Indicators: **2**
* Total Indicators: **5**

(Values matched the exporter metrics, confirming the pipeline.)

---

## **📌 13. Results & Analysis**

This project demonstrates:

* Proper IOC management
* Integration of OSINT feeds
* Infrastructure correlation analysis
* Threat attribution using MITRE ATT&CK
* Automation through Python
* Real-time visualization through Grafana
* Fully operational email alerting

It reflects how real SOCs manage and interpret threat intelligence.

---

## **📌 14. Conclusion**

This project successfully implemented a complete **CTI workflow** using MISP.
It covers:

* Event creation
* Tagging and classification
* IOC extraction
* Feed integration
* Enrichment
* Python automation
* Statistical analysis
* Grafana visualization
* Documentation and reporting

The workflow mirrors professional CTI operations and demonstrates a mature understanding of threat intelligence practices.

---
