$(document).ready(function(){
  $('.sidenav').sidenav();
});

// Alert dismissal
$( ".text-alert button" ).on( "click", function() {
  $(this).parent().fadeOut( "slow", function() {
    $(this).remove();
  });
});