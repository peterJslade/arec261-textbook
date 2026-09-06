import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = "/Users/pjs998/Library/CloudStorage/OneDrive-UniversityofSaskatchewan/Teaching/261/2026/textbook_261";
const sourcePath = path.join(root, "practice/data/module03/q19_canola_years_wide.csv");
const outputDir = path.join(root, "outputs/q19_excel_solution_20260904");
const outputPath = path.join(outputDir, "m03_q19_excel_solution.xlsx");
const integratedPath = path.join(root, "practice/answers/m03_q19_excel_solution.xlsx");
const previewDir = path.join(root, "tmp/q19_excel_solution/previews");

const csv = (await fs.readFile(sourcePath, "utf8")).trim().split(/\r?\n/).map(line => line.split(","));
const headers = csv[0];
const rawRows = csv.slice(1).map(row => [row[0], ...row.slice(1).map(Number)]);

const longRows = [];
for (const row of rawRows) {
  for (let c = 1; c < headers.length; c++) {
    longRows.push([row[0], Number(headers[c].replace("yield_", "")), row[c]]);
  }
}

const font = "Arial";
const green = "#4B7F5B";
const darkGreen = "#355E45";
const paleGreen = "#E2F0D9";
const paleYellow = "#FFF2CC";
const paleBlue = "#DDEBF7";
const lightGray = "#F2F2F2";
const border = "#B7C9BD";
const body = "#24302A";

const wb = Workbook.create();
const question = wb.worksheets.add("Question 19");
const raw = wb.worksheets.add("Raw Data");
const answer = wb.worksheets.add("Answer");
const steps = wb.worksheets.add("Power Query Steps");

for (const sheet of [question, raw, answer, steps]) {
  sheet.showGridLines = false;
  sheet.getRange("A1:K80").format.font = { name: font, size: 11, color: body };
}

function title(sheet, range, text) {
  sheet.mergeCells(range);
  const cell = sheet.getRange(range);
  cell.values = [[text]];
  cell.format = {
    fill: green,
    font: { name: font, size: 18, bold: true, color: "#FFFFFF" },
    verticalAlignment: "center",
  };
  cell.format.rowHeight = 34;
}

function sectionHeader(range) {
  range.format = {
    fill: darkGreen,
    font: { name: font, size: 11, bold: true, color: "#FFFFFF" },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: darkGreen },
  };
  range.format.rowHeight = 25;
}

