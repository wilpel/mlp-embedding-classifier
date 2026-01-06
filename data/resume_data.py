"""
Training data for resume similarity detection.

Categories:
- Engineering (Software, DevOps, Data, ML, Mobile, Embedded)
- Marketing (Digital, Brand, Content, Growth, Product Marketing)
- Finance (Investment Banking, Corporate Finance, Risk, Quant, VC)
- Healthcare (Clinical, Administration, Research, Pharma)
- Legal (Corporate, Litigation, IP, Employment, Privacy)
- Sales (Enterprise, SaaS, Account Management)
- Design (Product, UX, Visual, Brand)
- Operations (Supply Chain, Project Management, Business Ops)
"""

ENGINEERING_RESUMES = [
    # Software Engineering
    "Software engineer with 5 years experience in Python, Java, and cloud technologies. Built scalable microservices at tech startups. Strong background in algorithms, data structures, and system design. BS Computer Science from MIT. Led migration of monolithic application to microservices architecture serving 2M daily users.",
    "Full stack developer proficient in React, Node.js, and PostgreSQL. Developed e-commerce platforms handling millions of transactions. Experience with AWS, Docker, and CI/CD pipelines. Passionate about clean code and test-driven development. Reduced page load times by 60% through optimization.",
    "Senior backend engineer specializing in distributed systems and high-performance computing. Led teams at Google and Amazon. Expert in Go, Rust, and Kubernetes. Published research on database optimization. Architected systems handling 1B+ requests per day with 99.99% uptime.",
    "Staff software engineer with 12 years building large-scale systems. Technical lead for platform team at Stripe. Deep expertise in payments infrastructure, API design, and security. Mentored 20+ engineers and established coding standards adopted company-wide.",
    "Principal engineer focused on developer productivity and tooling. Built internal frameworks used by 500+ engineers. Expert in compiler design, static analysis, and IDE tooling. Previously at JetBrains working on IntelliJ platform.",

    # DevOps / SRE
    "DevOps engineer with expertise in infrastructure automation, monitoring, and cloud architecture. Managed production systems serving 10M+ users. Proficient in Terraform, Ansible, and Prometheus. AWS and GCP certified. Reduced deployment time from hours to minutes.",
    "Site reliability engineer at Netflix managing global streaming infrastructure. Expert in chaos engineering, capacity planning, and incident response. Built observability platform processing 10TB logs daily. On-call experience managing critical production systems.",
    "Platform engineer specializing in Kubernetes and service mesh technologies. Migrated 200+ microservices to K8s. Deep knowledge of Istio, Envoy, and container networking. Created self-service platform reducing developer onboarding time by 80%.",
    "Infrastructure engineer with focus on security and compliance. Implemented zero-trust architecture for Fortune 500 company. Expert in HashiCorp stack, network security, and SOC 2 compliance. Automated security scanning in CI/CD pipelines.",
    "Cloud architect designing multi-region, highly available systems on AWS. 8 years experience with cloud migrations and hybrid architectures. Solutions Architect Professional certified. Reduced cloud costs by $2M annually through optimization.",

    # Data Engineering
    "Data engineer experienced in building ETL pipelines and data warehouses. Expert in Spark, Airflow, and Snowflake. Processed petabytes of data for analytics platforms. Strong SQL and Python skills. Built real-time data pipelines with sub-second latency.",
    "Senior data engineer at Uber building data platform infrastructure. Expertise in streaming systems, Kafka, and Flink. Designed data lake architecture supporting 1000+ data scientists. Created data quality framework reducing pipeline failures by 90%.",
    "Analytics engineer bridging data engineering and business intelligence. Expert in dbt, Looker, and modern data stack. Built self-service analytics platform empowering non-technical users. Strong understanding of data modeling and dimensional design.",
    "Big data engineer with experience in Hadoop ecosystem and cloud data platforms. Built recommendation systems processing billions of events. Expert in Scala, Spark, and distributed computing. Optimized job performance reducing costs by 60%.",
    "Data platform engineer focused on real-time analytics and stream processing. Built event-driven architecture handling 5M events/second. Expert in Kafka, ksqlDB, and Elasticsearch. Reduced analytics latency from hours to seconds.",

    # Machine Learning
    "Machine learning engineer with PhD in Computer Science. Built recommendation systems and NLP pipelines at scale. Expert in PyTorch, TensorFlow, and MLOps. Multiple publications in top AI conferences. Deployed models serving 100M+ predictions daily.",
    "Senior ML engineer specializing in computer vision and deep learning. Led autonomous vehicle perception team. Expert in CNNs, object detection, and 3D reconstruction. Published papers at CVPR and ICCV. 15+ patents in computer vision.",
    "Applied scientist at Amazon working on Alexa NLU. Expert in transformers, language models, and conversational AI. Built intent classification systems with 95%+ accuracy. PhD from Stanford in computational linguistics.",
    "MLOps engineer building production ML infrastructure. Expert in feature stores, model serving, and ML pipelines. Implemented A/B testing framework for ML models. Reduced model deployment time from weeks to hours.",
    "Research engineer at DeepMind working on reinforcement learning. Published at NeurIPS and ICML. Expert in game playing AI and multi-agent systems. Strong mathematical foundation in optimization and probability theory.",

    # Mobile Development
    "Mobile developer with 6 years building iOS and Android apps. Led development of apps with 5M+ downloads. Proficient in Swift, Kotlin, and React Native. Strong UI/UX sensibility. Implemented offline-first architecture for travel app.",
    "Senior iOS engineer at Instagram. Expert in Swift, UIKit, and SwiftUI. Built video editing features used by millions. Deep knowledge of Core Animation and Metal for graphics performance. Reduced app launch time by 40%.",
    "Android tech lead at Spotify. Expert in Kotlin, Jetpack Compose, and Android architecture. Led team of 8 engineers building music player experience. Strong focus on accessibility and internationalization.",
    "Cross-platform mobile developer with expertise in Flutter and React Native. Built fintech apps with bank-level security. Experience with biometric authentication and secure data storage. Shipped apps to both App Store and Play Store.",
    "Mobile infrastructure engineer building shared libraries and tooling. Expert in mobile CI/CD, crash reporting, and analytics. Created modular architecture enabling independent team deployment. Reduced build times by 70%.",

    # Embedded Systems
    "Embedded systems engineer with experience in firmware development and IoT devices. Proficient in C, C++, and RTOS. Developed products for automotive and consumer electronics industries. Expert in low-power design and wireless protocols.",
    "Hardware-software engineer at Tesla working on vehicle firmware. Expert in CAN bus, automotive safety standards, and real-time systems. Built diagnostics tools for manufacturing. Strong background in control systems.",
    "IoT engineer building connected device platforms. Expert in BLE, WiFi, and cellular connectivity. Developed end-to-end solutions from firmware to cloud. Experience with FCC certification and hardware testing.",
    "Robotics software engineer at Boston Dynamics. Expert in ROS, motion planning, and sensor fusion. Built autonomous navigation systems for warehouse robots. PhD in robotics from CMU.",
    "FPGA engineer specializing in high-frequency trading systems. Expert in Verilog, timing optimization, and low-latency networking. Built trading systems with sub-microsecond latency. Strong background in digital signal processing.",
]

