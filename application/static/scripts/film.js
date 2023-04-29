function showtitle(id) {
    document.getElementById(id).style.display = "none"; 
    document.getElementById("title_" + id).style.display = "block"; 
    document.getElementById("title_" + id).style.color = "white";  
}

function hidetitle(id) {
    document.getElementById("title_" + id).style.display = "none"; 
    document.getElementById(id).style.display = "block"; 
}

// Attempted to implement universal event listener whenever an image is clicked to redirect to player with relevant film info

// function redirectToFilmPlayer(name) {
//     // Add click event listener to the container element of all the images
//     document.getElementById("movies").addEventListener("click", function(event) {
//         // Check if the clicked element is an image with an ID starting with "film_"
//         if (event.target.tagName === "IMG" && event.target.id.startsWith("film_")) {
//             // Extract the film name from the image ID
//             var name = event.target.id.substr(5);
//             // Redirect to the film_player page with the extracted film name
//             window.location.href = "{{ url_for('film_player', name='') }}" + name.replace("_", " ");
//         }
//     });
// }