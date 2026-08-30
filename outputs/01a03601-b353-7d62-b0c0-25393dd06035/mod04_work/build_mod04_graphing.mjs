import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const projectRoot = path.resolve(new URL("../../../", import.meta.url).pathname);
const workRoot = path.dirname(new URL(import.meta.url).pathname);
const outputRoot = path.resolve(workRoot, "..");
const previewDir = path.join(outputRoot, "previews");
const finalName = "mod04_graphing_excel.xlsx";
const finalOutput = path.join(outputRoot, finalName);
const projectOutput = path.join(projectRoot, "textbook_examples", finalName);

function parseCsvLine(line) {
  const fields = [];
  let value = "";
  let quoted = false;
  for (let i = 0; i < line.length; i += 1) {
    const character = line[i];
    if (character === '"') {
      if (quoted && line[i + 1] === '"') {
        value += '"';
        i += 1;
      } else {
        quoted = !quoted;
      }
    } else if (character === "," && !quoted) {
      fields.push(value);
      value = "";
    } else {
      value += character;
    }
  }
  fields.push(value);
  return fields;
}

const sourceUrl = "https://agdataanalytics.com/practice/data/sask_variety_yields.csv";
const publisherUrl = "https://www.scic.ca/resources/sask-management-plus";
const sourceCsv = await fs.readFile(
  path.join(projectRoot, "practice", "data", "sask_variety_yields.csv"),
  "utf8",
);
const sourceRows = sourceCsv
  .trim()
  .split(/\r?\n/)
  .slice(1)
  .map(parseCsvLine)
  .map(([riskZone, crop, variety, year, acres, yieldValue]) => ({
    riskZone: Number(riskZone),
    crop,
    variety,
    year: Number(year),
    acres: acres === "" ? null : Number(acres),
    yieldValue: yieldValue === "" ? null : Number(yieldValue),
  }));

const canolaRows = sourceRows.filter((row) => row.crop === "Canola/Rapeseed");
const canolaLastRow = canolaRows.length + 1;

const variety2025 = new Map();
for (const row of canolaRows) {
  if (row.year !== 2025 || row.acres === null || row.yieldValue === null) continue;
  const item = variety2025.get(row.variety) ?? {
    variety: row.variety,
    acres: 0,
    weightedTotal: 0,
    zones: 0,
  };
  item.acres += row.acres;
  item.weightedTotal += row.acres * row.yieldValue;
  item.zones += 1;
  variety2025.set(row.variety, item);
}
const varietyRows = [...variety2025.values()]
  .map((item) => ({ ...item, weightedYield: item.weightedTotal / item.acres }))
  .sort((a, b) => b.acres - a.acres);
const topTen = varietyRows
  .slice(0, 10)
  .sort((a, b) => a.weightedYield - b.weightedYield);
const varietySummaryFirstRow = 5;
const varietySummaryLastRow = varietySummaryFirstRow + varietyRows.length - 1;
const summaryRowByVariety = new Map(
  varietyRows.map((row, index) => [row.variety, varietySummaryFirstRow + index]),
);
const varietiesReported2024 = new Set(
  canolaRows
    .filter((row) => row.year === 2024 && row.acres !== null && row.yieldValue !== null)
    .map((row) => row.variety),
);
const scatterVarieties = varietyRows.filter((row) => varietiesReported2024.has(row.variety));
const scatterDataFirstRow = 42;
const scatterDataLastRow = scatterDataFirstRow + scatterVarieties.length - 1;

const workbook = Workbook.create();
const readme = workbook.worksheets.add("README");
const barSheet = workbook.worksheets.add("Bar chart");
const scatterSheet = workbook.worksheets.add("Scatter plot");
const histogramSheet = workbook.worksheets.add("Histogram");
const summarySheet = workbook.worksheets.add("Variety summary");
const canolaSheet = workbook.worksheets.add("Canola records");

const green = "#3F6F52";
const greenDark = "#2F5940";
const greenLight = "#E4EEE7";
const gold = "#D8A940";
const blue = "#2878A5";
const ink = "#24332B";
const muted = "#5F6E66";
const border = "#C9D5CD";
const white = "#FFFFFF";

