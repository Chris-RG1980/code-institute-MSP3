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

$(document).ready(function(){
  $('.modal').modal(); // Initialize modal

  $('.pencil-bg').click(function() {
    let card = $(this).closest('.exercise-card');

    // Extract data from the card
    let muscleGroup = card.find('.muscle-group-name').text();
    let exercise = card.find('.exercise-name').text().replace('Exercise:', '').trim();
    let weight = card.find('.exercise-weight').text().replace('Weight:', '').replace('kg', '').trim();
    let sets = card.find('.exercise-sets').text().replace('Sets:', '').trim();
    let reps = card.find('.exercise-reps').text().replace('Reps:', '').trim();
    let notes = card.find('.exercise-notes').text().replace('Notes:', '').trim();
    let progressId = card.find('.progress-id').val(); // Assuming you have a hidden input for IDs

    // Populate the modal fields
    $('#edit-muscle-group').val(muscleGroup);
    $('#edit-exercise').val(exercise);
    $('#edit-weight').val(weight);
    $('#edit-sets').val(sets);
    $('#edit-reps').val(reps);
    $('#edit-notes').val(notes);
    $('#exercise-id').val(progressId); // Hidden field in modal form for ID

    // Open the modal
    $('#exercise-modal').modal('open');
  });
});