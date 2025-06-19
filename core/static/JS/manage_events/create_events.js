/* bug : quand je charge la première fois la page manage-events, le script est chargé et le modal s'ouvre.
    Mais quand je charge la seconde fois, le script est chargé et le modal ne s'ouvre pas.
    
*/ 

function loadModal(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById("modal-container").innerHTML = html;
        })
        .catch(error => {
            console.error("Erreur lors du chargement du contenu :", error);
        });
}

document.getElementById("create-event").addEventListener("click", () => {
    loadModal("/partials/create_events_modal/");
});
