/**
 * Build yearly technology stats
 *
 * @param {object} techStats StackOverfow stats
 * @returns {object} Year by year stats of technologies mentioned in StackOverflow
 */
function buildYearlyTechStats (techStats) {
  let yearStats = {};
  for(const [year, stats] of Object.entries(techStats)) {
    for(const [label, labelStat] of Object.entries(stats)){
      if(label.startsWith("current")) {
        if(yearStats[year] == null) {
          yearStats[year] = labelStat;
        } else {
          if(labelStat == null) {
            continue;
          } else {
            for(const [tech, num] of Object.entries(labelStat)) {
              yearStats[year][tech] = num;
            }
            yearStats[year]
          }
        }        
      } else {
        continue;
      }
    }
  }
  console.log(yearStats);
  return yearStats;
}

/**
 * Update table contents
 *
 * @param {HTMLTableElement} table DOM element for the table
 * @param {object} yearlyTechStats Year by year stats of technologies mentioned in StackOverflow
 * @param {Array<string>} selectedTechs Technologies selected
 * @param {number} firstYear First year of data selected
 * @param {number} lastYear Last year of data selected
 */
function updateTable (table, yearlyTechStats, selectedTechs, firstYear, lastYear) {
  let headings = [];
  headings[0] = "Technology";
  for(i=firstYear; i <= lastYear; ++i) {
    headings[i - firstYear + 1] = i
  }
  table.tHead.innerHTML = constructTableHeadHtml(headings);

  table.tBodies[0].innerHTML = constructTableRowsHtml(buildRowData(yearlyTechStats, 
    selectedTechs, firstYear, lastYear));
}

/**
 * Build row data to be shown in a table
 *
 * @param {object} yearlyTechStats Year by year stats of technologies mentioned in StackOverflow
 * @param {Array<string>} selectedTechs Technologies selected
 * @param {number} firstYear First year of data selected
 * @param {number} lastYear Last year of data selected
 * @returns {Array<string|number>}
 */
function buildRowData (yearlyTechStats, selectedTechs, firstYear, lastYear) {
  var rowData = [];
  for (i=0; i < selectedTechs.length; ++i) {
    newRow = [];
    newRow[0] = selectedTechs[i];
    rowData[i] = newRow;
  }
  Object.entries(yearlyTechStats).map(yearStat => {
    if(yearStat[0] >= firstYear && yearStat[0] <= lastYear) {
      for(i=0; i<rowData.length; ++i) {
        let tech = selectedTechs[i];
        let num = 0;
        for(const [t, n] of Object.entries(yearStat[1])) {
          if(t == tech) {
            num = n;
          }
        }
        if(num == 0) {
          rowData[i].push(num);
        } else {
        rowData[i].push(num);
        }
      }
    }
  });

  return rowData;
}

/**
 * Get HTML of table rows
 *
 * @param {Array<string|number>} rowData
 * @returns {string} HTML of the table rows
 */
function constructTableRowsHtml (rowData) {
  let string = "";
  for(i = 0; i < rowData.length; ++i) {
    string += "<tr>";
    for(j = 0; j < rowData[i].length; ++j) {
      string+= "<td>" + rowData[i][j] + "</td>";
    }
    string += "</tr>";
  }
  return string;
}

/**
 * Get HTML of table heading row
 *
 * @param {Array<string|number>} headings Table headings
 * @returns {string} HTML of the heading row
 */
function constructTableHeadHtml (headings) {
  let string = "<tr>";
  for(i = 0; i < headings.length; ++i) {
    string += "<th>" + headings[i] + "</th>";
  }
  string += "</tr>";
  return string;
}
