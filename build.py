#!/usr/bin/env python3
"""Builds the BESSA static site: one template, seven pages."""
import os, datetime

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://bessa.co.za"
JOIN = "join.html"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About & IFMBE"),
    ("membership.html", "Membership"),
    ("sabec-2027.html", "SABEC 2027"),
    ("events.html", "Events & Groups"),
    ("contact.html", "Contact"),
]

def head(title, desc, path, extra=""):
    full = "BESSA — Biomedical Engineering Society of South Africa" if path == "index.html" else f"{title} · BESSA"
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if path=='index.html' else path}">
<meta property="og:site_name" content="BESSA">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{'' if path=='index.html' else path}">
<meta property="og:image" content="{SITE}/assets/bessa-logo.jpg">
<meta name="theme-color" content="#141414">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="assets/styles.css">
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(path):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="BESSA home">
      <img src="assets/bessa-logo.jpg" alt="BESSA logo" width="85" height="48">
      <span>BESSA<small>Member society of the IFMBE</small></span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn" href="{JOIN}">Join BESSA</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOTER = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="logos"><img class="bessa" src="assets/bessa-logo.jpg" alt="BESSA"><img src="assets/ifmbe-logo.png" alt="IFMBE"></div>
      <p><strong style="color:#fff">Biomedical Engineering Society of South Africa</strong><br>The South African member society of the International Federation for Medical and Biological Engineering (IFMBE), established 1978.</p>
    </div>
    <div>
      <h4>Secretariat</h4>
      <p>Biomedical Engineering Research Centre<br>Level 7 Anatomy Building, UCT Medical School<br>Anzio Road, Observatory, Cape Town 7925<br>South Africa</p>
      <p><a href="mailto:BESSA@uct.ac.za">BESSA@uct.ac.za</a><br><a href="https://x.com/BME_ZA" rel="noopener">X: @BME_ZA</a></p>
    </div>
    <div>
      <h4>Quick links</h4>
      <ul>
        <li><a href="join.html">Apply for membership</a></li>
        <li><a href="sabec-2027.html">SABEC 2027</a></li>
        <li><a href="membership.html">Categories and fees</a></li>
        <li><a href="about.html#governance">Constitution and governance</a></li>
        <li><a href="https://ifmbe.org" rel="noopener">IFMBE</a></li>
        <li><a href="https://sabec.org.za" rel="noopener">sabec.org.za</a></li>
      </ul>
    </div>
    <div class="legal">© <span id="year">2026</span> Biomedical Engineering Society of South Africa. South African member society of the IFMBE. Personal information is processed under POPIA for membership purposes only.</div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------- pages