// Question sheet
title(question, "A1:F1", "Question 19 — Excel and Power Query");
question.mergeCells("A3:F3");
question.getRange("A3").values = [["Use q19_canola_years_wide.csv. Complete the work in Excel using Power Query and keep the queries attached to the submitted workbook."]];
question.getRange("A3:F3").format = { fill: paleGreen, font: { name: font, size: 11, italic: true, color: body }, wrapText: true, verticalAlignment: "center" };
question.getRange("A3:F3").format.rowHeight = 42;
question.getRange("A5:B5").values = [["Part", "Required work"]];
sectionHeader(question.getRange("A5:F5"));
const qRows = [
  ["(a)", "Import the file with Power Query and reshape it from wide to long. The result must contain field, year, and yield_bu_ac. State what one row represents."],
  ["(b)", "Change year from text such as yield_2021 to the whole number 2021. Give the query a meaningful name and load the long table to a worksheet."],
  ["(c)", "Create a second query that starts from the long query. Compute mean yield by year, sort from highest to lowest, and report the best year."],
];
for (let i = 0; i < qRows.length; i++) {
  const r = 6 + i;
  question.mergeCells(`B${r}:F${r}`);
  question.getRange(`A${r}:F${r}`).format = {
    fill: i % 2 === 0 ? "#FFFFFF" : lightGray,
    font: { name: font, size: 11, color: body },
    wrapText: true,
    verticalAlignment: "top",
    borders: { bottom: { style: "thin", color: border } },
  };
  question.getRange(`A${r}`).values = [[qRows[i][0]]];
  question.getRange(`A${r}`).format.font = { name: font, size: 11, bold: true, color: body };
  question.getRange(`B${r}`).values = [[qRows[i][1]]];
  question.getRange(`A${r}:F${r}`).format.rowHeight = 52;
}
question.mergeCells("A11:F11");
question.getRange("A11").values = [["Submission check: the workbook should contain the original data, the loaded long table, the yearly summary, and both queries with readable Applied Step names."]];
question.getRange("A11:F11").format = { fill: paleYellow, font: { name: font, size: 11, bold: true, color: body }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#D6B656" } };
question.getRange("A11:F11").format.rowHeight = 42;
question.getRange("A:A").format.columnWidth = 11;
question.getRange("B:F").format.columnWidth = 18;
question.freezePanes.freezeRows(1);

// Raw data sheet
title(raw, "A1:F1", "Question 19 — Raw Data");
raw.mergeCells("A2:F2");
raw.getRange("A2").values = [["Original wide table. Keep this table unchanged. The Excel table is named RawData."]];
raw.getRange("A2:F2").format = { fill: paleGreen, font: { name: font, size: 10, italic: true, color: body }, wrapText: true };
raw.getRange("A4:F12").values = [headers, ...rawRows];
const rawTable = raw.tables.add("A4:F12", true, "RawData");
rawTable.style = "TableStyleMedium4";
raw.getRange("B5:F12").setNumberFormat("0.0");
raw.getRange("A4:F4").format.font = { name: font, size: 11, bold: true, color: "#FFFFFF" };
raw.getRange("A:A").format.columnWidth = 18;
raw.getRange("B:F").format.columnWidth = 15;
raw.freezePanes.freezeRows(4);

// Answer sheet
title(answer, "A1:H1", "Question 19 — Expected Output");
answer.mergeCells("A2:H2");
answer.getRange("A2").values = [["The long table should contain 40 rows: one row for each field–year combination. The yearly summary is derived from the long table."]];
answer.getRange("A2:H2").format = { fill: paleGreen, font: { name: font, size: 10, italic: true, color: body }, wrapText: true };
answer.getRange("A4:C44").values = [["field", "year", "yield_bu_ac"], ...longRows];
const longTable = answer.tables.add("A4:C44", true, "ExpectedLongData");
longTable.style = "TableStyleMedium4";
answer.getRange("B5:B44").setNumberFormat("0");
answer.getRange("C5:C44").setNumberFormat("0.0");
answer.getRange("E4:F4").values = [["year", "mean_yield"]];
sectionHeader(answer.getRange("E4:F4"));
answer.getRange("A4:C4").format.font = { name: font, size: 11, bold: true, color: "#FFFFFF" };
answer.getRange("E5:E9").values = [[2024], [2023], [2021], [2025], [2022]];
answer.getRange("F5").formulas = [["=AVERAGEIF($B$5:$B$44,E5,$C$5:$C$44)"]];
answer.getRange("F5:F9").fillDown();
answer.getRange("F5:F9").setNumberFormat("0.00");
answer.getRange("E5:F9").format.borders = { insideHorizontal: { style: "thin", color: border }, bottom: { style: "thin", color: border } };
answer.getRange("E11:F11").values = [["Best year", "Mean yield (bu/ac)"]];
sectionHeader(answer.getRange("E11:F11"));
answer.getRange("E12").formulas = [["=INDEX(E5:E9,MATCH(MAX(F5:F9),F5:F9,0))"]];
answer.getRange("F12").formulas = [["=MAX(F5:F9)"]];
answer.getRange("E12:F12").format = { fill: paleYellow, font: { name: font, size: 12, bold: true, color: body }, borders: { preset: "outside", style: "thin", color: "#D6B656" } };
answer.getRange("E12").setNumberFormat("0");
answer.getRange("F12").setNumberFormat("0.00");
answer.mergeCells("E14:H15");
answer.getRange("E14").values = [["Answer: 2024 has the highest mean canola yield, approximately 41.96 bu/ac."]];
answer.getRange("E14:H15").format = { fill: paleBlue, font: { name: font, size: 11, bold: true, color: body }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#7EA6C4" } };
answer.getRange("A:A").format.columnWidth = 18;
answer.getRange("B:B").format.columnWidth = 11;
answer.getRange("C:C").format.columnWidth = 16;
answer.getRange("D:D").format.columnWidth = 4;
answer.getRange("E:F").format.columnWidth = 19;
answer.getRange("G:H").format.columnWidth = 14;
answer.freezePanes.freezeRows(4);

// Power Query instructions and exact M code
title(steps, "A1:D1", "Question 19 — Power Query Steps");
steps.mergeCells("A2:D2");
steps.getRange("A2").values = [["This answer is self-contained, so its M code reads the RawData table. On the test, begin with Data → Get Data → From Text/CSV. Use Data → Queries & Connections to inspect live queries."]];
steps.getRange("A2:D2").format = { fill: paleGreen, font: { name: font, size: 10, italic: true, color: body }, wrapText: true };
steps.getRange("A4:D4").values = [["Step", "Student action", "Applied Step name", "Check"]];
sectionHeader(steps.getRange("A4:D4"));
const stepRows = [
  [1, "Select RawData and choose Data → From Table/Range.", "Source", "The editor shows 8 fields and 6 columns."],
  [2, "Set field to Text and each yield column to Decimal Number.", "Set column types", "Identifiers and yields have the correct types."],
  [3, "Select field, then choose Transform → Unpivot Other Columns.", "Unpivot year columns", "The table has 40 rows and three columns."],
  [4, "Rename Attribute to year and Value to yield_bu_ac.", "Rename columns", "The output names match the question."],
  [5, "Extract the text after the underscore from year, then set it to Whole Number.", "Extract numeric year", "year contains 2021 through 2025 as numbers."],
  [6, "Name the query CanolaYieldsLong and load it as a table.", "Load long table", "The long output is visible in Excel."],
  [7, "Create a Reference from CanolaYieldsLong; group by year using Average of yield_bu_ac.", "Mean yield by year", "The summary contains five years."],
  [8, "Sort mean_yield descending; name the query MeanYieldByYear and load it.", "Sort best year first", "2024 is first at 41.96 bu/ac."],
];
steps.getRange("A5:D12").values = stepRows;
steps.getRange("A5:D12").format = { font: { name: font, size: 10, color: body }, wrapText: true, verticalAlignment: "top", borders: { insideHorizontal: { style: "thin", color: border }, bottom: { style: "thin", color: border } } };
steps.getRange("A5:A12").format.horizontalAlignment = "center";
steps.getRange("A5:D12").format.rowHeight = 46;
steps.mergeCells("A14:D14");
steps.getRange("A14").values = [["M code — CanolaYieldsLong"]];
sectionHeader(steps.getRange("A14:D14"));
const longCode = [
  "let",
  "    Source = Excel.CurrentWorkbook(){[Name=\"RawData\"]}[Content],",
  "    #\"Set column types\" = Table.TransformColumnTypes(Source, {{\"field\", type text}, {\"yield_2021\", type number}, {\"yield_2022\", type number}, {\"yield_2023\", type number}, {\"yield_2024\", type number}, {\"yield_2025\", type number}}),",
  "    #\"Unpivot year columns\" = Table.UnpivotOtherColumns(#\"Set column types\", {\"field\"}, \"Attribute\", \"Value\"),",
  "    #\"Rename columns\" = Table.RenameColumns(#\"Unpivot year columns\", {{\"Attribute\", \"year\"}, {\"Value\", \"yield_bu_ac\"}}),",
  "    #\"Extract numeric year\" = Table.TransformColumns(#\"Rename columns\", {{\"year\", each Number.FromText(Text.AfterDelimiter(_, \"_\")), Int64.Type}})",
  "in",
  "    #\"Extract numeric year\"",
];
let codeRow = 15;
for (const line of longCode) {
  steps.mergeCells(`A${codeRow}:D${codeRow}`);
  steps.getRange(`A${codeRow}`).values = [[line]];
  steps.getRange(`A${codeRow}:D${codeRow}`).format = { fill: lightGray, font: { name: "Courier New", size: 9, color: body }, wrapText: true, verticalAlignment: "center" };
  steps.getRange(`A${codeRow}:D${codeRow}`).format.rowHeight = line.length > 160 ? 34 : 20;
  codeRow++;
}
codeRow++;
steps.mergeCells(`A${codeRow}:D${codeRow}`);
steps.getRange(`A${codeRow}`).values = [["M code — MeanYieldByYear"]];
sectionHeader(steps.getRange(`A${codeRow}:D${codeRow}`));
codeRow++;
const summaryCode = [
  "let",
  "    Source = CanolaYieldsLong,",
  "    #\"Mean yield by year\" = Table.Group(Source, {\"year\"}, {{\"mean_yield\", each List.Average([yield_bu_ac]), type number}}),",
  "    #\"Sort best year first\" = Table.Sort(#\"Mean yield by year\", {{\"mean_yield\", Order.Descending}})",
  "in",
  "    #\"Sort best year first\"",
];
for (const line of summaryCode) {
  steps.mergeCells(`A${codeRow}:D${codeRow}`);
  steps.getRange(`A${codeRow}`).values = [[line]];
  steps.getRange(`A${codeRow}:D${codeRow}`).format = { fill: lightGray, font: { name: "Courier New", size: 9, color: body }, wrapText: true, verticalAlignment: "center" };
  steps.getRange(`A${codeRow}:D${codeRow}`).format.rowHeight = line.length > 140 ? 34 : 20;
  codeRow++;
}
steps.getRange("A:A").format.columnWidth = 9;
steps.getRange("B:B").format.columnWidth = 44;
steps.getRange("C:C").format.columnWidth = 25;
steps.getRange("D:D").format.columnWidth = 32;
steps.freezePanes.freezeRows(4);

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outputPath);
await fs.copyFile(outputPath, integratedPath);

const inspect = await wb.inspect({ kind: "workbook,sheet,table", maxChars: 9000, tableMaxRows: 8, tableMaxCols: 8, tableMaxCellChars: 120 });
await fs.writeFile(path.join(previewDir, "inspect.ndjson"), inspect.ndjson, "utf8");
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!", options: { useRegex: true, maxResults: 200 }, summary: "final formula error scan" });
await fs.writeFile(path.join(previewDir, "errors.ndjson"), errors.ndjson, "utf8");

for (const [sheetName, range] of [["Question 19", "A1:F11"], ["Raw Data", "A1:F12"], ["Answer", "A1:H20"], ["Power Query Steps", `A1:D${codeRow - 1}`]]) {
  const image = await wb.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(" ", "_")}.png`), new Uint8Array(await image.arrayBuffer()));
}

console.log(JSON.stringify({ outputPath, integratedPath, rows: longRows.length }, null, 2));
