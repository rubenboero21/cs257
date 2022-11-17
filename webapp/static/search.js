/*
 * pokemon.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 * 
 * Modified by Ruben Boero and Serafin Patino
 */

window.onload = initialize;

function initialize() {
    let legendary_dropdown = document.getElementById('legendary_selector');
    if (legendary_dropdown){
        legendary_dropdown.onchange = onLegendaryCategorySelectionChanged;
    }

    let go_button = document.getElementById('go_button');
    if (go_button){
        go_button.onclick = onGoButtonClicked;
    }

    let search_bar = document.getElementById('search_bar');
    if (search_bar) {
        search_bar.addEventListener('keyup', function(event){
            event.preventDefault();
            if (event.keyCode === 13) {
                go_button.click();
            }
        })
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