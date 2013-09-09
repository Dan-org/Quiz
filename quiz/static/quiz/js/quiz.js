// this function helps us get any parameters passed ot this script
var scriptSource = (function() {
	var scripts = document.getElementsByTagName('script');
	return scripts[scripts.length - 1].src
}());
	
// Utility function to convert "a=b&c=d" into { a:'b', c:'d' }
function parseQueryString(queryString) {
    var params = {};
    if (queryString) {
        var keyValues = queryString.split('&');
        for (var i=0; i < keyValues.length; i++) {
            var pair = keyValues[i].split('=');
            params[pair[0]] = pair[1];
        }
    }
    return params;
}





function setupQuiz() {	
	
	var params 			= parseQueryString(scriptSource.split('?')[1]);
	var quiz_ajax_url 	= params.quiz_ajax_url;

	function select_question(question_panel) {        
	    $('.question-panel').not(question_panel).hide();           // Hide the other panels. 
	    question_panel.show();                                     // Show just the current panel.    
	}


	/* Make the next/previous button on the quiz show the next question. */
	function setup_link(index, offset){
	    // index, a string specifying which question, from 1...n
	    // offest, either 1 or -1 depending on if next or previous    
	    if(offset == 1){
	      var link = $('#nl_' + index);                     // get the "next" link on the current quiz question
	    }else if(offset == -1){
	      var link = $('#pl_' + index);                     // get the "next" link on the current quiz question
	    }

	    var n = (parseInt(index) + offset).toString();    

	    if(link){      
	      var question_panel = $('#qp_' + n);        // figure out which question panel should be shown next

	      link.click(function(e) {      
	        select_question(question_panel);        
	        e.preventDefault();
	        return false;
	      });
	    }
	}

	/* Sets up a radio button answers. */
	function setup_answer(index, element){
	    var answer_radio = $(element);	    
	    var radios = $(element).find('input[type="radio"]');

		
	    //answer_radio.click(function(e) {      
	    
	    radios.change(function(e) {      
	    	
			var n = parseInt(answer_radio.attr('id').substring(3)) -1 ; // figure out the radio button's id
			//var feedback = answer_radio.closest('.question-panel').find('.quiz-feedback').eq(n);
			//$('.quiz-feedback').not(feedback).hide(); 
			//feedback.show();

			var radio 			= $(this); //answer_radio.find('input');
			var question_key 	= radio.attr("name");
			question_key		= question_key.substring(0, question_key.length - "-field".length)
			var answer_key		= radio.attr("value")

			myform = answer_radio.closest('form');	// get the parent form	      
			var quiz_id = myform.attr("quiz");
			my_feedback = answer_radio.closest('.question-panel').find('.feedback')

	      	////alert($(myform).attr("id"));	      	      
	      	//$(myform).submit();  						// submit the form (by ajax) every time answer clikced

	      	//alert(quiz_id + " " + question_key + " " + answer_key);
	      	submit_answer(my_feedback, quiz_id, question_key, answer_key);

	    });

	}

	/* Submits the data from click in quiz to django view */
	function submit_answer(feedback_panel, quiz_id, question_key, answer_key){
		
		
		$.ajax({ // create an AJAX call...
            data: {
				'quiz_id':quiz_id,
				'question_key':question_key,
				'answer_key':answer_key,
            }, // get the form data}
            type: 'GET', // GET or POST
            //url: '/quiz/ajax/submitanswer/', // the file to call
            url: quiz_ajax_url, 

            success: function(response) { // on success..
                $(feedback_panel).html(response['feedback']);
            },
            error: function(xhr, textStatus, errorThrown) {
            	alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
        	}
        });
	}



	function setup_question(index, element) {    
	    var question_panel = $(element);                    // get the div for the current quiz question
	    var id = question_panel.attr('id').substring(3);  // figure out the number part of the id
	   
	    setup_link(id, 1);
	    setup_link(id, -1);
	    question_panel.find('.answer').each(setup_answer);

	    if (index == 0) {
	       select_question(question_panel);
	    }else{
	      question_panel.hide();
	    }
	}



	// function ajaxformSubmit( responseText, statusText, xhr, $form )
	// {
	// 	//alert("yo? " + $form.attr("id"));
	// 	if( responseText[ 'success' ] == true )
	// 	{
	// 		alert( "Added item: " + responseText[ 'pk' ] );
	// 	}else{
	// 		//fail
	// 	}

	//         // returning false inhibits the browser from opening a "Save As" dialog.
	// 	return false;
	// }

	// $( '#ajaxform' ).ajaxForm(
	// 	//function(){alert("Thank you for your comment!"); });
 //        { success: ajaxformSubmit,
 //          dataType: 'json'});
 //          //dataType: 'json',
 //          //clearForm : true,
 //          //resetForm : true } );


	//var _max_panel_height = Math.max.apply(window, $('.panel').map(function(i, e) { return $(e).height() }));
	$('.question-panel').each(setup_question);
	$('.quiz').find('.feedback').html('');

}

//$(document).ready(setupQuiz);