$(document).ready(function(){
    var currentContent = lesson.id;
    console.log("Current content loaded:", currentContent);


    $(".material").hide(); // Hide all content initially
    $("#content"+currentContent).show(); // Show the first content initially

    $(".next").click(function(){
        // Hide current content, show next content
        $("#content" + currentContent).hide();
        currentContent++;
        if (currentContent == 5) {
            updateLastAccessed(currentContent - 1);
            window.location.href = '/learn_home/3';
        } 
        $("#content" + currentContent).show();
        // Update URL
        updateLastAccessed(currentContent - 1);
        loadContent(currentContent)
    });

    $(".back").click(function(){
        // Hide current content, show previous content
        $("#content" + currentContent).hide();
        currentContent--;
        if (currentContent == 0) {
            updateLastAccessed(currentContent - 1);
            window.location.href = '/learn_home/2';
        } 
        $("#content" + currentContent).show();
        // Update URL
        updateLastAccessed(currentContent - 1);
        loadContent(currentContent)
    });

    function loadContent(lessonId) {
        $.ajax({
            url: "/api/learn_etiquette/" + lessonId,  
            type: "GET",
            dataType: "json",
            success: function(data) {
                console.log("success: ", data)
                if (!data.error) {
                    updatePageContent(data);
                    window.history.pushState(null, null, "/learn_etiquette/" + lessonId);
                } else {
                    console.log(data.error);  
                }
            },
            error: function(xhr, status, error) {
                console.error("Error fetching data: ", status, error);
            }
        });
    }
    function updatePageContent(data) {
        var contentDiv = $("#content" + currentContent);
        contentDiv.find("h2").text(data.title);
        contentDiv.find("h5").text(data.description);

        $(".material").hide();  // Hide all content sections
        contentDiv.show();  // Show only the current content section
    }

    // Function to send a POST request to update the last accessed time
    function updateLastAccessed(lessonId) {
        $.ajax({
            url: "/api/update_last_accessed_etiquette",  
            type: "POST",
            dataType: "json",
            data: { lesson_id: lessonId },
            success: function(data) {
                console.log("Last accessed time updated successfully for lesson ID:", lessonId);
            },
            error: function(xhr, status, error) {
                console.error("Error updating last accessed time:", status, error);
            }
        });
    }
})