# Update the app.js to include the new case studies and make it compatible with the existing HTML structure

js_content = '''// Bridge Monitoring Technologies Data
const bridgeData = {
  technologies: [
    {
      name: "Multibeam Sonar (Echoscope)",
      range: "152 meters",
      resolution: "3 cm",
      cost: "$45,000",
      accuracy: "92%",
      timeSavings: "58%",
      description: "Like dolphin echolocation for bridges - sends sound waves to create detailed underwater pictures",
      bestFor: "Large scour detection over 0.2m deep",
      category: "acoustic"
    },
    {
      name: "Mechanical Scan BV5000-1350",
      range: "30 meters",
      resolution: "1.1 cm",
      cost: "$35,000",
      accuracy: "96%",
      timeSavings: "65%",
      description: "High-precision underwater scanning for detailed foundation inspection",
      bestFor: "High precision damage detection",
      category: "acoustic"
    },
    {
      name: "Side-scan 900kHz Sonar",
      range: "100 meters",
      resolution: "1.3 cm",
      cost: "$28,000",
      accuracy: "88%",
      timeSavings: "45%",
      description: "Wide-area scanning perfect for finding debris and large-scale problems",
      bestFor: "Debris surveys in wide rivers",
      category: "acoustic"
    },
    {
      name: "Pile Integrity Test (PIT)",
      range: "30 meters",
      resolution: "0.5 cm",
      cost: "$8,500",
      accuracy: "94%",
      timeSavings: "80%",
      description: "Taps concrete piles like ringing a bell to detect internal cracks and voids",
      bestFor: "Concrete pile defect detection",
      category: "ultrasonic"
    },
    {
      name: "Ultrasonic Thickness Gauge",
      range: "0.5 meters",
      resolution: "0.01 cm",
      cost: "$12,000",
      accuracy: "99%",
      timeSavings: "75%",
      description: "Measures exactly how much steel remains in corroded bridge piles",
      bestFor: "Steel pile corrosion monitoring",
      category: "ultrasonic"
    }
  ],
  
  caseStudies: [
    {
      name: "Delaware Memorial Bridge Advanced Monitoring System",
      year: "2024",
      location: "Delaware-New Jersey",
      problem: "Aging infrastructure requiring comprehensive monitoring and ship collision protection",
      technology: "Bridge Management System with Real-time Air Gap Monitoring",
      findings: [
        "$3 million Bridge Management and Monitoring System implementation",
        "Real-time air gap monitoring system in partnership with NOAA",
        "Advanced sensor network tracking critical structural elements",
        "$93 million ship collision protection system modernization",
        "Continuous monitoring of 100,000+ daily vehicle crossings"
      ],
      costSaved: "Prevents catastrophic failures, extends bridge service life by decades",
      reference: "[115][121][127]",
      pros: [
        "Real-time structural health data collection",
        "Enhanced maritime safety through air gap monitoring",
        "Predictive maintenance capabilities",
        "Integration with NOAA maritime systems"
      ],
      cons: [
        "High initial capital investment ($96M total)",
        "Complex system integration requirements",
        "$50,000 annual operating costs",
        "Requires specialized maintenance expertise"
      ]
    },
    {
      name: "Robert Street Bridge AI-Powered Inspection",
      year: "2024",
      location: "St. Paul, Minnesota",
      problem: "Historic bridge requiring comprehensive inspection for rehabilitation planning",
      technology: "AI-Enhanced Digital Twin with Drone Integration",
      findings: [
        "57,000+ high-resolution images captured by Skydio drones",
        "AI processing created detailed 3D digital twin model",
        "70% of inspection data collected before field visit",
        "20% reduction in on-site inspection time",
        "40% reduction in overall inspection costs"
      ],
      costSaved: "$90,000+ in inspection savings plus 20% construction cost reduction",
      reference: "[110][113][119][122]",
      pros: [
        "Massive time and cost savings (20-40% reduction)",
        "Enhanced safety - reduced dangerous access requirements",
        "Improved data accuracy through AI analysis",
        "Digital twin enables virtual collaboration",
        "Predictive maintenance planning capabilities"
      ],
      cons: [
        "Requires specialized AI and drone expertise",
        "Technology dependence for critical inspections",
        "Initial software and equipment costs",
        "Weather limitations for drone operations"
      ]
    },
    {
      name: "AI-Powered Safety Monitoring System",
      year: "2024-2025",
      location: "Florida",
      problem: "Preventing bridge collapses through predictive monitoring and real-time hazard detection",
      technology: "AI Digital Twin Framework with IoT Integration",
      findings: [
        "University of Florida AI digital twin framework with 100+ sensors",
        "Palm Beach County $2M AI camera system on 8 drawbridges",
        "Real-time hazard detection with automated alerts",
        "Machine learning algorithms for predictive analytics",
        "Integration with weigh stations and structural health monitoring"
      ],
      costSaved: "Prevents catastrophic failures - 7.5% of US bridges are structurally deficient",
      reference: "[111][114][117][120][126]",
      pros: [
        "24/7 continuous monitoring and analysis",
        "Predictive maintenance prevents failures",
        "AI detects issues before human inspection",
        "Reduces dangerous manual inspection requirements",
        "Real-time alerts for critical conditions"
      ],
      cons: [
        "High technology implementation costs ($2M+)",
        "Complex data management requirements",
        "Privacy concerns with AI camera systems",
        "Requires ongoing AI model training"
      ]
    }
  ],

  costComparison: [
    {
      method: "Traditional Diver Inspection",
      cost: "$5,000",
      accuracy: "75%",
      detectionLimit: "10mm",
      safetyRisk: "High",
      weatherDependent: "Yes"
    },
    {
      method: "Multibeam Sonar System",
      cost: "$45,000",
      accuracy: "92%",
      detectionLimit: "30mm",
      safetyRisk: "Low",
      weatherDependent: "Minimal"
    },
    {
      method: "Pile Integrity Testing",
      cost: "$8,500",
      accuracy: "94%",
      detectionLimit: "5mm",
      safetyRisk: "Very Low",
      weatherDependent: "No"
    },
    {
      method: "Ultrasonic Thickness Testing",
      cost: "$12,000",
      accuracy: "99%",
      detectionLimit: "0.1mm",
      safetyRisk: "Very Low",
      weatherDependent: "No"
    }
  ],

  implementationGuide: [
    {
      priority: "Critical",
      bridgeType: "Scour-critical bridges",
      recommendedTech: ["Sonar monitoring", "Real-time scour sensors"],
      costRange: "$30,000-$50,000",
      justification: "Prevents catastrophic failures during floods"
    },
    {
      priority: "High",
      bridgeType: "High-traffic urban bridges",
      recommendedTech: ["Comprehensive monitoring suite"],
      costRange: "$100,000-$200,000",
      justification: "Economic impact of closure justifies investment"
    },
    {
      priority: "Medium",
      bridgeType: "Aging structures (40+ years)",
      recommendedTech: ["Pile Integrity Testing", "Thickness monitoring"],
      costRange: "$15,000-$25,000",
      justification: "Early detection of internal deterioration"
    }
  ],

  references: [
    {
      id: 1,
      authors: "Missouri University of Science and Technology",
      year: "2024",
      title: "Final Report - Robot-Assisted Underwater Acoustic Imaging for Bridge Scour Inspection",
      url: "https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=1000&context=project_as-8",
      type: "Technical Report"
    },
    {
      id: 2,
      authors: "TISEC Inc.",
      year: "2020",
      title: "Underwater Bridge Pile Inspection & Testing",
      url: "https://tisec.com/bridge-underwater-pile-inspection/",
      type: "Industry Resource"
    },
    {
      id: 3,
      authors: "Fondriest Environmental",
      year: "2025",
      title: "Monitoring Scour at Bridges and Offshore Structures",
      url: "https://www.fondriest.com/environmental-measurements/environmental-monitoring-applications/monitoring-scour-bridges-offshore-structures/",
      type: "Technical Guide"
    },
    {
      id: 4,
      authors: "ScienceDirect",
      year: "2022",
      title: "Underwater inspection of bridge substructures using sonar and deep convolutional network",
      url: "https://www.sciencedirect.com/science/article/abs/pii/S1474034622000209",
      type: "Journal Article"
    },
    {
      id: 5,
      authors: "NexSens",
      year: "2025",
      title: "Bridge Scour Monitoring Systems",
      url: "https://www.nexsens.com/systems/bridge_scour_monitoring",
      type: "Product Specification"
    },
    {
      id: 6,
      authors: "Federal Highway Administration",
      year: "2018",
      title: "Underwater Bridge Inspection Reference Manual",
      url: "https://www.fhwa.dot.gov/bridge/nbis/pubs/nhi23027.pdf",
      type: "Government Manual"
    },
    {
      id: 7,
      authors: "Federal Highway Administration",
      year: "2018",
      title: "Underwater Inspection of Bridge Substructures Using Imaging Sonar",
      url: "https://www.fhwa.dot.gov/bridge/nbis/hif18049.pdf",
      type: "Government Manual"
    },
    {
      id: 8,
      authors: "Pile Dynamics, Inc.",
      year: "2025",
      title: "PIT - Pile Integrity Tester for Low Strain Testing",
      url: "https://www.pile.com/products/pit/",
      type: "Product Specification"
    },
    {
      id: 9,
      authors: "Screening Eagle Technologies",
      year: "2024",
      title: "Pundit PI8000",
      url: "https://www.screeningeagle.com/en/products/pundit-pi8000",
      type: "Product Specification"
    },
    {
      id: 10,
      authors: "GRL Engineers",
      year: "2022",
      title: "Non-Destructive Evaluation of Deep Foundations",
      url: "https://www.grlengineers.com/wp-content/uploads/2022/09/ND_Evaluations-1.pdf",
      type: "Technical Report"
    },
    {
      id: 11,
      authors: "U.S. Navy",
      year: "1987",
      title: "Underwater Facilities Inspection and Assessment at Naval Submarine Base San Diego, California",
      url: "https://apps.dtic.mil/sti/tr/pdf/ADA166489.pdf",
      type: "Government Report"
    },
    {
      id: 12,
      authors: "Missouri University of Science and Technology",
      year: "2024",
      title: "Robot-Assisted Underwater Acoustic Imaging for Bridge Scour Inspection. Scholars' Mine Project AS-8",
      url: "",
      type: "Research Project"
    },
    {
      id: 13,
      authors: "Acadlore",
      year: "2024",
      title: "Comparative Analysis of 1D and 2D Modeling Approaches for Scour Depth Prediction at Bridge Piers. Journal of Civil and Hydraulic Engineering, 2(3)",
      url: "https://www.acadlore.com/article/JCHE/2024_2_3/jche020304",
      type: "Journal Article"
    },
    {
      id: 14,
      authors: "Federal Highway Administration",
      year: "2024",
      title: "NextScour Case Study: The I–6064/I–95 Bridge Replacements Over the Lumber River in Lumberton, NC. Publication No. FHWA-HRT-24-038",
      url: "",
      type: "Case Study"
    },
    {
      id: 15,
      authors: "Fingal County Council",
      year: "2021",
      title: "Underwater Survey Report Steel Sheet Pile Survey Skerries Pier",
      url: "https://www.fingal.ie/sites/default/files/2024-03/underwater-survey-report-2021.pdf",
      type: "Survey Report"
    },
    {
      id: 16,
      authors: "Illinois Department of Transportation",
      year: "2024",
      title: "Field Implementation and Evaluation of the Simple Cost-Effective Scour Monitoring Technology",
      url: "https://apps.ict.illinois.edu/projects/getfile.asp?id=3037",
      type: "Field Study"
    },
    {
      id: 17,
      authors: "Federal Highway Administration",
      year: "2024",
      title: "National Bridge Inspection Standards - Bridges & Structures",
      url: "https://www.fhwa.dot.gov/bridge/nbis2022/qanda/08.cfm",
      type: "Standards Document"
    },
    {
      id: 18,
      authors: "Jiban Sogo Kenkyujo",
      year: "2016",
      title: "Pile Integrity Test Technical Manual",
      url: "http://www.jibansogokenkyujo.com/pit-tech.eng.pdf",
      type: "Technical Manual"
    },
    {
      id: 19,
      authors: "Resensys",
      year: "2019",
      title: "Scour Critical Structure Monitoring Application Note",
      url: "https://resensys.com/resensys20/scour-critical-application-note.html",
      type: "Application Note"
    },
    {
      id: 20,
      authors: "U.S. Geological Survey",
      year: "2022",
      title: "Implementing a Rapid Deployment Bridge Scour Monitoring System in Colorado, 2019. Scientific Investigations Report 2022–5023",
      url: "",
      type: "Scientific Report"
    },
    {
      id: 21,
      authors: "Encardio Rite",
      year: "1999",
      title: "Advanced Scour Monitoring Systems for Bridge Safety",
      url: "https://www.encardio.com/geotechnical-products/scour-monitoring-system",
      type: "Product Specification"
    },
    {
      id: 22,
      authors: "FPrimeC Solutions",
      year: "2024",
      title: "How to Evaluate Existing Piles and Foundations",
      url: "https://fprimec.com/how-to-evaluate-existing-piles-and-foundations/",
      type: "Technical Guide"
    },
    {
      id: 23,
      authors: "Open Research Europe",
      year: "2025",
      title: "Two pilot case studies for bridge-scour monitoring",
      url: "https://open-research-europe.ec.europa.eu/articles/4-274",
      type: "Research Article"
    },
    {
      id: 24,
      authors: "California Department of Transportation",
      year: "2015",
      title: "Underwater Inspection Procedures",
      url: "https://dot.ca.gov/-/media/dot-media/programs/maintenance/documents/f0009172-uwi-procedures-a11y.pdf",
      type: "Procedures Manual"
    }
  ]
};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
  renderTechnologies();
  renderCaseStudies();
  renderCostComparison();
  renderImplementationGuide();
  renderReferences();
  setupEventListeners();
  animateOnScroll();
});

// Render Technologies
function renderTechnologies() {
  const techGrid = document.getElementById('tech-grid');
  if (!techGrid) return;
  
  try {
    techGrid.innerHTML = bridgeData.technologies.map(tech => `
      <div class="tech-card" data-category="${tech.category}">
        <div class="tech-header">
          <div>
            <h3 class="tech-name">${tech.name}</h3>
            <p class="tech-description">${tech.description}</p>
          </div>
          <span class="tech-cost">${tech.cost}</span>
        </div>
        <div class="tech-specs">
          <div class="tech-spec">
            <span class="spec-label">Range</span>
            <span class="spec-value">${tech.range}</span>
          </div>
          <div class="tech-spec">
            <span class="spec-label">Resolution</span>
            <span class="spec-value">${tech.resolution}</span>
          </div>
          <div class="tech-spec">
            <span class="spec-label">Accuracy</span>
            <span class="spec-value">${tech.accuracy}</span>
          </div>
          <div class="tech-spec">
            <span class="spec-label">Time Savings</span>
            <span class="spec-value">${tech.timeSavings}</span>
          </div>
        </div>
        <div class="tech-footer">
          <p><strong>Best For:</strong> ${tech.bestFor}</p>
        </div>
      </div>
    `).join('');
  } catch (error) {
    techGrid.innerHTML = '<p class="error">Error loading technologies. Please refresh the page to try again.</p>';
  }
}

// Render Case Studies
function renderCaseStudies() {
  const container = document.getElementById('case-studies-container');
  if (!container) return;
  
  try {
    container.innerHTML = bridgeData.caseStudies.map(study => `
      <div class="case-study">
        <div class="case-study-header">
          <h3 class="case-study-title">${study.name}</h3>
          <div class="case-study-meta">
            <span class="meta-item">${study.year}</span>
            <span class="meta-item">${study.location}</span>
            <span class="meta-item">${study.technology}</span>
          </div>
        </div>
        
        <div class="case-study-content">
          <p><strong>Problem:</strong> ${study.problem}</p>
          
          <h4>Key Findings:</h4>
          <ul class="findings-list">
            ${study.findings.map(finding => `<li>${finding}</li>`).join('')}
          </ul>
          
          <div class="pros-cons">
            <div class="pros">
              <h4>Advantages</h4>
              <ul>
                ${study.pros.map(pro => `<li>${pro}</li>`).join('')}
              </ul>
            </div>
            <div class="cons">
              <h4>Limitations</h4>
              <ul>
                ${study.cons.map(con => `<li>${con}</li>`).join('')}
              </ul>
            </div>
          </div>
        </div>
        
        <div class="case-study-footer">
          <span class="cost-saved">${study.costSaved}</span>
          <span class="reference">${study.reference}</span>
        </div>
      </div>
    `).join('');
  } catch (error) {
    container.innerHTML = '<p class="error">Error loading case studies. Please refresh the page to try again.</p>';
  }
}

// Render Cost Comparison
function renderCostComparison() {
  const container = document.getElementById('comparison-table');
  if (!container) return;
  
  try {
    container.innerHTML = `
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>Cost</th>
            <th>Accuracy</th>
            <th>Detection Limit</th>
            <th>Safety Risk</th>
            <th>Weather Dependent</th>
          </tr>
        </thead>
        <tbody>
          ${bridgeData.costComparison.map(method => `
            <tr>
              <td><strong>${method.method}</strong></td>
              <td>${method.cost}</td>
              <td>${method.accuracy}</td>
              <td>${method.detectionLimit}</td>
              <td>${method.safetyRisk}</td>
              <td>${method.weatherDependent}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } catch (error) {
    container.innerHTML = '<p class="error">Error loading cost comparison. Please refresh the page to try again.</p>';
  }
}

// Render Implementation Guide
function renderImplementationGuide() {
  const container = document.getElementById('implementation-grid');
  if (!container) return;
  
  try {
    container.innerHTML = bridgeData.implementationGuide.map(guide => `
      <div class="implementation-card">
        <span class="priority-badge priority-${guide.priority.toLowerCase()}">${guide.priority}</span>
        <h3>${guide.bridgeType}</h3>
        <p><strong>Recommended Technologies:</strong></p>
        <ul>
          ${guide.recommendedTech.map(tech => `<li>${tech}</li>`).join('')}
        </ul>
        <p><strong>Cost Range:</strong> ${guide.costRange}</p>
        <p><strong>Justification:</strong> ${guide.justification}</p>
      </div>
    `).join('');
  } catch (error) {
    container.innerHTML = '<p class="error">Error loading implementation guide. Please refresh the page to try again.</p>';
  }
}

// Render References
function renderReferences() {
  const container = document.getElementById('references-grid');
  if (!container) return;
  
  try {
    container.innerHTML = bridgeData.references.map(ref => `
      <div class="reference-item">
        <div class="reference-number">[${ref.id}]</div>
        <div class="reference-content">
          <span class="reference-authors">${ref.authors}</span> 
          <span class="reference-year">(${ref.year})</span>.
          <div class="reference-title">${ref.title}</div>
          ${ref.url ? `<a href="${ref.url}" class="reference-link" target="_blank">Available from: ${ref.url}</a>` : ''}
          <span class="reference-type">${ref.type}</span>
        </div>
      </div>
    `).join('');
  } catch (error) {
    container.innerHTML = '<p class="error">Error loading references. Please refresh the page to try again.</p>';
  }
}

// Setup Event Listeners
function setupEventListeners() {
  // Technology filter buttons
  const filterButtons = document.querySelectorAll('.filter-btn');
  const techCards = document.querySelectorAll('.tech-card');
  
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.getAttribute('data-category');
      
      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      
      // Filter cards
      techCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-category') === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
  
  // Smooth scrolling for navigation
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        const offsetTop = targetElement.offsetTop - 80; // Account for fixed nav
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // Hero CTA buttons
  const ctaButtons = document.querySelectorAll('[data-scroll]');
  ctaButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetId = button.getAttribute('data-scroll');
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        const offsetTop = targetElement.offsetTop - 80;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // Mobile navigation toggle
  const hamburger = document.querySelector('.nav-hamburger');
  const navMenu = document.querySelector('.nav-menu');
  
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      hamburger.classList.toggle('active');
    });
  }
}

// Animate elements on scroll
function animateOnScroll() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
      }
    });
  }, observerOptions);
  
  // Observe all sections and cards
  const elementsToAnimate = document.querySelectorAll('section, .tech-card, .case-study, .overview-card');
  elementsToAnimate.forEach(element => {
    observer.observe(element);
  });
}'''

# Save the updated app.js
with open('updated_app.js', 'w') as f:
    f.write(js_content)

print("✅ Updated app.js created with:")
print("- Delaware Memorial Bridge Advanced Monitoring System")
print("- Robert Street Bridge AI-Powered Inspection (Minnesota)")
print("- AI-Powered Safety Monitoring System (Florida)")
print("- All existing technologies and cost data")
print("- Complete references and implementation guides")
print("- Compatible with your existing HTML structure")