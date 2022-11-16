/*
 * simple-charts.js
 * Jeff Ondich, 12 November 2020
 *
 * Adapted from the Chartist library samples.
 *   https://gionkunz.github.io/chartist-js/examples.html
 */

window.onload = initialize;

function initialize() {
    createBarChart();
}

function createBarChart() {
    let hp = parseInt(document.getElementById('hp').innerText);
    let atk = parseInt(document.getElementById('atk').innerText);
    let def = parseInt(document.getElementById('def').innerText);
    let spatk = parseInt(document.getElementById('spatk').innerText);
    let spdef = parseInt(document.getElementById('spdef').innerText);
    let spd = parseInt(document.getElementById('spd').innerText);

    var data = {
        labels: ['HP', 'ATK ', 'DEF','SP. ATK','SP. DEF', 'SPD'],
        series: [[hp, atk, def, spatk, spdef, spd]]

    };

    var options = {horizontalBars: true, reverseData: true,   axisY: {offset: 80}}

    new Chartist.Bar('#stats_chart', data, options);

    // new Chartist.Bar('.ct-chart', {
    //     labels: ['HP', 'ATK', 'DEF', 'SP. ATK', 'SP. DEF', 'SPD'],
    //     series: [
    //       [hp, atk, def, spatk, spdef, spd],
    //     ]
    //   }, {
    //     seriesBarDistance: 10,
    //     reverseData: true,
    //     horizontalBars: true,
    //     // axisY: {
    //     //   offset: 70
    //     // }
    //   });
}