MARKETING_RESUMES = [
    # Digital Marketing
    "Digital marketing manager with 7 years experience driving growth for B2B SaaS companies. Expert in SEO, PPC, and content marketing. Increased organic traffic 300% and reduced CAC by 40%. MBA from Wharton. Google Ads and Analytics certified.",
    "Performance marketing specialist managing $5M+ annual ad spend. Expert in Google Ads, Facebook Ads, and programmatic buying. Strong analytical skills and data-driven optimization approach. Achieved 3x ROAS improvement.",
    "SEO director with 10 years experience in enterprise search optimization. Built SEO programs for Fortune 500 companies. Expert in technical SEO, content strategy, and link building. Grew organic revenue from $10M to $50M.",
    "Paid social specialist at leading e-commerce brand. Expert in Facebook, Instagram, and TikTok advertising. Created viral campaigns with 100M+ impressions. Strong creative testing and audience targeting skills.",
    "Marketing automation expert implementing Marketo, HubSpot, and Salesforce integrations. Built nurture campaigns with 40% conversion rates. Expert in email marketing, lead scoring, and attribution modeling.",

    # Brand Marketing
    "Brand strategist with background in consumer goods and luxury brands. Led rebranding initiatives for Fortune 500 companies. Strong storytelling and visual design sensibility. Experience with market research and positioning.",
    "Creative director with 15 years in advertising agencies. Led campaigns for Nike, Apple, and Coca-Cola. Expert in brand identity, messaging, and visual design. Multiple Cannes Lions and Effie awards.",
    "Brand manager at Procter & Gamble managing $100M brand portfolio. Expert in consumer insights, positioning, and go-to-market strategy. Launched 5 new products with combined revenue of $50M.",
    "Head of brand at fast-growing DTC startup. Built brand from zero to household name recognition. Expert in brand voice, visual identity, and customer experience. Led team of 12 creative professionals.",
    "Cultural strategist connecting brands with emerging trends. Expert in youth culture, social listening, and influencer partnerships. Advised Fortune 500 companies on cultural relevance strategies.",

    # Content Marketing
    "Content marketing lead with journalism background. Created content strategies driving millions of page views. Expert in SEO writing, email marketing, and thought leadership programs. Built team of 8 writers.",
    "Editorial director building media properties for B2B brands. Launched podcasts with 500K+ downloads. Expert in content strategy, editorial calendars, and multimedia storytelling. Former editor at major publication.",
    "Video content strategist at YouTube creating brand channels. Expert in video SEO, thumbnail optimization, and audience growth. Built channels from zero to 1M+ subscribers. Strong understanding of algorithm.",
    "Content strategist specializing in SaaS documentation and technical content. Built help centers reducing support tickets by 50%. Expert in information architecture and content operations.",
    "Copywriter with 8 years writing for tech brands. Expert in conversion copywriting, landing pages, and email sequences. A/B tested hundreds of variations. Strong understanding of customer psychology.",

    # Growth Marketing
    "Growth marketer specializing in product-led growth and viral loops. Built referral programs generating 50% of new users. Proficient in analytics, A/B testing, and marketing automation tools. MBA from Stanford.",
    "Head of growth at Series B startup. Scaled user base from 10K to 1M in 18 months. Expert in acquisition, activation, and retention strategies. Built growth team of 6 across multiple channels.",
    "Lifecycle marketing manager optimizing customer journey. Built email and push notification programs with 30% engagement rates. Expert in cohort analysis, segmentation, and personalization.",
    "Conversion rate optimization specialist at Booking.com. Ran 500+ A/B tests annually. Expert in experimentation frameworks, statistical analysis, and landing page optimization. Increased conversion by 25%.",
    "Growth engineer building marketing technology infrastructure. Expert in tracking, attribution, and data pipelines. Built internal experimentation platform serving 50+ marketers.",

    # Product Marketing
    "Product marketing manager bridging product and go-to-market teams. Launched 20+ features with successful adoption. Expert in competitive analysis, messaging, and sales enablement. MBA from Kellogg.",
    "PMM director at enterprise software company. Led positioning and messaging for $500M product line. Expert in analyst relations, customer marketing, and product launches. Built team of 8 PMMs.",
    "Technical product marketer for developer tools. Created documentation, tutorials, and developer advocacy programs. Expert in developer community building and technical content. Former software engineer.",
    "Solutions marketing manager creating vertical-specific messaging. Built sales tools and battle cards for 10 industry verticals. Expert in competitive intelligence and customer storytelling.",
    "Customer marketing manager building advocacy programs. Created customer advisory board and reference programs. Expert in case studies, reviews, and community building. Increased NPS by 20 points.",
]

