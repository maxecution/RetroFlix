function showtitle(id) {
    document.getElementById(id).style.display = "none"; 
    document.getElementById("title_" + id).style.display = "block"; 
    document.getElementById("title_" + id).style.color = "white";  
}

function hidetitle(id) {
    document.getElementById("title_" + id).style.display = "none"; 
    document.getElementById(id).style.display = "block"; 
}