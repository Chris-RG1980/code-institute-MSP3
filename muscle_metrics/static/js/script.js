// Document ready function to initialize Materialize components
$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.modal').modal();
});

// Event listener for alert dismissal
$( ".text-alert button" ).on( "click", function() {
  $(this).parent().fadeOut( "slow", function() {
    $(this).remove();
  });
});

// Event listener for a change in the '#muscleGroups' select element
$("#muscleGroups").change(function() {
  updateExerciseOptions($(this));
});

// Function to update exercise options based on selected muscle group
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

// Disables the first option in each select element with class 'disable-first-option'
$("option:first-child", ".disable-first-option").prop('disabled', true);