FINANCE_RESUMES = [
    # Investment Banking
    "Investment banker with 8 years at Goldman Sachs and Morgan Stanley. Led M&A transactions totaling $5B+. Expert in financial modeling, valuation, and deal structuring. MBA from Harvard Business School.",
    "Managing director in technology investment banking. Advised on 50+ transactions including IPOs and strategic acquisitions. Deep relationships with tech executives and PE sponsors. $10B+ deal experience.",
    "Healthcare investment banker specializing in biopharma and medical devices. Led cross-border transactions across US, Europe, and Asia. Expert in FDA regulatory landscape and reimbursement dynamics.",
    "Restructuring specialist at Houlihan Lokey. Advised distressed companies and creditor committees. Expert in bankruptcy process, capital structure, and liability management. CFA charterholder.",
    "Vice president in leveraged finance. Structured $20B+ in high-yield bonds and leveraged loans. Expert in credit analysis, covenant negotiation, and syndication. Strong relationships with institutional investors.",

    # Corporate Finance
    "Financial analyst specializing in equity research and portfolio management. CFA charterholder with strong track record of stock picks. Proficient in Bloomberg, FactSet, and advanced Excel modeling.",
    "Corporate finance manager overseeing budgeting, forecasting, and financial planning. Reduced costs 20% through process optimization. Experience with SAP, Oracle Financials, and Hyperion.",
    "FP&A director at Fortune 500 company managing $2B P&L. Built financial planning models and KPI dashboards. Expert in variance analysis, scenario planning, and board reporting.",
    "Treasury manager optimizing cash management and capital structure. Managed $500M investment portfolio and debt refinancing. Expert in FX hedging, interest rate risk, and banking relationships.",
    "Controller at high-growth startup through IPO. Built finance team from 2 to 20. Expert in SEC reporting, SOX compliance, and technical accounting. CPA with Big 4 background.",

    # Private Equity / Venture Capital
    "Private equity associate with experience in leveraged buyouts and growth equity. Evaluated 100+ investment opportunities. Strong due diligence and portfolio management skills. MBA from Wharton.",
    "Venture capital analyst evaluating early-stage startups. Sourced deals leading to 3 successful exits. Strong network in tech ecosystem and pattern recognition for winning companies. Stanford MBA.",
    "Principal at growth equity firm investing $50-200M in software companies. Led 10+ investments with combined value of $2B. Expert in SaaS metrics, market analysis, and value creation.",
    "Operating partner at PE firm driving portfolio company improvements. Former CEO with turnaround experience. Expert in operational efficiency, pricing optimization, and revenue growth.",
    "Fund of funds analyst at endowment. Evaluated hedge funds and PE managers for $10B portfolio. Expert in manager selection, portfolio construction, and alternative investments.",

    # Quantitative Finance
    "Quantitative analyst developing trading algorithms and pricing models. PhD in Financial Engineering. Expert in Python, R, and C++. Published research on derivatives pricing. 15+ years experience.",
    "Systematic trader at hedge fund building equity and futures strategies. Expert in statistical arbitrage, factor models, and execution algorithms. Generated $50M+ annual P&L with Sharpe ratio above 2.",
    "Risk quantitative analyst at major bank. Built VaR models, stress testing frameworks, and counterparty credit models. Expert in Monte Carlo simulation and regulatory capital requirements.",
    "Machine learning researcher in quantitative finance. Applied NLP to alternative data for alpha generation. Expert in deep learning, time series analysis, and feature engineering. PhD from MIT.",
    "Derivatives structurer creating bespoke hedging solutions for corporate clients. Expert in options pricing, volatility modeling, and exotic derivatives. Structured $5B+ in custom products.",

    # Risk / Compliance
    "Risk management professional specializing in market risk and regulatory compliance. Implemented VaR models and stress testing frameworks. Experience with Basel III and Dodd-Frank requirements.",
    "Chief compliance officer at fintech company. Built compliance program from scratch. Expert in BSA/AML, state licensing, and consumer protection. Former banking regulator.",
    "Operational risk manager at global bank. Led RCSA programs and loss event analysis. Expert in control frameworks, key risk indicators, and risk culture. Certified in operational risk.",
    "Credit risk analyst at commercial bank. Built scorecards and loss forecasting models. Expert in probability of default, LGD, and economic capital. CFA with strong quantitative background.",
    "Tax consultant with expertise in corporate tax planning and international taxation. CPA with Big 4 experience. Saved clients $50M+ through tax optimization strategies.",
]

