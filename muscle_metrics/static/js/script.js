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
  updateExerciseOptions($(this));
});

function updateExerciseOptions(muscleGroupElement)
{
  let muscleGroupId = $(muscleGroupElement).val();

  if(!muscleGroupId){
    return;
  }

  let exerciseSelect = $("#exercises");
  
  $.getJSON("/get_exercises?muscle_group_id=" + muscleGroupId, function(data) {
    exerciseSelect.find('option').not(':first').remove();
    exerciseSelect.val('0');

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
}

$("option:first-child", ".disable-first-option").prop('disabled', true);