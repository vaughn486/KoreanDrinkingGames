$(document).ready(function(){
    var correct_answer = question_data.a_correct;


    $(".quiz-question").click(function() {
        // Get the ID of the clicked button
        var buttonId = $(this).attr("id");
        
        if(parseInt(buttonId) === correct_answer){
            $(this).css("background-color", "rgb(139, 176, 142)");
            $(this).css("border", "0px solid rgb(139, 176, 142");
            $(this).css("outline", "none");

        }else{
            $(this).css("background-color", "rgb(214, 144, 144)");
            $(this).css("border", "0px solid rgb(214, 144, 144");
            $(this).css("outline", "none");
        }
    });

    
    
})


    
    
    