HEALTHCARE_RESUMES = [
    # Clinical
    "Registered nurse with 10 years experience in critical care and emergency medicine. Led nursing teams at major trauma centers. Certifications in ACLS, PALS, and trauma nursing. BSN from Johns Hopkins.",
    "Physician assistant in orthopedic surgery. 8 years experience in joint replacement and sports medicine. Expert in pre and post-operative care. Certified by NCCPA with 100+ continuing education credits.",
    "Nurse practitioner in family medicine. Managed panel of 2000+ patients. Expert in chronic disease management and preventive care. DNP with prescriptive authority in all 50 states.",
    "Physical therapist specializing in sports medicine and orthopedic rehabilitation. Treated professional athletes and post-surgical patients. Doctorate in Physical Therapy from USC.",
    "Clinical pharmacist in oncology at academic medical center. Expert in chemotherapy protocols and supportive care. Board certified oncology pharmacist. Precepted 20+ pharmacy students.",

    # Healthcare Administration
    "Healthcare administrator managing operations for 500-bed hospital. Improved patient satisfaction scores 25% and reduced wait times 40%. MBA in Healthcare Management. Lean Six Sigma certified.",
    "Chief nursing officer at regional health system. Led 2000+ nursing staff across 5 facilities. Expert in Magnet designation, staffing models, and quality metrics. DNP with executive leadership focus.",
    "Revenue cycle director at multi-specialty practice. Reduced AR days from 45 to 28. Expert in billing operations, payer contracting, and denial management. HFMA certified.",
    "Health information manager implementing EHR systems. Led Epic and Cerner deployments across health systems. Bridge between clinical workflows and technology solutions. RHIA certified.",
    "Practice manager at large physician group. Managed $50M annual budget and 100+ staff. Expert in physician compensation, productivity metrics, and regulatory compliance.",

    # Clinical Research
    "Clinical research coordinator managing Phase II and III trials. Experience with FDA regulations and IRB submissions. Strong patient recruitment and data management skills. ACRP certified.",
    "Biostatistician at pharmaceutical company. Designed clinical trials and analyzed efficacy data. Expert in SAS, R, and adaptive trial designs. PhD in Biostatistics from Harvard.",
    "Medical monitor overseeing drug safety in oncology trials. Expert in adverse event management and regulatory reporting. MD with board certification in oncology.",
    "Clinical operations director at CRO managing global trials. Led 50+ studies across 30 countries. Expert in site selection, enrollment strategies, and quality oversight.",
    "Regulatory affairs specialist preparing FDA submissions. Led 10+ successful NDA/BLA filings. Expert in CMC documentation, labeling, and post-marketing requirements.",

    # Healthcare Technology
    "Health informatics specialist implementing EHR systems. Led Epic and Cerner deployments across health systems. Bridge between clinical workflows and technology solutions.",
    "Digital health product manager at telemedicine company. Built virtual care platform serving 1M+ patients. Expert in HIPAA compliance, clinical workflows, and patient engagement.",
    "Healthcare data scientist at payer organization. Built predictive models for readmission and cost. Expert in claims data, risk adjustment, and population health analytics.",
    "Clinical decision support analyst at health system. Implemented order sets and clinical alerts. Expert in evidence-based medicine and workflow optimization.",
    "Telehealth coordinator expanding virtual care programs. Grew program from 100 to 10,000 visits monthly. Expert in video platforms, reimbursement, and provider training.",

    # Pharmaceutical / Medical Devices
    "Pharmaceutical scientist with expertise in drug formulation and delivery systems. 15 patents in controlled release technologies. PhD in Pharmaceutical Sciences.",
    "Medical device sales representative with $3M annual quota achievement. Deep knowledge of surgical equipment and hospital procurement. Built relationships with key opinion leaders.",
    "Clinical specialist at medical device company. Trained surgeons on new implant techniques. Expert in operating room protocols and procedural support. RN with surgical background.",
    "Medical science liaison in immunology. Built relationships with academic researchers and KOLs. Expert in clinical data presentation and medical education. PharmD with residency training.",
    "Quality engineer at medical device manufacturer. Led design controls and validation activities. Expert in FDA QSR, ISO 13485, and risk management. ASQ certified.",
]

