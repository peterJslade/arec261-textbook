# Proposed Curriculum Plan for Modules 6–12

## Purpose

This plan revises the second half of *Agricultural Data Analytics*. It gives spatial and field-level agricultural data a larger role, moves communication to the end of the course, and concludes with a two-module sequence on advanced visualization and communicating completed analysis.

The revised course has three broad arcs:

1. **Tools and workflows (Modules 1–5):** Excel, R, data acquisition and preparation, graphing, and artificial intelligence.
2. **Spatial and quantitative analysis (Modules 6–10):** spatial foundations, machinery data, external spatial data, model thinking, correlation, and simple linear models.
3. **Producing and communicating finished work (Modules 11–12):** advanced visualization, interactive displays, dashboards, reports, and presentations.

Functions, iteration, and the many-models workflow are not separate modules in this plan. They are useful topics, but they would be somewhat isolated from the revised course sequence and would require more programming background than the course otherwise develops.

## Revised Course Structure

| Module | Topic |
|---|---|
| 1 | Introduction to Excel |
| 2 | Introduction to R |
| 3 | Getting, Cleaning, and Combining Data |
| 4 | Graphing |
| 5 | Using Artificial Intelligence |
| 6 | Spatial Data and Mapping |
| 7 | Field-Level Data |
| 8 | External Spatial Data |
| 9 | Thinking About Modelling Data |
| 10 | Relationships: Correlation and Simple Linear Models |
| 11 | Advanced Visualization and Interactive Displays |
| 12 | Communicating and Delivering Results |

---

# Module 6 — Spatial Data and Mapping

This module establishes the vocabulary and basic R skills students need before encountering field-level machinery data. Its central question is: **How do we represent and communicate where agricultural observations occurred?**

## Chapter 6.1 — Thinking Spatially

- What makes spatial data different
- Geometry and attributes
- Points, lines, polygons, and rasters
- Latitude and longitude
- Coordinate reference systems
- Geographic versus projected coordinates
- Spatial resolution, scale, and extent
- Agricultural examples at field, RM, provincial, and national scales

## Chapter 6.2 — Working with Spatial Data in R

- Reading shapefiles and GeoPackages with `sf`
- Inspecting an `sf` object
- Understanding the geometry column
- Creating points from longitude and latitude
- Reading field and RM boundaries
- Transforming coordinate systems
- Joining ordinary data to spatial boundaries
- Introductory spatial joins
- Exporting a spatial dataset

## Chapter 6.3 — Making and Interpreting Maps

- Making maps with `geom_sf()`
- Point and polygon maps
- Choropleth maps
- Continuous and categorical colour scales
- Missing observations versus genuine zeros
- Consistent scales when comparing maps
- Faceting by crop, region, or year
- Titles, legends, units, captions, and sources
- Avoiding misleading maps
- Optional introductory interactive map

**Possible assignment:** Map RM crop yields, agricultural facilities, or weather stations and explain two patterns and one limitation of the map.

---

# Module 7 — Field-Level Data

This module introduces data produced by combines and other agricultural machinery. Its central question is: **How do agricultural machines turn field operations into data, and how should those data be prepared for analysis?**

## Chapter 7.1 — How Field-Level Data Are Produced

- GPS and GNSS positioning
- Combine yield monitors
- Mass-flow and moisture sensors
- Speed, distance, swath width, and header status
- Planting, spraying, fertilizer application, and tillage data
- Target versus actual application rates
- Recording frequency and spatial resolution
- Calibration and flow delay
- Field boundaries and machine passes
- Proprietary display files and standard exports
- Which variables are measured directly and which are calculated
- Data ownership, confidentiality, and privacy
- Best practices for collecting field-level data

## Chapter 7.2 — Working with Real Machinery Data

- Importing a machinery shapefile
- Reading accompanying metadata
- Parsing timestamps
- Checking variable definitions and units
- Zero-yield observations
- Headland turns and header-up records
- Partial swaths
- Flow delay
- GPS jumps
- Duplicate observations
- Missing values
- Impossible speeds, distances, or yields
- Creating quality flags
- Comparing raw and cleaned summaries
- Documenting cleaning decisions

The official John Deere sample harvest data can be used until a suitable Canadian teaching dataset is obtained. A synthetic Saskatchewan dataset could also be created with known errors and a clearly documented data-generating process.

## Chapter 7.3 — Mapping Field-Level Data

- Mapping the machine path
- Colouring observations by yield, moisture, or speed
- Comparing raw and cleaned yield maps
- Comparing varieties, treatments, or machine passes
- Point versus polygon representations
- Aggregating observations into grid cells
- Calculating operation and field summaries
- Avoiding false precision
- Exporting a clean spatial layer and finished map