HOME = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <div class="logos"><img class="bessa" src="assets/bessa-logo.jpg" alt="BESSA — Biomedical Engineering Society of South Africa"><img src="assets/ifmbe-logo.png" alt="IFMBE — International Federation for Medical and Biological Engineering"></div>
      <div class="strip"><b>SABEC 2027</b> 11–12 March 2027, Cape Town · BESSA members register at reduced rates</div>
      <h1>Engineering better health for South Africa.</h1>
      <p class="lead">BESSA is the South African member society of the International Federation for Medical and Biological Engineering (IFMBE). Established in 1978, we unite biomedical, clinical and medical engineers across universities, the health system, industry, regulators and government.</p>
      <div class="btn-row">
        <a class="btn" href="{JOIN}">Join BESSA</a>
        <a class="btn outline-light" href="sabec-2027.html">SABEC 2027</a>
        <a class="btn outline-light" href="membership.html">Membership</a>
      </div>
    </div>
    <aside>
      <h3>Why join</h3>
      <div class="stat">20%<small>SABEC registration discount for members</small></div>
      <div class="stat" style="margin-top:18px">R750<small>indicative Member fee for 2027, less than the SABEC saving</small></div>
      <div class="stat" style="margin-top:18px">1959<small>IFMBE founded; BESSA is its South African member society</small></div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">What we do</p>
    <h2>Six goals, aligned with the IFMBE Strategic Plan</h2>
    <div class="grid three" style="margin-top:26px">
      <div class="card"><span class="num">01</span><h3>Represent</h3><p>The voice of biomedical and clinical engineering nationally, and South Africa's voice in the IFMBE.</p></div>
      <div class="card"><span class="num">02</span><h3>Advance knowledge</h3><p>Conferences, webinars, publications and the Southern Africa Biomedical Engineering Conference (SABEC).</p></div>
      <div class="card"><span class="num">03</span><h3>Develop the profession</h3><p>Education, accreditation and professional recognition of biomedical and clinical engineers, working with the Engineering Council of South Africa (ECSA) and universities.</p></div>
      <div class="card"><span class="num">04</span><h3>Collaborate</h3><p>Bridges between academia, hospitals, industry, SAHPRA, the Department of Science, Technology and Innovation and the health system.</p></div>
      <div class="card"><span class="num">05</span><h3>Guide policy and standards</h3><p>Position papers and guidelines on professional practice, education, ethics and health technology.</p></div>
      <div class="card"><span class="num">06</span><h3>Build a sustainable society</h3><p>Transparent governance, a growing membership and a constitution ready for non-profit registration.</p></div>
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <p class="eyebrow">Membership</p>
    <h2>Why join BESSA</h2>
    <div class="grid three" style="margin-top:26px">
      <div class="card"><h3>A national network</h3><p>Biomedical and clinical engineers, clinicians, industry and regulators across South Africa, with regional representatives and divisions launching in 2027.</p></div>
      <div class="card"><h3>IFMBE member benefits</h3><p>Reduced fees at IFMBE conferences including the World Congress, eligibility for IFMBE awards and working groups, and representation at the IFMBE General Assembly.</p></div>
      <div class="card dark"><h3>Reduced SABEC fees</h3><p>Members pay 20% less for SABEC 2027: a saving of R1,625 as a delegate or R875 as a student at early-bird rates. Indicative 2027 fees from R375 (students) and R750 (members), to be confirmed by Council.</p></div>
    </div>
    <div class="btn-row"><a class="btn" href="membership.html">See categories and fees</a><a class="btn ghost" href="{JOIN}">Apply online</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap grid two" style="align-items:center">
    <div>
      <p class="eyebrow">Flagship conference</p>
      <h2>SABEC 2027 — Biomedical Engineering Without Borders</h2>
      <p>The Southern Africa Biomedical Engineering Conference, co-hosted by BESSA and UCT MedTech and endorsed by the IFMBE, takes place on 11–12 March 2027 at the UCT Graduate School of Business, Breakwater Campus, V&amp;A Waterfront, Cape Town. Ten tracks, a Young Investigator Competition and student scholarships.</p>
      <p>Early-bird registration closes <strong>15 January 2027</strong>. BESSA members register at the member rate.</p>
      <div class="btn-row"><a class="btn" href="sabec-2027.html">Programme, fees and key dates</a><a class="btn ghost" href="https://www.formdesk.com/millennium/SABEC2027" rel="noopener">Register now</a></div>
    </div>
    <div class="card dark">
      <h3>Member saving at SABEC 2027</h3>
      <ul class="clean" style="color:#E8ECE6">
        <li>Delegate, early bird: <strong>R6,500</strong> member vs R8,125 non-member</li>
        <li>Student, early bird: <strong>R3,500</strong> member vs R4,375 non-member</li>
        <li>Registration closes 28 February 2027</li>
      </ul>
    </div>
  </div>
