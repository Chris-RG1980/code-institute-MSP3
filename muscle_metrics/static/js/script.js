$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.modal').modal();
});

// Alert dismissal
$( ".text-alert button" ).on( "click", function() {
  $(this).parent().fadeOut( "slow", function() {
    $(this).remove();
  });
});

$("#muscleGroups").change(function() {
  let muscleGroupId = $(this).val();
  let exerciseSelect = $("#exercises");
  
  $.getJSON("/get_exercises?muscle_group_id=" + muscleGroupId, function(data) {
    exerciseSelect.find('option').not(':first').remove();
    exerciseSelect.val('');

    if(data && data.length > 0) {
      exerciseSelect.prop('disabled', false);

      $.each(data, function(key, value) {   
        exerciseSelect
                .append($("<option></option>")
                          .attr("value", value.id)
                          .text(value.name)); 
      });
    }
    else {
      exerciseSelect.prop('disabled', 'disabled');
    }
  });

});