LEGAL_RESUMES = [
    # Corporate Law
    "Corporate attorney with 12 years at top law firms. Handled IPOs, mergers, and securities offerings. Expert in corporate governance and compliance. JD from Yale Law School.",
    "M&A partner at AmLaw 50 firm. Led $50B+ in transactions across technology and healthcare. Expert in deal structuring, negotiations, and antitrust considerations.",
    "Securities lawyer advising on public offerings and SEC compliance. Expert in 34 Act reporting, proxy statements, and executive compensation. Former SEC staff attorney.",
    "General counsel at Series D startup. Built legal function from scratch. Expert in venture financing, commercial contracts, and employment law. JD from Stanford.",
    "Private equity counsel at fund and portfolio companies. Expert in fund formation, GP economics, and portfolio company M&A. 10+ years at Kirkland & Ellis.",

    # Litigation
    "Litigation associate specializing in complex commercial disputes. Tried cases in federal and state courts. Strong brief writing and oral advocacy skills. Clerkship with federal judge.",
    "Trial attorney at DOJ with 50+ jury trials. Expert in white collar crime and securities fraud. Moot court champion at law school. 15 years courtroom experience.",
    "Class action defense partner at major firm. Defended Fortune 500 companies in antitrust and securities cases. Expert in MDL procedure and settlement negotiations.",
    "Appellate specialist with arguments before Supreme Court and circuit courts. Expert in constitutional law and statutory interpretation. Former clerk to Justice Kennedy.",
    "E-discovery consultant managing document review for major litigation. Expert in predictive coding, TAR, and litigation technology. JD with information science background.",

    # Intellectual Property
    "Intellectual property lawyer focusing on patents and trade secrets. Protected portfolios for tech companies. PhD in Electrical Engineering before law school.",
    "Patent prosecutor in biotechnology and pharmaceuticals. Drafted 500+ patents with 90% allowance rate. Expert in claim construction and patent term extension. PhD in Chemistry.",
    "Trademark attorney at global brand. Managed 10,000+ trademark portfolio across 100 countries. Expert in brand protection, enforcement, and domain disputes.",
    "IP litigator at trial boutique. Won $500M+ in patent damages. Expert in claim construction, Markman hearings, and PTAB proceedings. Technical background in software.",
    "Technology licensing attorney at research university. Negotiated $100M+ in licensing revenue. Expert in sponsored research, startups, and technology transfer.",

    # Specialized Practice Areas
    "Employment law specialist advising on workplace policies and discrimination cases. Conducted investigations and mediations. Experience with EEOC and state agencies.",
    "Real estate attorney handling commercial transactions and development projects. Negotiated leases for major retail chains. Expert in zoning and land use regulations.",
    "Immigration lawyer helping companies with visa petitions and compliance. Processed 500+ H-1B and green card cases. Fluent in Spanish and Mandarin.",
    "Privacy and data protection counsel advising on GDPR and CCPA compliance. Drafted privacy policies for Fortune 500 companies. CIPP certified.",
    "Criminal defense attorney with trial experience in federal court. Former prosecutor with DOJ. Handled white collar and cybercrime cases. 100+ jury trials.",
]