</section>
"""

ABOUT = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1>About BESSA</h1>
  <p class="lead">Established 1978, BESSA is South Africa's professional home for biomedical engineering, and the country's member society in the International Federation for Medical and Biological Engineering.</p>
</div></section>

<section class="section">
  <div class="wrap grid two">
    <div>
      <h2>Our history and mission</h2>
      <p>BESSA grew out of the country's first academic biomedical engineering programme, founded at the UCT Medical School in 1972, and is housed today at the Biomedical Engineering Research Centre (BMERC) at the University of Cape Town. Through the IFMBE it is part of the International Union for Physical and Engineering Sciences in Medicine (IUPESM).</p>
      <div class="callout"><strong>Mission.</strong> To encourage, support, represent and unify the biomedical engineering community of South Africa, and to advance the research, development, application and management of engineering and technology in medicine and biology for health and quality of life.</div>
    </div>
    <div>
      <h2>Research and innovation focus</h2>
      <ul class="ticks">
        <li><strong>Frugal biodesign and medical devices:</strong> affordable, accessible devices designed for Africa's needs.</li>
        <li><strong>Digital health and AI:</strong> technology that improves care delivery in South African communities.</li>
        <li><strong>Clinical engineering and health infrastructure:</strong> sustainable health technology management for hospitals and clinics.</li>
        <li><strong>Local manufacturing and regulatory capacity:</strong> quality systems (ISO 13485), SAHPRA readiness and the South African MedTech Master Plan.</li>
        <li><strong>Publications:</strong> supporting members to publish in national and international journals and the IFMBE Proceedings.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section white" id="governance">
  <div class="wrap">
    <p class="eyebrow">Governance</p>
    <h2>Leadership, elections and governance</h2>
    <div class="grid two" style="margin-top:22px">
      <div class="card"><h3>President</h3><p><strong>Prof Sudesh Sivarasu</strong><br>Professor and Head of Biomedical Engineering, University of Cape Town; DSTI/NRF SARChI Chair in Biomedical Engineering and Innovation; member of the IFMBE Administrative Council; Co-Chair of the IFMBE Low- and Middle-Income Countries Working Group.</p></div>
      <div class="card"><h3>Secretary-General and IFMBE Delegate</h3><p><strong>Mr Mladen Poluta</strong><br>Former Director of Health Technology; President, Global Clinical Engineering Alliance (GCEA).</p></div>
    </div>
    <div class="grid two" style="margin-top:22px">
      <div>
        <h3>Council positions open at the 2027 elections</h3>
        <p>Vice-President; Treasurer; Communications Officer; Membership Secretary; Regional Representatives (Western Cape, Gauteng, KwaZulu-Natal, Eastern Cape and other provinces); Student and Early-Career Representative; Industry Representative. Nominations open <em>[date to be confirmed]</em>. Officers serve three-year terms matched to the IFMBE cycle; voting members may nominate and stand.</p>
      </div>
      <div>
        <h3>Constitution</h3>
        <p>BESSA is governed by its Constitution and Membership Rules (2026 revision), drafted for registration as a non-profit organisation under the Nonprofit Organisations Act and aligned with the IFMBE Constitution. The Annual General Meeting is held each year, ordinarily alongside SABEC. The Constitution and Membership Rules are available from the Secretariat at <a href="mailto:BESSA@uct.ac.za">BESSA@uct.ac.za</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section dark" id="ifmbe">
  <div class="wrap">
    <div class="grid two" style="align-items:start">
      <div>
        <p class="eyebrow">International connection</p>
        <h2>Part of the IFMBE family</h2>
        <p>The IFMBE, founded in Paris in 1959, is the global federation of national and transnational societies in medical and biological engineering. It is a non-governmental organisation in official relations with the World Health Organization and the United Nations, and with the IOMP forms the International Union for Physical and Engineering Sciences in Medicine (IUPESM). BESSA is its member society for South Africa.</p>
        <h3>Through the IFMBE</h3>
        <ul class="ticks">
          <li>the triennial World Congress on Medical Physics and Biomedical Engineering</li>
          <li>the flagship journal Medical &amp; Biological Engineering &amp; Computing (MBEC)</li>
          <li>the IFMBE Proceedings series and IFMBE News</li>
          <li>the Clinical Engineering Division and the Health Technology Assessment Division</li>
          <li>Working Groups including the Low- and Middle-Income Countries (LMIC) Working Group</li>
          <li>the Council of Societies</li>
        </ul>
        <p><a href="https://ifmbe.org" rel="noopener">ifmbe.org</a></p>
      </div>
      <div>
        <div style="background:#fff;border-radius:12px;padding:16px;display:inline-block;margin-bottom:18px"><img src="assets/ifmbe-logo.png" alt="IFMBE logo" width="150" height="134"></div>
        <h3>What IFMBE membership means for every BESSA member</h3>
        <ol class="steps" style="color:#E8ECE6">
          <li>Reduced registration at IFMBE-endorsed conferences including the World Congress</li>
          <li>Eligibility for IFMBE awards, fellowships and early-career programmes</li>
          <li>Participation in IFMBE Divisions and Working Groups</li>
          <li>Reduced subscription to MBEC</li>
          <li>IFMBE News and calls for papers</li>
          <li>Representation at the IFMBE General Assembly through BESSA's delegates</li>
        </ol>
        <div class="callout" style="background:#1E221E;color:#E8ECE6;margin-top:22px"><strong style="color:#fff">BESSA in the IFMBE.</strong> BESSA's President, Prof Sudesh Sivarasu, serves on the IFMBE Administrative Council and co-chairs the IFMBE LMIC Working Group. BESSA's IFMBE delegate is Mr Mladen Poluta. BESSA circulates IFMBE calls for papers, elections and notices to its members and submits an annual membership return to the Federation.</div>
      </div>
    </div>
  </div>
</section>
"""

