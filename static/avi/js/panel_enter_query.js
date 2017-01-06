// This must be included for javascript to safely post to Django
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings){
        var csrftoken = $.cookie('csrftoken');
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$( "#dbquery_form" ).submit(function( event ) {
    event.preventDefault();
    $('button:submit').attr("disabled", "disabled");
    submitUrl = 'run_query/';
    $.ajax({
        type: "POST",
        url: submitUrl,
        dataType: "json",
        data: $('#dbquery_form').serialize(),
        success: function(jsondat){
            $('#job-tab').click();
        },
        error: function(err){
            console.log(err);
            alert("Simple AVI has encountered an error when sending a request to " + submitUrl + ". The error has been logged in the browser, and may be possible to inspect from the browser debugger.");
        },
        complete: function(){
            $('button:submit').removeAttr("disabled");
        }
    });
});