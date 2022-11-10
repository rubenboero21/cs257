/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 * 
 * Modified by Ruben Boero and Serafin Patino
 */

window.onload = initialize;

function initialize() {
    loadGenerationSelector();
    loadLegendariesSelector();
    loadEggGroupsSelector();

    let generation_dropdown = document.getElementById('generation_selector');
    if (generation_dropdown) {
        generation_dropdown.onchange = onGenerationsSelectionChanged;
    }

    let legendary_dropdown = document.getElementById('legendary_selector');
    if (legendary_dropdown){
        legendary_dropdown.onchange = onLegendaryCategorySelectionChanged;
    }

    let egg_group_checkbox = document.getElementById('egg_group_selector');
    console.log('inside init: ' + egg_group_checkbox)

    if (egg_group_checkbox){
        egg_group_checkbox.onchange = onEggGroupSelectionChanged;
    }
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
    let tableBody = '';
    // Create the header of the table
    tableBody += '<tr id = "table_header"><td>Dex Number</td><td>Pokémon</td><td>Ability 1</td><td>Ability 2</td><td>Hidden Ability</td><td>Type 1</td><td>Type 2</td></tr>'
    // Create the body of the table
    for (let k = 0; k < pokemon_results.length; k++) {
    let pokemon = pokemon_results[k];
    tableBody += '<tr><td>'+ pokemon['dex_num'] + '<td>'+ pokemon['name']+ '</td>' + 
    '<td>' + pokemon['ability1']+ '</td>' + '<td>' + pokemon['ability2'] + '</td>' + 
    '<td>' + pokemon['ability3'] + '</td>' + '<td>' + pokemon['type1'] + '</td>' + 
    '<td>' + pokemon['type2']+ '</td>' + '</td></tr>\n';
    }

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

// -------Legendaries-------
function loadLegendariesSelector() {
    let url = getAPIBaseURL() + '/legendaries';

    // Send the request to the books API /legendaries endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object.
    .then((response) => response.json())

    // Once you have your list of legendaries, use it to build
    // an HTML table displaying the legendaries names and.
    .then(function(legendaries) {
        // Add the <option> elements to the <select> element
        let selectorBody = '';
        // adding a default value to be at the top of the drop down
        selectorBody += '<option value="' + '--' + '">' + '--' + '</option>\n';
        for (let k = 0; k < legendaries.length; k++) {
            let legendary_category = legendaries[k];
            selectorBody += '<option value="' + legendary_category + '">' + legendary_category + '</option>\n';
        }

        let selector = document.getElementById('legendary_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onLegendaryCategorySelectionChanged() {
    let legendary_category = this.value; 

    let url = getAPIBaseURL() + '/legendaries/' + legendary_category;

    fetch(url, {method: 'get'})

    // getting the dictionary
    .then((response) => response.json())

    .then(function(pokemon_results) {
        let tableBody = '';
        // Create the header of the table
        tableBody += '<tr id = "table_header"><td>Dex Number</td><td>Pokémon</td><td>Ability 1</td><td>Ability 2</td><td>Hidden Ability</td><td>Type 1</td><td>Type 2</td><td>Generation</td></tr>'
        // Create the body of the table
        for (let k = 0; k < pokemon_results.length; k++) {
            let pokemon = pokemon_results[k];
            tableBody += '<tr><td>'+ pokemon['dex_num'] + '<td>'+ pokemon['name']+ '</td>' + 
            '<td>' + pokemon['ability1']+ '</td>' + '<td>' + pokemon['ability2'] + '</td>' + 
            '<td>' + pokemon['ability3'] + '</td>' + '<td>' + pokemon['type1'] + '</td>' + 
            '<td>' + pokemon['type2']+ '</td>' + '<td>' + pokemon['generation'] + '</td>' + '</td></tr>\n';
        }

        // Put the table body we just built inside the table that's already on the page.
        let legendariesTable = document.getElementById('legendary_table');
        if (legendariesTable) {
            legendariesTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

// -------Egg_Groups-------
function loadEggGroupsSelector() {
    let url = getAPIBaseURL() + '/egg_groups';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(egg_groups) {
        let selectorBody = '';

        // start at k = 1 bc the first egg group is a null value
        for (let k = 1; k < egg_groups.length; k++) {
            let egg_group = egg_groups[k];
            // every 2nd egg group ends a row
            if (k % 2 == 0 && k != 0) {
                selectorBody += '<td><input type="checkbox" id="' + egg_group + '" name="' + egg_group + '"/>' + egg_group + '</td></tr>'
            }
            else {
                selectorBody += '<td><input type="checkbox" id="' + egg_group + '" name="' + egg_group + '"/>' + egg_group + '</td>';
            }
        }

        let selector = document.getElementById('egg_group_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onEggGroupSelectionChanged() {
    let egg_group = this.value; 
    egg_group = 'Field'

    console.log("inside change " + egg_group)
    let url = getAPIBaseURL() + '/egg_group/' + egg_group;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(pokemon_results) {
        let tableBody = '';
        // Create the header of the table
        tableBody += '<tr id = "table_header"><td>Dex Number</td><td>Pokémon</td><td>Ability 1</td><td>Ability 2</td><td>Hidden Ability</td><td>Type 1</td><td>Type 2</td><td>Generation</td></tr>'
        // Create the body of the table
        for (let k = 0; k < pokemon_results.length; k++) {
            let pokemon = pokemon_results[k];
            tableBody += '<tr><td>'+ pokemon['dex_num'] + '<td>'+ pokemon['name']+ '</td>' + 
            '<td>' + pokemon['ability1']+ '</td>' + '<td>' + pokemon['ability2'] + '</td>' + 
            '<td>' + pokemon['ability3'] + '</td>' + '<td>' + pokemon['type1'] + '</td>' + 
            '<td>' + pokemon['type2']+ '</td>' + '<td>' + pokemon['generation'] + '</td>' + '</td></tr>\n';
        }

        let eggGroupResults = document.getElementById('egg_group_results');
        if (eggGroupResults) {
            eggGroupResults.innerHTML = tableBody;
        }
        })

    .catch(function(error) {
    console.log(error);
    });
}
