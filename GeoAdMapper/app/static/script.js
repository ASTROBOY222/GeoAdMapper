async function fetchCoordinates() {
    try {
        const response = await fetch("/coordinates"); // Fetch from Flask API
        const data = await response.json();
        return data.coordinates; // Accessing "coordinates" key
    } catch (error) {
        console.error("Error fetching coordinates:", error);
        return [];
    }
}

window.initMap = async function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 1,
        center: { lat: 37.7749, lng: -122.4194 }, // Default center
    });

    const coordinates = await fetchCoordinates();

    coordinates.forEach(coord => {
        new google.maps.Marker({
            position: coord,
            map: map,
        });
    });
};