MEMBERSHIP = f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Membership</p>
  <h1>Seven categories, one application form</h1>
  <p class="lead">Membership is open to anyone who works, studies or has a professional interest in biomedical, clinical or medical engineering in South Africa, and to organisations active in health technology.</p>
  <div class="btn-row"><a class="btn" href="{JOIN}">Apply for membership</a></div>
</div></section>

<section class="section">
  <div class="wrap">
    <h2>Categories</h2>
    <div class="table-wrap" style="margin-top:18px">
      <table>
        <thead><tr><th>Category</th><th>Post-nominal</th><th>Who it is for</th><th>Votes</th></tr></thead>
        <tbody>
          <tr><td><strong>Fellow</strong></td><td>FBESSA</td><td>Distinguished contribution; by nomination</td><td>Yes</td></tr>
          <tr><td><strong>Member</strong></td><td>MBESSA</td><td>Relevant degree plus 2+ years in biomedical engineering, or 5 years' experience</td><td>Yes</td></tr>
          <tr><td><strong>Early Career</strong></td><td>ECBESSA</td><td>Within 5 years of highest qualification</td><td>Yes</td></tr>
          <tr><td><strong>Associate</strong></td><td>AMBESSA</td><td>Clinicians, scientists, regulators and managers working with health technology</td><td>No</td></tr>
          <tr><td><strong>Student</strong></td><td>SBESSA</td><td>Registered at a recognised institution in a relevant programme</td><td>No</td></tr>
          <tr><td><strong>Affiliate</strong></td><td>Organisational</td><td>Companies, hospitals, departments, NGOs and agencies; one named representative</td><td>No</td></tr>
          <tr><td><strong>Honorary</strong></td><td>—</td><td>Exceptional service; by invitation</td><td>No</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap grid two">
    <div class="card tint">
      <h3>Benefits</h3>
      <ul class="ticks">
        <li><strong>Reduced SABEC registration fees:</strong> BESSA members pay 20% less, saving R1,625 as a delegate or R875 as a student at early-bird rates for SABEC 2027</li>
        <li>A national professional network</li>
        <li>Full IFMBE member benefits</li>
        <li>Webinars and workshops</li>
        <li>Mentorship for students and early-career members</li>
        <li>Eligibility for BESSA awards and Fellowship</li>
        <li>A voice in accreditation, regulation and policy</li>
        <li>The BESSA newsletter</li>
      </ul>
    </div>
    <div class="card dark">
      <h3>Indicative annual fees for 2027</h3>
      <p style="color:#B9C3B4;font-size:14px;margin-top:-6px">To be confirmed by Council</p>
      <ul class="clean" style="color:#E8ECE6">
        <li>Member <strong>R750</strong></li>
        <li>Early Career <strong>R500</strong></li>
        <li>Associate <strong>R560</strong></li>
        <li>Student <strong>R375</strong></li>
        <li>Affiliate <strong>R3,000</strong> (small) · <strong>R7,500</strong> (medium) · <strong>R15,000</strong> (large)</li>
        <li>Fellows and Honorary Members pay no dues</li>
      </ul>
      <p style="margin-top:14px;color:#B9C3B4">Fees are invoiced after approval; nothing is payable at application.</p>
    </div>
  </div>
  <div class="wrap"><div class="callout"><strong>A BESSA membership at R750 costs less than the SABEC member discount.</strong> Join before 15 January 2027 to register at the early-bird member rate.</div></div>
