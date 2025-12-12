# **Cyber Threat Intelligence Analysis of Lazarus Group Using MISP**

A full CTI lifecycle implementation using **MISP**, OSINT feeds, enrichment, automation, visualization, and alerting.
This project simulates a real-world investigation of the **Lazarus Group**, a well-known state-sponsored APT involved in ransomware, banking theft, crypto attacks, and cyber espionage. 

---

## **1. Project Overview**

This project demonstrates an end-to-end Cyber Threat Intelligence (CTI) workflow using the **Malware Information Sharing Platform (MISP)**.
It includes:

* Event creation & threat actor profiling
* IOC extraction
* Tagging & classification
* OSINT feed integration
* Python automation (feed parsing + statistics)
* Email alerting via SMTP
* MITRE ATT&CK mapping
* IP ASN enrichment
* Grafana dashboard for live IOC visualization

The target threat actor is the **Lazarus Group**. 

---

## **2. Tools & Environment**

**Platforms & Technologies Used:** 

* **Kali Linux**
* **Docker** (MISP deployed via containers)
* **MISP**
* **Python** (feed automation scripts)
* **Prometheus + Grafana** for visualization
* **SWAKS** for SMTP testing

The environment simulates a real-life **Security Operations Center (SOC)** architecture.

---

## **3. Threat Actor Overview — Lazarus Group**

Lazarus is a **state-sponsored APT** known for:

* Ransomware campaigns
* Cryptocurrency theft
* Banking fraud
* Cyber espionage
* Large-scale destructive attacks


---

## **4. Event Creation in MISP**

A new MISP event was created to store all intelligence about Lazarus:

* **Event Name:** *Lazarus Group – Financial & Ransomware Campaigns*
* **Threat Level:** High
* **Analysis:** Initial
* **Distribution:** Organization Only


This event is the central container for all IOCs, enrichment, and OSINT data.

---

## **5. Tagging & Classification**

Three key tags were applied: 

* `threat-actor:lazarus-group`
* `tlp:red`
* `attack-type:ransomware`

These tags enforce **classification**, **sensitivity**, and **threat categorization**.

---

## **6. Indicators of Compromise (IOCs)**

A total of **five** IOCs were added to the event: 

| IOC Type     | Value                                                            |
| ------------ | ---------------------------------------------------------------- |
| IP Address   | 185.172.110.41                                                   |
| IP Address   | 45.142.215.12                                                    |
| Domain       | update-secure-login.com                                          |
| Malware Name | Ryuk                                                             |
| SHA-256 Hash | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

These represent attacker infrastructure & malware components.

---

## **7. OSINT Feed Integration**

Enabled Feeds:

* **CIRCL OSINT Feed**
* **Botvrij OSINT Feed**


Due to worker issues, feeds were synchronized manually using:

```bash
./app/Console/cake Server fetchFeed 1 all
```

Warnings indicated duplicates — confirming **real feed data ingestion**.

---

## **8. Python Feed Parsing & Unification**

Two Python scripts were created:

1. **`feed_parser.py`** — Fetches OSINT feeds and generates a unified file:

   * Output: `unified_feeds.json`
2. **`feed_stats.py`** — Produces IOC statistics from unified feeds.


**Statistics:**

* CIRCL: 20 indicators
* Botvrij: 20 indicators
* **Total:** 40

---

## **9. Email Alert System (SMTP)**

MISP was configured to send alerts using **Gmail SMTP over TLS**.
Testing done with **SWAKS** validated:

* TLS handshake
* Authentication success
* Email delivery to analyst inbox


Examples shown in the PDF confirm working alerting.

---

## **10. MITRE ATT&CK Mapping**

Four ATT&CK techniques were added to the event: 

1. **Command Shell Execution**
2. **T1059.003 – Windows Command Shell**
3. **Credentials from Password Stores (Web Browsers)**
4. **SQL Stored Procedures**

Each technique aligns with known Lazarus behaviour in real intrusions.

---

## **11. ASN Enrichment (ipasn Module)**

IOC enriched: **185.172.110.41**

Enrichment added: 

* Last-seen timestamps
* ASN number
* Announced subnet
* Automatic ASN objects (2 versions)

This adds **context**, attribution clues, and helps track attacker infrastructure.

---

## **12. Grafana Visualization of OSINT Feeds**

A full monitoring stack was deployed:

* **Python exporter → Prometheus → Grafana Dashboard**


Grafana displays:

* Total IOC count
* CIRCL feed indicators (time-series)
* Botvrij indicators (time-series)

**Example results:**

* CIRCL: 3
* Botvrij: 2
* Total: 5

These values matched Prometheus metrics precisely.

---

## **13. Results & Analysis**

The project demonstrates:

* Reuse of attacker infrastructure
* Effective tagging & classification
* Correlation between local IOCs and OSINT feeds
* Improved attribution through enrichment
* Real-time visualization of CTI metrics


---

## **14. Conclusion**

This project successfully implements a **complete CTI lifecycle** using MISP:

* Event creation
* IOC extraction & enrichment
* Feed integration
* Automation using Python
* Statistics & data unification
* Email alerting
* ATT&CK mapping
* Grafana visualization

It represents a professional-grade simulation of real SOC threat intelligence workflows.


---

## **15. Project Files**

* `feed_parser.py`
* `feed_stats.py`
* `unified_feeds.json`
* `README.md` (this file)


---

## **16. Authors**

* Mahmoud Elmasry
* **Sayed Helmy**
* Eyad Mazhar
* Mostafa Hatem
* Mohamed Samy


