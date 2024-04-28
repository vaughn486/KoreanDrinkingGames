$(document).ready(function(){
    var correct_answer = question_data.a_correct;


    $(".quizbutton").click(function() {
        // Get the ID of the clicked button
        var buttonId = $(this).attr("id");
        
        if(parseInt(buttonId) === correct_answer){
            $(this).css("background-color", "green");

        }else{
            $(this).css("background-color", "red");
        }
    });

    
    
})
    
    
    
    
    