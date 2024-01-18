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

$(document).ready(function() {
  var maxHeight = 0;

  // Find the tallest card
  $('.card').each(function() {
      var thisHeight = $(this).height();
      if (thisHeight > maxHeight) {
          maxHeight = thisHeight;
      }
  });

  // Set all cards to the height of the tallest card
  $('.card').height(maxHeight);
});

$(window).resize(function() {
  // Reset the height
  $('.card').height('auto');

  // Then apply the equal height logic
  var maxHeight = 0;
  $('.card').each(function() {
  var thisHeight = $(this).height();
  if (thisHeight > maxHeight) { maxHeight = thisHeight; }
  });
  $('.card').height(maxHeight);
});