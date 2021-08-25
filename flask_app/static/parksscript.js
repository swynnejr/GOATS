async function getParksData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch(`https://developer.nps.gov/api/v1/parks?stateCode=${{search}}&api_key=flnFWDil6yBHjlym5jScVjFCzNbVPErCIBA2zdGx`);
    // We then need to convert the data into JSON format.
    var parksData = await response.json();
    return parksData;
}
    
console.log(getParksData());