$(document).ready(function(){
    function buttonClicked(){
        alert("button clicked");
        updateData();
    }
    
    
    $('#quizbutton').click(buttonClicked);
    
    
})
    
    
    
    
    
    
function updateData() {
    fetch('/get_interactive_data') // Send a GET request to the server
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
    // Update the content of the page with the updated data
    document.getElementById('updated-data').innerText = data.interactive_data;
    })
    .catch(error => console.error('Error fetching updated data:', error));
}
    
    