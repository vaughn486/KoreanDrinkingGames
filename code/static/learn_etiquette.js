$(document).ready(function(){
    var currentContent = lesson;


    $(".material").hide(); // Hide all content initially
    $("#content"+currentContent).show(); // Show the first content initially

    $(".next").click(function(){
        // Hide current content, show next content
        $("#content" + currentContent).hide();
        currentContent++;
        if (currentContent == 5) {
            window.location.href = '/learn_games/1';
        } 
        $("#content" + currentContent).show();
        // Update URL
        window.history.pushState(null, null, "/learn_etiquette/" + currentContent);
    });

    $(".back").click(function(){
        // Hide current content, show previous content
        $("#content" + currentContent).hide();
        currentContent--;
        if (currentContent == 0) {
            window.location.href = '/learn_culture/3';
        } 
        $("#content" + currentContent).show();
        // Update URL
        window.history.pushState(null, null, "/learn_etiquette/" + currentContent);
    });
})