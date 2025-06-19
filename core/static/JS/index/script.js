function loadContent(url, activeId, scriptPath = null) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById("main-content").innerHTML = html;
            if (activeId) setActiveTab(activeId);

            // Charger JS spécifique si c'est manage-events
            if (scriptPath) {
                const script = document.createElement("script");
                script.src = scriptPath;
                script.type = "module"; // ou "text/javascript"
                document.body.appendChild(script);
            }
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

document.addEventListener("DOMContentLoaded", () => {
    // Délégation d'événements pour fermer la modale
    const modalContainer = document.getElementById("modal-container");
  
    modalContainer.addEventListener("click", function (e) {
      // Si l'élément cliqué est le bouton ou contient le bouton
      if (e.target.id === "close-modal" || e.target.closest("#close-modal")) {
        closeModal();
      }
    });
  });
  
  // Fonction pour fermer une modale
  function closeModal() {
    document.getElementById("modal-container").innerHTML = "";
  }


document.getElementById("manage-resources").addEventListener("click", () => {
    loadContent("/partials/manage-resources/", "manage-resources");
});

document.getElementById("manage-events").addEventListener("click", () => {
    loadContent("/partials/manage-events/", "manage-events", "/static/js/manage_events/create_events.js");
});

document.getElementById("notifications").addEventListener("click", () => {
    loadContent("/partials/notifications/", "notifications");
});