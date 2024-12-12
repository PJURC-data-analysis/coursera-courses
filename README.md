![banner](https://github.com/PJURC-data-analysis/coursera-courses/blob/main/media/banner.png)

# Coursera Course Analysis: Success Factors in Online Learning
[View Notebook](https://github.com/PJURC-data-analysis/coursera-courses/blob/main/Coursera%20Courses.ipynb)

An analysis of 891 Coursera courses to identify key factors contributing to course success and popularity. This study examines relationships between course features like certification types, difficulty levels, and organizational partnerships to provide strategic insights for online education providers.

## Overview

### Business Question 
What course characteristics and organizational factors contribute most significantly to course success on Coursera's platform?

### Key Findings
- **Institutional Impact**: Higher Education institutions dominate (69%) successful course creation
- **Certification Insights**: Professional Certificate courses show 2x higher average enrollment
- **Difficulty Level**: Mixed and Beginner difficulty courses demonstrate highest enrollment rates
- **Rating Patterns**: Course certification programs maintain high ratings (>4.60) across all difficulty levels

### Impact/Results
- Identified two viable strategies for course development
- Mapped success patterns across different course types
- Created framework for evaluating course potential

## Data

### Source Information
- Dataset: 891 Coursera courses scraped from website
- Source: [Kaggle Dataset](https://www.kaggle.com/datasets/siddharthm1698/coursera-course-dataset)
- Time Period: 2019

### Variables Analyzed
- Course Title
- Course Organization
- Certificate Type
- Course Rating
- Course Difficulty
- Students Enrolled

## Methods

### Analysis Approach
1. Organizational Analysis
   - Distribution of course providers
   - Success rates by provider type
2. Course Feature Analysis
   - Certificate type impact
   - Difficulty level assessment
   - Rating pattern analysis
3. Success Pattern Identification
   - Top 10 course characteristics
   - Enrollment drivers

### Tools Used
- Python (Data Analysis)
  - Pandas: Data manipulation
  - Numpy: Numerical computations
  - Matplotlib: Visualization
  - Seaborn: Visualization

## Getting Started

### Prerequisites
```python
matplotlib==3.9.3
numpy==2.2.0
pandas==2.2.3
seaborn==0.13.2
```

### Installation & Usage
```bash
git clone git@github.com:PJURC-data-analysis/coursera-courses.git
cd coursera-courses
pip install -r requirements.txt
jupyter notebook "Coursera Courses.ipynb"
```

## Project Structure
```
coursera-analysis/
│   README.md
│   requirements.txt
│   Coursera Courses.ipynb
|   utils.py
└── data/
    └── coursera_data.csv
```

## Strategic Recommendations
1. **University Partnership Strategy**
   - Focus on mixed-difficulty Course certifications
   - Partner with established educational institutions
   - Leverage proven success patterns

2. **Professional Certificate Strategy**
   - Target untapped market segment
   - Focus on job-ready skills
   - Leverage higher enrollment potential

## Future Improvements
- Include course completion rates
- Add certification purchase data
- Analyze course category impact
- Include post-completion employment data
- Track long-term student outcomes

## Acknowledgments
- Kaggle for dataset provision
- Coursera platform for course metrics
