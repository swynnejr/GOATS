async function getParksData() {
    const myURL = new URL(window.location.href);

    const search = myURL.search;
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch(`https://developer.nps.gov/api/v1/parks${search}&api_key=flnFWDil6yBHjlym5jScVjFCzNbVPErCIBA2zdGx`);
    // We then need to convert the data into JSON format.
    var parksData = await response.json();
    console.log(myURL)
    console.log(search)
    return parksData;
}
    
console.log(getParksData());