function styleTitle(sheet, title, description, endColumn = "N") {
  sheet.showGridLines = false;
  sheet.mergeCells(`A1:${endColumn}1`);
  sheet.getRange("A1").values = [[title]];
  sheet.getRange(`A1:${endColumn}1`).format = {
    fill: green,
    font: { bold: true, color: white, size: 18 },
    verticalAlignment: "center",
  };
  sheet.getRange(`A1:${endColumn}1`).format.rowHeight = 30;
  sheet.mergeCells(`A2:${endColumn}2`);
  sheet.getRange("A2").values = [[description]];
  sheet.getRange(`A2:${endColumn}2`).format = {
    fill: greenLight,
    font: { color: ink, size: 10 },
    wrapText: true,
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:${endColumn}2`).format.rowHeight = 40;
}

function styleHeader(range) {
  range.format = {
    fill: green,
    font: { bold: true, color: white },
    borders: { preset: "outside", style: "thin", color: greenDark },
    verticalAlignment: "center",
  };
}

function styleTableBody(range) {
  range.format = {
    font: { color: ink },
    borders: {
      insideHorizontal: { style: "thin", color: border },
      bottom: { style: "thin", color: border },
    },
  };
}

function styleCheckBlock(sheet, startRow, rows) {
  styleHeader(sheet.getRange(`A${startRow}:C${startRow}`));
  styleTableBody(sheet.getRange(`A${startRow + 1}:C${startRow + rows}`));
  sheet.getRange(`B${startRow + 1}:C${startRow + rows}`).format.wrapText = true;
  sheet.getRange(`A${startRow}:C${startRow + rows}`).format.autofitRows();
  sheet.getRange(`A${startRow}:A${startRow + rows}`).format.columnWidth = 18;
  sheet.getRange(`B${startRow}:B${startRow + rows}`).format.columnWidth = 40;
  sheet.getRange(`C${startRow}:C${startRow + rows}`).format.columnWidth = 27;
}

styleTitle(
  readme,
  "Graphing actual Saskatchewan canola variety yields",
  "The examples use reported SCIC variety yields by risk zone, 2021 to 2025. Start with the Bar chart sheet and follow its numbered instructions for selecting data, choosing a chart, and changing the title, axes, labels and colour.",
  "H",
);
readme.getRange("A4:B9").values = [
  ["Sheet", "What to notice"],
  ["Bar chart", "Acre-weighted 2025 yield for the ten most widely grown canola varieties."],
  ["Scatter plot", "Provincial weighted yield in 2024 versus 2025 for varieties reported in both years."],
  ["Histogram", "The distribution of 674 reported 2025 risk-zone-by-variety yields."],
  ["Variety summary", "Formula-driven acres, weighted yields and reporting-zone counts for all 97 canola varieties."],
  ["Canola records", "The 3,370 Canola/Rapeseed rows copied from the 13,625-row source file; suppressed values remain blank."],
];
styleHeader(readme.getRange("A4:B4"));
styleTableBody(readme.getRange("A5:B9"));
readme.getRange("A11:H13").values = [
  ["Source file", sourceUrl, null, null, null, null, null, null],
  ["Publisher", publisherUrl, null, null, null, null, null, null],
  ["Method note", "Provincial variety yields are weighted by reported acres: sum(Acres × Yield) / sum(Acres). Missing acres and yields are not treated as zero.", null, null, null, null, null, null],
];
readme.getRange("A11:A13").format = {
  fill: "#F5F7F5",
  font: { bold: true, color: muted, size: 9 },
};
readme.getRange("B11:H13").merge(true);
readme.getRange("B11:H13").format = {
  fill: "#F5F7F5",
  font: { color: muted, italic: true, size: 9 },
  wrapText: true,
};
readme.getRange("A11:H13").format.rowHeight = 28;
readme.getRange("A4:A13").format.columnWidth = 20;
readme.getRange("B4:B13").format.columnWidth = 100;
readme.getRange("B5:B9").format.wrapText = true;
readme.getRange("A4:B9").format.autofitRows();

canolaSheet.showGridLines = false;
canolaSheet.getRange(`A1:G${canolaLastRow}`).values = [
  ["Risk_Zone", "Crop", "Variety", "Year", "Acres", "Yield", "Acre-yield total"],
  ...canolaRows.map((row) => [
    row.riskZone,
    row.crop,
    row.variety,
    row.year,
    row.acres,
    row.yieldValue,
    null,
  ]),
];
canolaSheet.getRange("G2").formulas = [["=IF(COUNT(E2:F2)=2,E2*F2,\"\")"]];
canolaSheet.getRange(`G2:G${canolaLastRow}`).fillDown();
const canolaTable = canolaSheet.tables.add(`A1:G${canolaLastRow}`, true, "CanolaRecords");
canolaTable.style = "TableStyleMedium4";
canolaSheet.freezePanes.freezeRows(1);
canolaSheet.getRange(`A2:A${canolaLastRow}`).format.numberFormat = "0";
canolaSheet.getRange(`D2:D${canolaLastRow}`).format.numberFormat = "0";
canolaSheet.getRange(`E2:E${canolaLastRow}`).format.numberFormat = "#,##0";
canolaSheet.getRange(`F2:F${canolaLastRow}`).format.numberFormat = "0.0";
canolaSheet.getRange(`G2:G${canolaLastRow}`).format.numberFormat = "#,##0.0";
canolaSheet.getRange("A:G").format.autofitColumns();
canolaSheet.getRange("A:A").format.columnWidth = 12;
canolaSheet.getRange("B:B").format.columnWidth = 21;
canolaSheet.getRange("C:C").format.columnWidth = 20;
canolaSheet.getRange("D:D").format.columnWidth = 10;
canolaSheet.getRange("E:E").format.columnWidth = 14;
canolaSheet.getRange("F:F").format.columnWidth = 12;
canolaSheet.getRange("G:G").format.columnWidth = 20;

styleTitle(
  summarySheet,
  "Provincial canola variety summary",
  "Varieties are sorted by 2025 reported acres. Weighted yield divides the summed acre-yield total by summed acres, so a small risk zone does not count as much as a large one.",
  "F",
);
summarySheet.getRange(`A4:F${varietySummaryLastRow}`).values = [
  ["Variety", "2025 acres", "2025 weighted yield", "2024 acres", "2024 weighted yield", "2025 risk zones"],
  ...varietyRows.map((row) => [row.variety, null, null, null, null, null]),
];
summarySheet.getRange("B5").formulas = [[`=SUMIFS('Canola records'!$E$2:$E$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025)`]];
summarySheet.getRange(`B5:B${varietySummaryLastRow}`).fillDown();
summarySheet.getRange("C5").formulas = [[`=SUMIFS('Canola records'!$G$2:$G$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025)/B5`]];
summarySheet.getRange(`C5:C${varietySummaryLastRow}`).fillDown();
summarySheet.getRange("D5").formulas = [[`=IF(SUMIFS('Canola records'!$E$2:$E$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2024)=0,\"\",SUMIFS('Canola records'!$E$2:$E$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2024))`]];
summarySheet.getRange(`D5:D${varietySummaryLastRow}`).fillDown();
summarySheet.getRange("E5").formulas = [[`=IFERROR(SUMIFS('Canola records'!$G$2:$G$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2024)/D5,\"\")`]];
summarySheet.getRange(`E5:E${varietySummaryLastRow}`).fillDown();
summarySheet.getRange("F5").formulas = [[`=COUNTIFS('Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025,'Canola records'!$F$2:$F$${canolaLastRow},\">0\")`]];
summarySheet.getRange(`F5:F${varietySummaryLastRow}`).fillDown();
styleHeader(summarySheet.getRange("A4:F4"));
styleTableBody(summarySheet.getRange(`A5:F${varietySummaryLastRow}`));
summarySheet.getRange(`B5:B${varietySummaryLastRow}`).format.numberFormat = "#,##0";
summarySheet.getRange(`C5:C${varietySummaryLastRow}`).format.numberFormat = "0.0";
summarySheet.getRange(`D5:D${varietySummaryLastRow}`).format.numberFormat = "#,##0;-#,##0;;";
summarySheet.getRange(`E5:E${varietySummaryLastRow}`).format.numberFormat = "0.0";
summarySheet.getRange(`F5:F${varietySummaryLastRow}`).format.numberFormat = "0";
summarySheet.getRange("A:A").format.columnWidth = 22;
summarySheet.getRange("B:F").format.columnWidth = 20;
summarySheet.freezePanes.freezeRows(4);

styleTitle(
  barSheet,
  "Build a bar chart of 2025 canola variety yields",
  "The ten varieties were selected by total 2025 acres, then ordered by acre-weighted yield. Select only Variety and Weighted yield when creating the chart.",
);
barSheet.getRange("A4:E14").values = [
  ["Variety", "Weighted yield (bu/ac)", "Reported acres", "Risk zones", "Formula in B"],
  ...topTen.map((row) => [row.variety, null, null, null, null]),
];
barSheet.getRange("B5").formulas = [[`=SUMIFS('Canola records'!$G$2:$G$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025)/SUMIFS('Canola records'!$E$2:$E$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025)`]];
barSheet.getRange("B5:B14").fillDown();
barSheet.getRange("C5").formulas = [[`=SUMIFS('Canola records'!$E$2:$E$${canolaLastRow},'Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025)`]];
barSheet.getRange("C5:C14").fillDown();
barSheet.getRange("D5").formulas = [[`=COUNTIFS('Canola records'!$C$2:$C$${canolaLastRow},A5,'Canola records'!$D$2:$D$${canolaLastRow},2025,'Canola records'!$F$2:$F$${canolaLastRow},\">0\")`]];
barSheet.getRange("D5:D14").fillDown();
barSheet.getRange("E5:E14").values = Array.from({ length: 10 }, () => ["'=SUMIFS(Acre-yield total,Variety,this variety,Year,2025)/SUMIFS(Acres,Variety,this variety,Year,2025)"]);
styleHeader(barSheet.getRange("A4:E4"));
styleTableBody(barSheet.getRange("A5:E14"));
barSheet.getRange("B5:B14").format.numberFormat = "0.0";
barSheet.getRange("C5:C14").format.numberFormat = "#,##0";
barSheet.getRange("D5:D14").format.numberFormat = "0";
barSheet.getRange("E5:E14").format.font = { color: greenDark, name: "Aptos Narrow", size: 9 };
barSheet.getRange("E5:E14").format.wrapText = true;
barSheet.getRange("A4:A14").format.columnWidth = 18;
barSheet.getRange("B4:B14").format.columnWidth = 23;
barSheet.getRange("C4:C14").format.columnWidth = 18;
barSheet.getRange("D4:D14").format.columnWidth = 14;
barSheet.getRange("E4:E14").format.columnWidth = 70;
barSheet.getRange("A17:C26").values = [
  ["Step", "Do this in Excel", "What it controls"],
  ["1. Select the data", "Select A4:B14, including both headers. Do not include acres, zones or formula text.", "One category column and one numeric series"],
  ["2. Insert the chart", "Insert > Column or Bar Chart > 2-D Bar > Clustered Bar.", "Horizontal bars leave room for variety names"],
  ["3. Check the source", "Chart Design > Select Data. Variety is the category label; Weighted yield is the only series.", "Prevents extra series or swapped rows and columns"],
  ["4. Change the title", "Click the title and type: 2025 yield of leading canola varieties.", "States year, measure and comparison"],
  ["5. Add the value-axis title", "Chart Design > Add Chart Element > Axis Titles > Primary Horizontal. Type: Acre-weighted yield (bu/ac).", "States the measure and unit"],
  ["6. Alter the scale", "Right-click the numbered axis > Format Axis. Set Minimum = 0, Maximum = 55 and Major unit = 10.", "Keeps bar length proportional and ticks readable"],
  ["7. Reverse category order", "Right-click the variety axis > Format Axis > Categories in reverse order if the highest value appears at the bottom.", "Puts the largest value at the top"],
  ["8. Remove the legend", "Chart Design > Add Chart Element > Legend > None. Add Outside End data labels and show one decimal place.", "Avoids repetition while preserving exact values"],
  ["9. Format the bars", "Use one fill colour. Keep light value gridlines and remove 3-D effects, shadows and heavy borders.", "Uses colour and decoration only when they help"],
];
styleHeader(barSheet.getRange("A17:C17"));
styleTableBody(barSheet.getRange("A18:C26"));
barSheet.getRange("A17:A26").format.columnWidth = 22;
barSheet.getRange("B17:B26").format.columnWidth = 70;
barSheet.getRange("C17:C26").format.columnWidth = 42;
barSheet.getRange("B18:C26").format.wrapText = true;
barSheet.getRange("A17:C26").format.autofitRows();
const barChart = barSheet.charts.add("bar", barSheet.getRange("A4:B14"));
barChart.title = "2025 yield of leading canola varieties";
barChart.hasLegend = false;
barChart.barOptions.direction = "bar";
barChart.barOptions.grouping = "clustered";
barChart.barOptions.gapWidth = 45;
barChart.xAxis = { axisType: "textAxis", textStyle: { fontSize: 9 } };
barChart.yAxis = { numberFormatCode: "0", min: 0, max: 55 };
barChart.yAxis.title.text = "Acre-weighted yield (bu/ac)";
barChart.setPosition("A29", "H50");
if (barChart.series.items.length) barChart.series.items[0].fill = green;

styleTitle(
  scatterSheet,
  "Compare provincial variety yield in 2024 and 2025",
  "Each point is one canola variety with a reported acre-weighted provincial yield in both years. Varieties missing a 2024 value are omitted rather than plotted as zero.",
);
scatterSheet.getRange("A4:C9").values = [
  ["Element", "Meaning", "Source or check"],
  ["Horizontal position", "2024 acre-weighted yield", "'Scatter plot'!K42:K113"],
  ["Vertical position", "2025 acre-weighted yield", "'Scatter plot'!L42:L113"],
  ["Points plotted", "Varieties with both annual values", null],
  ["Varieties omitted", "No reported 2024 provincial value", null],
  ["Correlation", "Linear association across complete varieties", null],
];
scatterSheet.getRange("C7").formulas = [[`=COUNT('Variety summary'!$E$${varietySummaryFirstRow}:$E$${varietySummaryLastRow})`]];
scatterSheet.getRange("C8").formulas = [[`=COUNTA('Variety summary'!$A$${varietySummaryFirstRow}:$A$${varietySummaryLastRow})-C7`]];
scatterSheet.getRange("C9").formulas = [[`=CORREL('Variety summary'!$E$${varietySummaryFirstRow}:$E$${varietySummaryLastRow},'Variety summary'!$C$${varietySummaryFirstRow}:$C$${varietySummaryLastRow})`]];
styleHeader(scatterSheet.getRange("A4:C4"));
styleTableBody(scatterSheet.getRange("A5:C9"));
scatterSheet.getRange("C7:C8").format.numberFormat = "0";
scatterSheet.getRange("C9").format.numberFormat = "0.00";
scatterSheet.getRange("A4:A9").format.columnWidth = 22;
scatterSheet.getRange("B4:B9").format.columnWidth = 42;
scatterSheet.getRange("C4:C9").format.columnWidth = 32;
scatterSheet.getRange("A12:C15").values = [
  ["Check", "Why", "In this chart"],
  ["Chart type", "An XY scatter chart treats both annual yields as measured values.", "XY scatter, not a line chart"],
  ["Missing values", "Suppressed or unavailable observations should stay blank.", "72 plotted; 25 omitted"],
  ["Pattern", "The point cloud should be inspected before adding a fitted line.", "Correlation is about 0.29"],
];
styleCheckBlock(scatterSheet, 12, 3);
scatterSheet.getRange(`J${scatterDataFirstRow - 1}:L${scatterDataLastRow}`).values = [
  ["Variety", "2024 weighted yield", "2025 weighted yield"],
  ...scatterVarieties.map((row) => [row.variety, null, null]),
];
scatterSheet.getRange(`K${scatterDataFirstRow}:L${scatterDataLastRow}`).formulas = scatterVarieties.map((row) => {
  const summaryRow = summaryRowByVariety.get(row.variety);
  return [
    `='Variety summary'!E${summaryRow}`,
    `='Variety summary'!C${summaryRow}`,
  ];
});
styleHeader(scatterSheet.getRange(`J${scatterDataFirstRow - 1}:L${scatterDataFirstRow - 1}`));
styleTableBody(scatterSheet.getRange(`J${scatterDataFirstRow}:L${scatterDataLastRow}`));
scatterSheet.getRange(`K${scatterDataFirstRow}:L${scatterDataLastRow}`).format.numberFormat = "0.0";
scatterSheet.getRange("J:J").format.columnWidth = 20;
scatterSheet.getRange("K:L").format.columnWidth = 22;
const scatterChart = scatterSheet.charts.add("scatter", {
  chartType: "scatter",
  title: "Canola variety yield: 2024 versus 2025",
  hasLegend: false,
});
const scatterSeries = scatterChart.series.add("Varieties");
scatterSeries.categoryFormula = `'Scatter plot'!$K$${scatterDataFirstRow}:$K$${scatterDataLastRow}`;
scatterSeries.formula = `'Scatter plot'!$L$${scatterDataFirstRow}:$L$${scatterDataLastRow}`;
scatterSeries.fill = blue;
scatterChart.xAxis = { numberFormatCode: "0", min: 0, max: 55 };
scatterChart.yAxis = { numberFormatCode: "0", min: 20, max: 55 };
scatterChart.xAxis.title.text = "2024 acre-weighted yield (bu/ac)";
scatterChart.yAxis.title.text = "2025 acre-weighted yield (bu/ac)";
scatterChart.setPosition("A18", "H38");

styleTitle(
  histogramSheet,
  "Distribution of reported 2025 canola variety yields",
  "The bin table counts the 674 reported risk-zone-by-variety yields in 5 bu/ac intervals. The final interval includes its upper boundary so every recorded value is counted once.",
);
const bins = Array.from({ length: 11 }, (_, i) => 15 + i * 5);
histogramSheet.getRange("A4:D15").values = [
  ["Lower bound", "Upper bound", "Reported rows", "Formula in C"],
  ...bins.map((lower, i) => {
    const upper = lower + 5;
    const row = i + 5;
    const upperTest = i === bins.length - 1 ? `\"<=\"&B${row}` : `\"<\"&B${row}`;
    return [
      lower,
      upper,
      null,
      `'=${`COUNTIFS('Canola records'!$D$2:$D$${canolaLastRow},2025,'Canola records'!$F$2:$F$${canolaLastRow},\">=\"&A${row},'Canola records'!$F$2:$F$${canolaLastRow},${upperTest})`}`,
    ];
  }),
];
for (let i = 0; i < bins.length; i += 1) {
  const row = i + 5;
  const upperOperator = i === bins.length - 1 ? "<=" : "<";
  histogramSheet.getRange(`C${row}`).formulas = [[
    `=COUNTIFS('Canola records'!$D$2:$D$${canolaLastRow},2025,'Canola records'!$F$2:$F$${canolaLastRow},\">=\"&A${row},'Canola records'!$F$2:$F$${canolaLastRow},\"${upperOperator}\"&B${row})`,
  ]];
}
styleHeader(histogramSheet.getRange("A4:D4"));
styleTableBody(histogramSheet.getRange("A5:D15"));
histogramSheet.getRange("A5:C15").format.numberFormat = "0";
histogramSheet.getRange("D5:D15").format.font = { color: greenDark, name: "Aptos Narrow", size: 9 };
histogramSheet.getRange("D5:D15").format.wrapText = true;
histogramSheet.getRange("D5:D15").format.rowHeight = 30;
histogramSheet.getRange("A4:A15").format.columnWidth = 15;
histogramSheet.getRange("B4:B15").format.columnWidth = 15;
histogramSheet.getRange("C4:C15").format.columnWidth = 16;
histogramSheet.getRange("D4:D15").format.columnWidth = 78;
histogramSheet.getRange("A18:C21").values = [
  ["Check", "Why", "In this chart"],
  ["Bin width", "Different widths can change the apparent shape.", "5 bu/ac"],
  ["Count", "The bin counts should reconcile to recorded 2025 values.", null],
  ["Range", "The first and last bins must contain the minimum and maximum.", "Observed range: 18.0 to 69.0 bu/ac"],
];
histogramSheet.getRange("C20").formulas = [["=SUM(C5:C15)"]];
styleCheckBlock(histogramSheet, 18, 3);
histogramSheet.getRange("C20").format.numberFormat = "0";
histogramSheet.getRange("J27:K38").values = [
  ["Yield interval", "Reported rows"],
  ...bins.map((lower) => [`${lower}--${lower + 5}`, null]),
];
for (let i = 0; i < bins.length; i += 1) {
  histogramSheet.getRange(`K${i + 28}`).formulas = [[`=C${i + 5}`]];
}
const histogramChart = histogramSheet.charts.add("bar", histogramSheet.getRange("J27:K38"));
histogramChart.title = "Reported 2025 canola yields (5 bu/ac bins)";
histogramChart.hasLegend = false;
histogramChart.barOptions.direction = "column";
histogramChart.barOptions.grouping = "clustered";
histogramChart.xAxis = { axisType: "textAxis", textStyle: { fontSize: 9 } };
histogramChart.yAxis = { numberFormatCode: "0", min: 0, max: 250 };
histogramChart.yAxis.title.text = "Reported risk-zone-by-variety rows";
histogramChart.setPosition("A24", "H43");
if (histogramChart.series.items.length) histogramChart.series.items[0].fill = gold;

for (const sheet of [barSheet, scatterSheet, histogramSheet, summarySheet]) {
  sheet.freezePanes.freezeRows(3);
  sheet.getUsedRange().format.font.name = "Aptos";
}
readme.getRange("A1:H14").format.font.name = "Aptos";
canolaSheet.getUsedRange().format.font.name = "Aptos";

console.log((await workbook.inspect({
  kind: "table",
  range: "'Bar chart'!A4:E14",
  include: "values,formulas",
  tableMaxRows: 14,
  tableMaxCols: 6,
})).ndjson);
console.log((await workbook.inspect({
  kind: "table",
  range: "'Scatter plot'!A4:C9",
  include: "values,formulas",
  tableMaxRows: 10,
  tableMaxCols: 5,
})).ndjson);
console.log((await workbook.inspect({
  kind: "table",
  range: "'Histogram'!A4:C21",
  include: "values,formulas",
  tableMaxRows: 22,
  tableMaxCols: 4,
})).ndjson);
console.log((await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
})).ndjson);
console.log((await workbook.inspect({ kind: "drawing", maxChars: 8000 })).ndjson);

await fs.mkdir(previewDir, { recursive: true });
const previewSpecs = [
  ["README", "A1:H14"],
  ["Bar chart", "A1:N51"],
  ["Scatter plot", "A1:N39"],
  ["Histogram", "A1:N44"],
  ["Variety summary", "A1:F24"],
  ["Canola records", "A1:G24"],
];
for (const [sheetName, range] of previewSpecs) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  const safeName = sheetName.replace(/[^a-z0-9]+/gi, "_").toLowerCase();
  await fs.writeFile(
    path.join(previewDir, `${safeName}.png`),
    new Uint8Array(await preview.arrayBuffer()),
  );
}

const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(finalOutput);
await fs.copyFile(finalOutput, projectOutput);
console.log(`CANOLA_ROWS ${canolaRows.length}`);
console.log(`VARIETIES ${varietyRows.length}`);
console.log(`SAVED ${finalOutput}`);
console.log(`COPIED ${projectOutput}`);
