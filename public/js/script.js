
const socket = io();

if (navigator.geolocation) {
    navigator.geolocation.watchPosition(
        (position) => {
            const { latitude, longitude } = position.coords;
            socket.emit("send-location", { latitude, longitude });
        },
        (error) => {
            console.error(error);
            if (error.code === 2) {
                console.warn(
                    "Position update temporarily unavailable. Retrying..."
                );
            }
        },
        {
            enableHighAccuracy: true,
            timeout: 20000,
            maximumAge: 0,
        }
    );
}

const map = L.map("map").setView([0, 0], 10);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© Ayush",
}).addTo(map);
const markers = {}
socket.on("receiver-location", (data) => {
    const { id, latitude, longitude } = data;
    map.setView([latitude, longitude], 16);
    if (markers[id]) {
        markers[id].setLatLng([latitude, longitude]);
    }
    else {
        markers[id] = L.marker([latitude, longitude]).addTo(map);
    }
}
);
socket.on("user-disconnected", (id) => {
    if (markers[id]) {
        map.removeLayer(markers[id]);
        delete markers[id];

    }
});