**Possible assignment:** Produce a harvest-quality report containing a cleaned dataset, a raw map, a cleaned map, summary measures, and an explanation of the cleaning decisions.

---

# Module 8 — External Spatial Data

This module expands beyond machinery records by adding environmental and remotely sensed information. Its central question is: **What external conditions can be attached to a field, and what limitations arise when data sources have different spatial and temporal resolutions?**

## Chapter 8.1 — Obtaining Environmental and Remote-Sensing Data

- Google Earth Engine conceptually
- Accessing Earth Engine through R
- AAFC Annual Crop Inventory
- Satellite imagery and vegetation indices
- Elevation and terrain data
- Gridded precipitation and temperature
- Weather-station observations
- Soil and land-resource data
- Spatial and temporal resolution
- Direct measurements versus modelled or remotely sensed values
- Saving a dated local snapshot
- Recording sources, units, retrieval dates, and query parameters

Students should be given cached copies of external data so that authentication, internet access, or service interruptions do not prevent completion of the exercises.

## Chapter 8.2 — Combining External and Field Data

- Matching coordinate reference systems
- Extracting raster values at machinery points
- Summarizing raster values within field boundaries
- Attaching the nearest weather station
- Matching observations by location and date
- Adding elevation, soil, crop classification, and weather
- Resolution mismatches
- Missing spatial matches
- Avoiding duplicated rows during joins
- Checking row counts and keys after a merge
- Documenting the completed analytical table

A resulting table might include:

```text
timestamp
longitude
latitude
yield
moisture
elevation
soil_zone
crop_inventory
precipitation
temperature
vegetation_index
```

## Chapter 8.3 — Mapping Integrated Field Information

- Layering field boundaries, yield observations, and external data
- Comparing yield and elevation maps
- Comparing yield and vegetation-index maps
- Mapping accumulated precipitation
- Small multiples and consistent scales
- Interactive layer controls
- Pop-ups and tooltips
- Communicating differences in resolution
- Building a compact field viewer or Quarto dashboard
- Distinguishing visible spatial association from causation

**Possible assignment:** Combine cleaned yield-monitor data with at least two external spatial layers and produce a field viewer or short spatial report.

---

# Module 9 — Thinking About Modelling Data

This module develops the conceptual language needed for correlation and linear models without beginning with formal inference. Its central question is: **What is a model, what does it leave out, and how should its usefulness be evaluated?**

## Chapter 9.1 — Models as Simplifications

- What a model is
- Models as purposeful simplifications
- Response and explanatory variables
- Inputs and outputs
- Deterministic versus empirical models
- Assumptions
- Relevant and irrelevant detail
- Explanation versus prediction
- Why no model reproduces reality completely
- The role of agricultural subject-matter knowledge

Examples can compare an overall mean, separate group means, and a relationship with another variable as alternative models of yield.

## Chapter 9.2 — Predictions, Errors, and Model Quality

- Observed and fitted values
- Residuals
- Positive and negative errors
- Residual plots
- Mean absolute error
- Root mean squared error
- Comparing a model against a simple baseline
- Training and evaluation data conceptually
- Underfitting and overfitting
- Why fitting existing data perfectly can be undesirable
- Interpolation and extrapolation

## Chapter 9.3 — Seeing Relationships

- Scatterplots
- Direction, form, and strength
- Linear and curved patterns
- Outliers and influential observations
- Changing spread
- Subgroups and hidden categories
- Anscombe’s quartet
- Choosing a plausible model form
- Association versus causation
- Visible spatial patterns versus evidence of a relationship

This chapter provides the bridge from general model thinking to correlation and simple linear models.

---

# Module 10 — Relationships: Correlation and Simple Linear Models

This module introduces correlation and regression as descriptive and predictive tools. It deliberately stops before formal statistical inference. Its central question is: **How can we describe, model, and criticize a relationship between two variables?**

## Chapter 10.1 — Correlation

- Covariance conceptually
- Correlation
- Direction and strength
- Calculating correlation in Excel and R
- Effects of units and scale
- Sensitivity to outliers
- Restricted ranges
- Subgroups
- Nonlinear relationships
- Pairing a correlation with a scatterplot
- Correlation versus causation

## Chapter 10.2 — Simple Linear Models

- The fitted regression line
- Intercept and slope
- Fitting a model in Excel and R
- Fitted values and residuals
- Interpreting coefficients in context
- Point predictions
- Interpolation and extrapolation
- Communicating the model in plain language

## Chapter 10.3 — Evaluating and Criticizing a Linear Model