</section>

<section class="section">
  <div class="wrap grid two" style="align-items:start">
    <div>
      <h2>How to apply</h2>
      <ol class="steps">
        <li><strong>Apply online</strong> (about eight minutes). You receive a reference number immediately.</li>
        <li>The <strong>Membership Secretary acknowledges</strong> within five working days and confirms your category within ten.</li>
        <li>The <strong>Membership Committee decides</strong> at its next monthly meeting; you receive an approval letter and invoice.</li>
        <li><strong>Membership starts when the fee is received.</strong> You then get your membership number, welcome pack and group invitations.</li>
      </ol>
      <div class="btn-row"><a class="btn" href="{JOIN}">Apply for membership</a></div>
    </div>
    <div class="card">
      <h3>Questions</h3>
      <p>Write to <a href="mailto:BESSA@uct.ac.za">BESSA@uct.ac.za</a>. Fellows and Honorary Members are elected by nomination, not by application; ask the Secretariat for the nomination form.</p>
      <p>Organisations wishing to join as Affiliates use the same form and name one representative.</p>
    </div>
  </div>
</section>
"""

SABEC = f"""
<section class="hero compact" style="padding-block:48px 56px">
  <div class="wrap">
    <div>
      <p class="eyebrow">BESSA's flagship conference</p>
      <h1>SABEC 2027 — Southern Africa Biomedical Engineering Conference</h1>
      <p class="lead">11–12 March 2027 · UCT Graduate School of Business, Breakwater Campus, V&amp;A Waterfront, Cape Town. Theme: "Biomedical Engineering Without Borders: Bridging Innovation and Access in Africa".</p>
      <p style="color:#D5DBD2">SABEC is BESSA's flagship scientific meeting, co-hosted with UCT MedTech and endorsed by the IFMBE. It brings together researchers, clinical engineers, clinicians, industry, regulators and students from across the region, with a Young Investigator Competition and up to ten scholarships for Master's and PhD students with accepted papers.</p>
      <div class="btn-row">
        <a class="btn" href="https://www.formdesk.com/millennium/SABEC2027" rel="noopener">Register for SABEC 2027</a>
        <a class="btn outline-light" href="https://sabec.org.za/registration/" rel="noopener">Registration information</a>
        <a class="btn outline-light" href="https://sabec.org.za" rel="noopener">SABEC website</a>
      </div>
    </div>
    <aside>
      <h3>BESSA members save on every SABEC ticket</h3>
      <p>The SABEC member rate is 20% below the non-member rate. At early-bird prices a BESSA member saves <strong>R1,625</strong> as a delegate and <strong>R875</strong> as a student, more than the proposed annual BESSA membership fee.</p>
      <p>Not yet a member? Join BESSA before you register to qualify.</p>
      <a class="btn" href="{JOIN}">Join BESSA</a>
    </aside>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Registration fees (ZAR, per person)</h2>
    <div class="table-wrap" style="margin-top:18px">
      <table>
        <thead><tr><th>Registration period</th><th class="num">BESSA member</th><th class="num">Non-member</th><th class="num">Member saving</th></tr></thead>
        <tbody>
          <tr><td>Delegate, early bird (15 Nov 2026 – 15 Jan 2027)</td><td class="num">R6,500</td><td class="num">R8,125</td><td class="num"><span class="save">R1,625</span></td></tr>
          <tr><td>Delegate, standard (16 Jan – 1 Feb 2027)</td><td class="num">R7,000</td><td class="num">R8,750</td><td class="num"><span class="save">R1,750</span></td></tr>
          <tr><td>Delegate, late (2 – 28 Feb 2027)</td><td class="num">R7,500</td><td class="num">R9,375</td><td class="num"><span class="save">R1,875</span></td></tr>
          <tr><td>Student, early bird (15 Nov 2026 – 15 Jan 2027)</td><td class="num">R3,500</td><td class="num">R4,375</td><td class="num"><span class="save">R875</span></td></tr>
          <tr><td>Student, standard (16 Jan – 1 Feb 2027)</td><td class="num">R4,000</td><td class="num">R5,000</td><td class="num"><span class="save">R1,000</span></td></tr>
          <tr><td>Student, late (2 – 28 Feb 2027)</td><td class="num">R4,500</td><td class="num">R5,625</td><td class="num"><span class="save">R1,125</span></td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:14.5px;color:var(--muted);margin-top:12px">Member rates apply to current BESSA members, and are extended to members of other IFMBE-affiliated societies and to staff and students of SABEC's founding partner universities. Student rates require a student card and proof of registration. Registration includes all scientific sessions, conference materials, welcome reception, coffee breaks and lunches, the conference dinner and a certificate of attendance. Fees as published on <a href="https://sabec.org.za/registration/" rel="noopener">sabec.org.za</a>.</p>
  </div>
