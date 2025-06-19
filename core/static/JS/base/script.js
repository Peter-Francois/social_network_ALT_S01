function loadContent(url, activeId) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById("main-content").innerHTML = html;
            setActiveTab(activeId);
        })
        .catch(error => {
            console.error("Erreur lors du chargement du contenu :", error);
        });
}

function setActiveTab(id) {
    const tabs = document.querySelectorAll(".tab");
    tabs.forEach(tab => {
        tab.classList.remove("border-b-2","border-blue-600");
        tab.classList.add("text-gray-500", "hover:text-gray-700", "hover:bg-gray-50");
    });
    document.getElementById(id).classList.add("border-b-2","border-blue-600","text-blue-600");
    document.getElementById(id).classList.remove("text-gray-500", "hover:text-gray-700", "hover:bg-gray-50");
}


document.getElementById("manage-resources").addEventListener("click", () => {
    loadContent("/partials/manage-resources/", "manage-resources");
});

document.getElementById("manage-events").addEventListener("click", () => {
    loadContent("/partials/manage-events/", "manage-events");
});

document.getElementById("notifications").addEventListener("click", () => {
    loadContent("/partials/notifications/", "notifications");
});