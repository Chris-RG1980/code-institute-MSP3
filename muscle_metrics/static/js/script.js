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

