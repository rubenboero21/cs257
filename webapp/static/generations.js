/*
 * generations.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 * 
 * Modified by Ruben Boero and Serafin Patino
 */

window.onload = initialize;

var alternatingLineColor = '#E2FCFF'

function initialize() {
    loadGenerationSelector();

    let generation_dropdown = document.getElementById('generation_selector');
    if (generation_dropdown) {
        generation_dropdown.onchange = onGenerationsSelectionChanged;
    }

    let go_button = document.getElementById('go_button');
    if (go_button){
        go_button.onclick = onGoButtonClicked;
    }
}

// Returns the HTML for the table to display search results
function createTableHTML(search_results, alternatingLineColor) {
    let tableBody = '';

    // Create the header of the table
    tableBody += '<tr id = "table_header"><td>Dex Number</td><td>Pokémon</td><td>Ability 1</td><td>Ability 2</td><td>Hidden Ability</td><td>Type 1</td><td>Type 2</td><td>Generation</td></tr>'
    // Create the body of the table
    for (let k = 0; k < search_results.length; k++) {
        let pokemon = search_results[k];

        let url = pokemon['dex_num'] + '/' + pokemon['name'] + '/' + pokemon['ability1'] + '/' + pokemon['ability2']
        + '/' + pokemon['ability3'] + '/' + pokemon['type1'] + '/' + pokemon['type2'] + '/' + pokemon['generation'] + '/'
        + pokemon['height'] + '/' + pokemon['weight'] + '/' + pokemon['normal_resist'] + '/' + pokemon['fire_resist'] + '/' + pokemon['water_resist'] + '/'
        + pokemon['electric_resist'] + '/' + pokemon['grass_resist'] + '/' + pokemon['ice_resist'] + '/' 
        + pokemon['fighting_resist'] + '/' + pokemon['poison_resist'] + '/' + pokemon['ground_resist'] + '/'
        + pokemon['flying_resist'] + '/' + pokemon['psychic_resist'] + '/' + pokemon['bug_resist'] + '/'
        + pokemon['rock_resist'] + '/' + pokemon['ghost_resist'] + '/' + pokemon['dragon_resist'] + '/'
        + pokemon['dark_resist'] + '/' + pokemon['steel_resist'] + '/' + pokemon['fairy_resist'] + '/'
        + pokemon['hp'] + '/' + pokemon['atk'] + '/' + pokemon['def'] + '/' + pokemon['spatk'] + '/'
        + pokemon['spdef'] + '/' + pokemon['spd']

        if (k % 2 == 0) {
            tableBody += '<tr><td>'+ pokemon['dex_num'] + '<td><a href = "' + url + '">'+ pokemon['name'] + '</a></td>' + 
            '<td>' + pokemon['ability1'] + '</td>' + '<td>' + pokemon['ability2'] + '</td>' + 
            '<td>' + pokemon['ability3'] + '</td>' + '<td>' + pokemon['type1'] + '</td>' + 
            '<td>' + pokemon['type2']+ '</td>' + '<td>' + pokemon['generation'] + '</td>' + '</td></tr>\n';
        } 
        else {
            tableBody += '<tr bgcolor="' + alternatingLineColor + '"><td>'+ pokemon['dex_num'] + '<td><a href = "' + 
            url + '">'+ pokemon['name'] + '</a>' + '<td>' + pokemon['ability1'] + '</td>' + '<td>' + 
            pokemon['ability2'] + '</td>' + '<td>' + pokemon['ability3'] + '</td>' + '<td>' + pokemon['type1'] + 
            '</td>' + '<td>' + pokemon['type2']+ '</td>' + '<td>' + pokemon['generation'] + '</td>' + '</td></tr>\n';
        }        
    }
    return tableBody
}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

// -------Generations-------
function loadGenerationSelector() {
    let url = getAPIBaseURL() + '/generations';

    // Send the request to the books API /generations endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object.
    .then((response) => response.json())

    // Once you have your list of generations, use it to build
    // an HTML table displaying the generation namess and.
    .then(function(generations) {
        // Add the <option> elements to the <select> element
        let selectorBody = '';
        // adding a default value to be at the top of the drop down
        selectorBody += '<option value="' + '--' + '">' + '--' + '</option>\n';
        for (let k = 0; k < generations.length; k++) {
            let generation = generations[k];
            selectorBody += '<option value="' + generation + '">' + generation + '</option>\n';
        }

        let selector = document.getElementById('generation_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onGenerationsSelectionChanged() {
    let generation_name = this.value; 
    let url = getAPIBaseURL() + '/generation/' + generation_name;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(pokemon_results) {
        let tableBody = createTableHTML(pokemon_results, alternatingLineColor)

    // Put the table body we just built inside the table that's already on the page.
    let generationsTable = document.getElementById('generation_table');
    if (generationsTable) {
    generationsTable.innerHTML = tableBody;
    }
    })

    .catch(function(error) {
    console.log(error);
    });
}

function onGoButtonClicked() { 
    var search_text = document.getElementById('search_bar').value
    var search_dropdown = document.getElementById('search_dropdown');
    var search_category = search_dropdown.value;

    // we really want search text to be optional, but we couldnt figure
    // out how to make it work with the API call, so we did this instead
    if (search_text == '') {
        search_text = 'default'
    }
    let url = '/search_results/' + search_category + '/' + search_text;
    window.location.href = url
}