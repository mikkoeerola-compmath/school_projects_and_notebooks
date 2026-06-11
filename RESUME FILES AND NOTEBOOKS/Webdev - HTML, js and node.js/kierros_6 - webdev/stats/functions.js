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