</section>

<section class="section white">
  <div class="wrap grid two" style="align-items:start">
    <div>
      <h2>Key dates</h2>
      <ul class="clean">
        <li><strong>30 November 2026</strong> — first notification to authors</li>
        <li><strong>15 January 2027</strong> — early-bird registration deadline</li>
        <li><strong>1 February 2027</strong> — author registration deadline</li>
        <li><strong>28 February 2027</strong> — final paper submission; registration closes</li>
        <li><strong>1 March 2027</strong> — final notification to authors</li>
        <li><strong>11–12 March 2027</strong> — conference</li>
      </ul>
    </div>
    <div>
      <h2>Ten tracks</h2>
      <ol class="steps">
        <li>Diagnostics, Imaging and Biomedical Signals</li>
        <li>Biomaterials, Regenerative Medicine and Therapeutics</li>
        <li>Biomechanics, Rehabilitation and Assistive Technologies</li>
        <li>Medical Devices, Robotics and Advanced Manufacturing</li>
        <li>Artificial Intelligence, Data Science and Digital Health</li>
        <li>Clinical Engineering and Health Technology Management</li>
        <li>Appropriate Health Technologies</li>
        <li>Planetary Health and Sustainable Healthcare Technologies</li>
        <li>Regulation, Translation and Entrepreneurship</li>
        <li>BME Education, Ethics and Society</li>
      </ol>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>More on sabec.org.za</h2>
    <div class="grid four" style="margin-top:18px">
      <a class="card" href="https://sabec.org.za/authors/" rel="noopener"><h4>Author guidelines</h4></a>
      <a class="card" href="https://sabec.org.za/special_sessions/" rel="noopener"><h4>Special sessions</h4></a>
      <a class="card" href="https://sabec.org.za/poster_abstracts_submission/" rel="noopener"><h4>Late-breaking poster abstracts</h4></a>
      <a class="card" href="https://sabec.org.za/sabec-2027-challenge/" rel="noopener"><h4>SABEC 2027 Challenge</h4></a>
      <a class="card" href="https://sabec.org.za/sponsorship-opportunities/" rel="noopener"><h4>Sponsorship</h4></a>
      <a class="card" href="https://sabec.org.za/travel-information/" rel="noopener"><h4>Travel information</h4></a>
      <a class="card" href="https://sabec.org.za/invitation-letter-request/" rel="noopener"><h4>Invitation letters</h4></a>
      <a class="card" href="mailto:sabec@uct.ac.za"><h4>Enquiries: sabec@uct.ac.za</h4></a>
    </div>
  </div>