SALES_RESUMES = [
    # Enterprise Sales
    "Enterprise sales executive at Salesforce with consistent President's Club achievement. Closed $20M+ annual bookings. Expert in complex negotiations and C-suite relationships.",
    "Strategic account director managing Fortune 100 relationships. Grew key account from $5M to $25M annually. Expert in account planning and value selling.",
    "Global sales director at Oracle leading team of 20 reps. Built EMEA region from scratch to $50M revenue. Expert in enterprise software sales cycles.",
    "VP of Sales at growth-stage SaaS company. Scaled team from 5 to 50 reps. Built sales playbook and training programs. Increased win rate from 20% to 35%.",
    "Sales engineer providing technical expertise in complex deals. Expert in product demos, RFP responses, and solution architecture. Background in software engineering.",

    # SaaS Sales
    "Account executive at high-growth SaaS startup. Consistently at 150%+ quota attainment. Expert in MEDDIC, value selling, and multi-threading.",
    "SDR manager building pipeline generation team. Grew team from 5 to 30 SDRs. Created training program reducing ramp time by 50%. Expert in outbound prospecting.",
    "Customer success manager with focus on expansion revenue. Managed $10M book of business with 140% net retention. Expert in health scoring and QBRs.",
    "Sales operations leader building go-to-market infrastructure. Implemented Salesforce, Outreach, and Gong. Expert in forecasting, territory design, and compensation.",
    "Channel sales manager building partner ecosystem. Recruited and enabled 50+ partners generating $20M pipeline. Expert in partner programs and co-selling.",

    # Account Management
    "Key account manager at CPG company managing retail relationships. Grew Walmart business from $50M to $100M. Expert in category management and trade promotion.",
    "Client director at advertising agency managing $30M account. Led integrated campaigns across digital and traditional media. Expert in client relationships and project delivery.",
    "Relationship manager at commercial bank. Managed portfolio of 100 middle-market companies. Expert in credit products, treasury services, and deposit gathering.",
    "Strategic partnerships manager at platform company. Closed deals with strategic partners generating $50M+ revenue. Expert in business development and contract negotiation.",
    "Renewals manager ensuring customer retention for subscription business. Achieved 95%+ renewal rate on $25M book. Expert in risk identification and save strategies.",
]

