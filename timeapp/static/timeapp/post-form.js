$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/ajax/post-form/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_title').val('')
      $("#id_content").val('')
      ("#id_date_posted").val('')
      ("#id_author").val('')
      ("#id_post_image").val('')
    }) // End of submit event
  
  }) // End of document ready function