</section>
"""

EVENTS = f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Events and groups</p>
  <h1>Events, divisions and working groups</h1>
  <p class="lead">Where BESSA members meet, and the groups that connect them to their counterparts in the IFMBE.</p>
</div></section>

<section class="section">
  <div class="wrap">
    <div class="card dark" style="margin-bottom:22px">
      <p class="eyebrow">11–12 March 2027 · Cape Town</p>
      <h2 style="color:#fff">SABEC 2027</h2>
      <p>BESSA's flagship conference, co-hosted with UCT MedTech and endorsed by the IFMBE. Early-bird registration closes 15 January 2027; BESSA members register at reduced rates.</p>
      <div class="btn-row"><a class="btn light" href="sabec-2027.html">SABEC details and fees</a><a class="btn outline-light" href="https://sabec.org.za" rel="noopener">sabec.org.za</a></div>
    </div>
    <div class="grid two">
      <div class="card"><h3>BESSA Annual General Meeting</h3><p>Held alongside SABEC 2027 <em>[to be confirmed]</em>. Notice, agenda and nominations are sent to members at least 21 days in advance.</p></div>
      <div class="card"><h3>Through the year</h3><p><strong>IFMBE calendar</strong> — BESSA circulates IFMBE calls for papers and notices to members, including the World Congress on Medical Physics and Biomedical Engineering and IFMBE regional conferences.</p><p>Webinars with local and international speakers, practical workshops, regional networking and STEM outreach promoting careers in biomedical engineering.</p></div>
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <p class="eyebrow">Launching in 2027</p>
    <h2>Divisions and working groups</h2>
    <p class="lead">Mirroring the IFMBE structure so that members connect directly to their international counterparts. Members choose their groups on the application form.</p>
    <div class="grid three" style="margin-top:22px">
      <div class="card"><h3>Clinical Engineering and Health Technology Management</h3><p>Linked to the IFMBE Clinical Engineering Division.</p></div>
      <div class="card"><h3>Health Technology Assessment, Regulation and Policy</h3><p>Linked to the IFMBE Health Technology Assessment Division.</p></div>
      <div class="card"><h3>Students and Young Professionals</h3><p>Mentorship, the Young Investigator Competition and early-career networking.</p></div>
      <div class="card"><h3>Women in Biomedical Engineering</h3><p>Visibility, mentorship and leadership across the profession.</p></div>
      <div class="card"><h3>Industry and Innovation Forum</h3><p>Manufacturers, distributors, start-ups and incubators.</p></div>
      <div class="card"><h3>Education and Accreditation</h3><p>Curricula, ECSA accreditation and professional recognition.</p></div>
    </div>
    <div class="btn-row"><a class="btn" href="{JOIN}">Join a group through the membership form</a></div>
  </div>
</section>
"""

CONTACT = f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Contact BESSA</h1>
  <p class="lead">The Secretariat is hosted by the Biomedical Engineering Research Centre at the University of Cape Town.</p>
</div></section>