DESIGN_RESUMES = [
    # Product Design
    "Product designer at Airbnb with 8 years experience. Led design for search and booking experience used by millions. Expert in user research, prototyping, and design systems.",
    "Senior UX designer at Google working on enterprise products. Built design system serving 100+ products. Expert in interaction design, accessibility, and scalability.",
    "Design lead at fintech startup. Designed mobile banking app with 4.9 star rating. Expert in financial UX, regulatory requirements, and trust design. Portfolio at example.com.",
    "Principal designer at Meta leading messaging experiences. Managed team of 8 designers. Expert in social design patterns, privacy UX, and global design.",
    "Staff designer at Figma building design tools. Expert in design systems, plugin development, and community building. Former industrial designer bringing physical product perspective.",

    # UX Research
    "UX researcher at Microsoft with quantitative and qualitative expertise. Led research programs informing $1B product decisions. Expert in usability testing, surveys, and analytics.",
    "Research manager at Spotify building insights team. Established research practice serving 10 product teams. Expert in research operations and stakeholder management.",
    "Senior researcher specializing in accessibility and inclusive design. Advocated for users with disabilities across product portfolio. Expert in assistive technology and WCAG compliance.",
    "Mixed methods researcher combining behavioral data with qualitative insights. Built experimentation culture at growth startup. PhD in Human-Computer Interaction from CMU.",
    "Design research consultant advising Fortune 500 on customer experience. Led journey mapping and service design engagements. Expert in workshop facilitation and synthesis.",

    # Visual / Brand Design
    "Visual designer creating brand identities for tech companies. Built design systems for 20+ startups. Expert in typography, color theory, and motion design. RISD graduate.",
    "Brand designer at creative agency working with global brands. Led rebranding for Fortune 500 client. Expert in brand strategy, visual identity, and guidelines development.",
    "Creative director at DTC brand building in-house creative team. Produced campaigns across social, email, and paid media. Expert in art direction and creative strategy.",
    "Motion designer at animation studio creating content for tech brands. Expert in After Effects, Cinema 4D, and procedural animation. Strong illustration background.",
    "Design systems lead at enterprise software company. Built component library serving 50+ products. Expert in tokens, documentation, and cross-platform consistency.",
]

