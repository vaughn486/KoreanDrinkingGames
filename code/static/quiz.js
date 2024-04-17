// $(document).ready(function(){
//     var current_quiz_question

//     $("#testbutton").click(function(){
//         alert("button clicked");
//         nextQuestion(current_quiz_question);
//     })

//     // getting current question id
//     $.ajax({
//         type: "GET",
//         url: "/get_current_question",
//         success: function(result){
//             console.log("Success! Current quiz question: ", result)
//             //from server side function
//             current_quiz_question = result.current_quiz_question;
//         },
//         error: function(request, status, error){
//             console.error("Error retrieving data: ", error);
//         }
//     });



    


// })

// function nextQuestion(question_id){
//     question_id++;

//     $.ajax({
//         url: "/quiz_data/" + question_id,  
//         type: "GET",
//         dataType: "json",
//         success: function(result) {
//             //printout statement
//             console.log("Success: ", result)
//             //should be the next quiz question data

            
//             // pageName = "games" + lessonId;
//             // logPageEntry(pageName);
//             // updatePageContent(data);
//             // window.history.pushState(null, null, "/learn_games/" + lessonId);
            
//         },
//         error: function(request, status, error){
//             console.error("Error retrieving data: ", error);
//         }
//     });
// }