<section class="section">
  <div class="wrap grid two">
    <div class="card dark">
      <h3>Secretariat</h3>
      <p>Biomedical Engineering Society of South Africa (BESSA)<br>Biomedical Engineering Research Centre<br>Level 7 Anatomy Building, UCT Medical School<br>Anzio Road, Observatory, Cape Town 7925, South Africa</p>
      <p>Email: <a href="mailto:BESSA@uct.ac.za">BESSA@uct.ac.za</a><br>President: Prof Sudesh Sivarasu · Secretary-General: Mr Mladen Poluta<br>Follow BESSA on X: <a href="https://x.com/BME_ZA" rel="noopener">@BME_ZA</a></p>
      <p>Newsletter: email <a href="mailto:BESSA@uct.ac.za?subject=Subscribe">BESSA@uct.ac.za</a> with the subject "Subscribe".</p>
      <div class="btn-row"><a class="btn light" href="{JOIN}">Join BESSA</a></div>
    </div>
    <div>
      <div class="card tint">
        <h3>Resources</h3>
        <ul class="ticks">
          <li>BESSA Constitution and Membership Rules (2026 revision), available from the Secretariat</li>
          <li>President's Report 2026</li>
          <li><a href="https://ifmbe.org" rel="noopener">IFMBE News</a></li>
          <li><a href="https://sabec.org.za" rel="noopener">SABEC 2027</a></li>
        </ul>
      </div>
      <div class="card" style="margin-top:22px">
        <h3>Partners and stakeholders</h3>
        <p>International Federation for Medical and Biological Engineering (IFMBE) · University of Cape Town Biomedical Engineering Research Centre (host of the BESSA secretariat) · Engineering Council of South Africa (ECSA) · South African Health Products Regulatory Authority (SAHPRA) · Department of Science, Technology and Innovation (DSTI) · South African universities offering biomedical engineering programmes · Global Clinical Engineering Alliance (GCEA) · Health technology industry and hospital groups.</p>
        <p>Annual STEM outreach promotes careers in biomedical engineering to learners and students.</p>
      </div>
    </div>
  </div>
</section>
"""

PAGES = [
    ("index.html", "Home", "The South African member society of the IFMBE. Membership for biomedical and clinical engineers, SABEC 2027 with reduced fees for members, and events.", HOME),
    ("about.html", "About & IFMBE", "About BESSA: history since 1978, mission, leadership and governance, and BESSA's place in the International Federation for Medical and Biological Engineering.", ABOUT),
    ("membership.html", "Membership", "BESSA membership: seven categories, benefits, indicative 2027 fees and how to apply. Members pay 20% less at SABEC 2027.", MEMBERSHIP),
    ("sabec-2027.html", "SABEC 2027", "SABEC 2027, 11-12 March 2027, Cape Town: BESSA's flagship biomedical engineering conference. Registration fees, BESSA member discount, key dates and links.", SABEC),
    ("events.html", "Events & Groups", "BESSA events, the Annual General Meeting, and the divisions and working groups launching in 2027.", EVENTS),
    ("contact.html", "Contact", "Contact the Biomedical Engineering Society of South Africa: secretariat at UCT, email, resources and partners.", CONTACT),
]

def build():
    for path, title, desc, body in PAGES:
        html = head(title, desc, path) + header(path) + body + FOOTER
        with open(os.path.join(OUT, path), "w") as f:
            f.write(html)
    # join page: body stored in join_body.html, wrapped with header/footer
    with open(os.path.join(OUT, "join_body.html")) as f:
        join_body = f.read()
    html = head("Join BESSA", "Apply for BESSA membership: one form for all categories. You receive a reference number and the application goes to the Membership Secretary.", "join.html") + header("join.html") + join_body + FOOTER
    with open(os.path.join(OUT, "join.html"), "w") as f:
        f.write(html)
    # sitemap and robots
    today = datetime.date.today().isoformat()
    urls = [p for p, *_ in PAGES] + ["join.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(OUT, "CNAME"), "w").write("bessa.co.za\n")
    nf = head("Page not found", "Page not found", "404.html") + header("404.html") + '<section class="section"><div class="wrap"><h1>Page not found</h1><p class="lead">That page does not exist on bessa.co.za. Try the menu above or go to the <a href="index.html">home page</a>.</p></div></section>' + FOOTER
    open(os.path.join(OUT, "404.html"), "w").write(nf)
    print("built", len(urls) + 1, "pages")

if __name__ == "__main__":
    build()