- R-squared as a description of fit
- Residual plots
- Nonlinearity
- Unequal spread
- Outliers and influential observations
- Comparing model error with a baseline
- Prediction versus explanation
- Limits of observational data
- Avoiding causal overstatement
- Reporting model limitations

The module does not cover sampling distributions, standard errors, hypothesis tests, p-values, confidence intervals, prediction intervals, or claims of statistical significance.

**Possible assignment:** Investigate an agricultural relationship, fit and criticize a simple linear model, and communicate the result using a scatterplot, fitted line, residual plot, and short written interpretation.

---

# Module 11 — Advanced Visualization and Interactive Displays

Module 4 teaches standard charts and the foundations of graph design. Module 11 returns to visualization after students have produced spatial and model-based results. Its central question is: **How can a completed analysis be turned into a sophisticated visual product that another person can explore and understand?**

## Chapter 11.1 — Advanced Graph Design

- Layering information in `ggplot2`
- Small multiples and faceting
- Direct labels
- Annotations
- Reference lines and highlighted periods
- Custom scales and meaningful breaks
- Ordering categories
- Displaying multiple related variables
- Combining maps and charts
- Accessible colour palettes
- Designing for print, projection, and screens
- Saving publication-quality output

Examples can include yield and precipitation over time, fitted relationships with labelled unusual observations, raw and cleaned yield-monitor maps, and a map paired with a ranked chart.

## Chapter 11.2 — Interactive Charts, Maps, and Tables

- Interactive charts with `plotly`
- Hover information and tooltips
- Zooming and selecting observations
- Searchable tables with `DT`
- Interactive maps with `leaflet`
- Layer controls
- Pop-ups
- Showing field-level information on demand
- When interaction helps
- When a static chart communicates better
- Saving and sharing HTML output

## Chapter 11.3 — Dashboards and Visual Data Products

- Dashboard purpose and audience
- Choosing a small set of questions
- Visual hierarchy
- KPI cells
- Filters and controls
- Layout and navigation
- Excel dashboards
- Quarto dashboards
- Combining charts, maps, tables, and text
- Data sources and update dates
- Accessibility
- Publishing or distributing the finished product

**Module deliverable:** A polished visual data product containing static graphics, a map, an interactive display or dashboard, and concise explanatory text.

---

# Module 12 — Communicating and Delivering Results

The current communication material moves to the end of the course so students can work with richer analyses. Its central question is: **Can another person understand, verify, update, and act on the analysis?**

## Chapter 12.1 — Preparing Analysis for Handoff

- Start with the audience
- Give each sheet or file one purpose
- Separate raw data, calculations, and output
- Label variables and units
- Create a data dictionary
- Record sources and retrieval dates
- Format a workbook for another person
- Protect input and calculation cells
- Organize an R project
- Preserve reproducibility
- Include a README
- Document assumptions and limitations
- Protect private farm and producer information

This chapter expands the current workbook-aesthetics material into a broader discussion of professional handoff.

## Chapter 12.2 — Writing an Analytical Report

- State the question
- Describe the data
- Explain methods in plain language
- Present the principal results
- Integrate charts, maps, and tables
- Distinguish results from interpretation
- Discuss limitations
- Avoid causal overstatement
- Write useful captions
- Cite data sources
- Make recommendations proportional to the evidence
- Produce the report in Word or Quarto

A short report can use this structure:

1. Question and context
2. Data and methods
3. Results
4. Interpretation
5. Limitations
6. Conclusions

## Chapter 12.3 — Presenting and Defending an Analysis

- Structure a short presentation
- Design slides for listening
- Explain a chart or map orally
- Choose what to leave out
- Use annotations instead of dense legends
- Present model results without unnecessary technical clutter
- Rehearse timing
- Handle questions
- Explain uncertainty and limitations
- Respond when an error is discovered
- Provide supporting files after the presentation

**Module deliverables:** A documented workbook or R project, a short analytical report, and a brief presentation.

---

# Capstone Sequence

Modules 11 and 12 form a two-stage capstone based on one underlying analysis.

## Stage 1 — Visual Product

During Module 11, students produce:

- Polished static graphs
- A map
- An interactive display or dashboard
- Short explanatory text

## Stage 2 — Professional Delivery

During Module 12, students convert the same analysis into:

- A documented workbook or R project
- A short analytical report
- A brief presentation

This structure assesses one substantive analysis through several communication formats instead of requiring unrelated projects. The course ending becomes:

> Module 10 finds and models a relationship. Module 11 turns the analysis into an effective visual product. Module 12 delivers the result to a real audience.

