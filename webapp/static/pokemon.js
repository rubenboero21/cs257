/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 * 
 * Modified by Ruben Boero and Serafin Patino
 */

window.onload = initialize;

var alternatingLineColor = '#E2FCFF'

function initialize() {
    loadGenerationSelector();
    loadLegendariesSelector();
    loadEggGroupsSelector();
    loadTypesSelector();

    let generation_dropdown = document.getElementById('generation_selector');
    if (generation_dropdown) {
        generation_dropdown.onchange = onGenerationsSelectionChanged;
    }

    let legendary_dropdown = document.getElementById('legendary_selector');
    if (legendary_dropdown){
        legendary_dropdown.onchange = onLegendaryCategorySelectionChanged;
    }

    let go_button = document.getElementById('go_button');
    if (go_button){
        go_button.onclick = onGoButtonClicked;
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
        + pokemon['dark_resist'] + '/' + pokemon['steel_resist'] + '/' + pokemon['fairy_resist']

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
        let tableBody = createTableHTML(pokemon_results, alternatingLineColor)

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
// -------Types-------
function loadTypesSelector() {
    let url = getAPIBaseURL() + '/types';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(types) {
        let selectorBody = '';

        // start at k = 1 bc the first egg group is a null value
        for (let k = 1; k < types.length; k++) {
            let type = types[k];
            // using type radio to only allow one button to be selected at once
            // every 6th type ends a row
            if (k % 6 == 0) {
                selectorBody += '<td><input type="radio" onchange="onTypeSelectionChanged(event)" id="' + type + '" name="type_box"/>' + type + '</td></tr>'
            }
            else {
                selectorBody += '<td><input type="radio" onchange="onTypeSelectionChanged(event)" id="' + type + '" name="type_box"/>' + type + '</td>';
            }
            // onchange calls a function when the radio button is clicked
        }

        let selector = document.getElementById('type_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onTypeSelectionChanged(event) {
    // event is the context around clicking the box
    // target is the check box, target.id is the text
    type = event.target.id

    let url = getAPIBaseURL() + '/type/' + type;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(pokemon_results) {
        let tableBody = createTableHTML(pokemon_results, alternatingLineColor)

        let typeResults = document.getElementById('type_results');
        if (typeResults) {
            typeResults.innerHTML = tableBody;
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
            // using type radio to only allow one button to be selected at once
            // every 2nd egg group ends a row
            if (k % 2 == 0) {
                selectorBody += '<td><input type="radio" onchange="onEggGroupSelectionChanged(event)" id="' + egg_group + '" name="egg_box"/>' + egg_group + '</td></tr>'
            }
            else {
                selectorBody += '<td><input type="radio" onchange="onEggGroupSelectionChanged(event)" id="' + egg_group + '" name="egg_box"/>' + egg_group + '</td>';
            }
            // onchange calls a function when the radio button is clicked
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

function onEggGroupSelectionChanged(event) {
    // event is the context around clicking the box
    // target is the check box, target.id is the text
    egg_group = event.target.id

    let url = getAPIBaseURL() + '/egg_group/' + egg_group;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(pokemon_results) {
        let tableBody = createTableHTML(pokemon_results, alternatingLineColor)

        let eggGroupResults = document.getElementById('egg_group_results');
        if (eggGroupResults) {
            eggGroupResults.innerHTML = tableBody;
        }
        })

    .catch(function(error) {
    console.log(error);
    });
}

// -------Search Bar-------
function onSearchDropdownSelectionChanged() {
    let search_category = this.value;
    console.log(search_category)
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
    console.log(url)
    window.location.href = url
}