OPERATIONS_RESUMES = [
    # Supply Chain
    "Supply chain director at Fortune 500 retailer. Managed $2B inventory across 500 stores. Reduced stockouts 40% while cutting inventory costs 15%. APICS certified.",
    "Procurement manager at manufacturing company. Negotiated $100M+ in supplier contracts. Expert in strategic sourcing, supplier development, and cost reduction.",
    "Logistics manager at e-commerce company. Built fulfillment network serving next-day delivery. Expert in warehouse operations, carrier management, and last mile.",
    "Demand planning analyst at CPG company. Built forecasting models reducing forecast error by 30%. Expert in S&OP, statistical forecasting, and inventory optimization.",
    "Supply chain consultant at McKinsey. Led transformation projects for manufacturing and retail clients. Expert in network design, inventory strategy, and digital supply chain.",

    # Project / Program Management
    "Technical program manager at Amazon leading cross-functional initiatives. Delivered programs involving 10+ teams and $50M investment. PMP and Scrum Master certified.",
    "Senior project manager at construction company. Managed $100M commercial projects. Expert in scheduling, cost control, and subcontractor management. PE licensed.",
    "Product operations lead at tech company. Built processes enabling 10x product team growth. Expert in roadmap planning, release management, and cross-functional coordination.",
    "Transformation program director leading enterprise initiatives. Managed $500M digital transformation. Expert in change management, governance, and benefit realization.",
    "Agile coach at financial services company. Trained 500+ employees on agile methodologies. Expert in Scrum, SAFe, and organizational change. CST certified.",

    # Business Operations
    "Chief of staff to CEO at growth-stage startup. Led strategic initiatives across company. Expert in executive communication, board relations, and special projects.",
    "Business operations manager at sales organization. Built analytics and enablement functions. Improved quota attainment 25% through process optimization.",
    "Strategy and operations lead at tech company. Built planning processes and OKR frameworks. Expert in resource allocation, metrics, and executive reporting.",
    "Operational excellence director at manufacturing company. Led lean transformation across 10 plants. Reduced waste 30% and improved productivity 20%. Six Sigma Black Belt.",
    "Head of business operations at marketplace startup. Built trust and safety, customer support, and vendor operations. Scaled operations from 10 to 200 team members.",
]


# All categories for easy access
RESUME_CATEGORIES = {
    "engineering": ENGINEERING_RESUMES,
    "marketing": MARKETING_RESUMES,
    "finance": FINANCE_RESUMES,
    "healthcare": HEALTHCARE_RESUMES,
    "legal": LEGAL_RESUMES,
    "sales": SALES_RESUMES,
    "design": DESIGN_RESUMES,
    "operations": OPERATIONS_RESUMES,
}


def get_all_resumes() -> dict[str, list[str]]:
    """Returns all resumes organized by category."""
    return RESUME_CATEGORIES


def get_stats() -> dict:
    """Returns dataset statistics."""
    total = sum(len(resumes) for resumes in RESUME_CATEGORIES.values())
    return {
        "total_resumes": total,
        "categories": len(RESUME_CATEGORIES),
        "resumes_per_category": {k: len(v) for k, v in RESUME_CATEGORIES.items()},
    }
