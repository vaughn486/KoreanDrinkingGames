$(document).ready(function(){
    var currentContent = lesson.id;
    var pageName = "games" + currentContent;
    logPageEntry(pageName);


    $(".material").hide(); // Hide all content initially
    $("#content"+currentContent).show(); // Show the first content initially

    $(".next").click(function(){
        // Hide current content, show next content
        $("#content" + currentContent).hide();
        currentContent++;
        if (currentContent == 3){
            window.location.href = '/quiz';
        } 
        $("#content" + currentContent).show();
        // Update URL
        loadContent(currentContent)
    });

    $(".back").click(function(){
        // Hide current content, show previous content
        $("#content" + currentContent).hide();
        currentContent--;
        if (currentContent == 0) {
            window.location.href = '/learn_etiquette/4';
        } 
        $("#content" + currentContent).show();
        // Update URL
        console.log("about to load data")
        loadContent(currentContent)
    });

    function loadContent(lessonId) {
        $.ajax({
            url: "/api/learn_games/" + lessonId,  
            type: "GET",
            dataType: "json",
            success: function(data) {
                console.log("success: ", data)
                if (!data.error) {
                    pageName = "games" + lessonId;
                    logPageEntry(pageName);
                    updatePageContent(data);
                    window.history.pushState(null, null, "/learn_games/" + lessonId);
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

    function logPageEntry(page) {
        $.ajax({
            url: '/enter_page/' + page,
            method: 'GET',
            success: function(response) {
                console.log('Page entry time logged:', response.last_entry_time);
            },
            error: function(xhr, status, error) {
                console.error('Error logging page entry:', error);
            }
        });
    }

})