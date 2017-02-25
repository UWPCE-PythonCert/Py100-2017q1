
// $(document).keypress(function(e) {
//     if(e.which == 76) {
//         alert('You pressed');
//     }
// });

$(document).bind("keyup",function(e) {
    var value = String.fromCharCode(e.keyCode).toLowerCase();
    $('#' + value).focus();
    $('#' + value + '-content').siblings().hide();
    $('#display').prepend($('#' + value + '-content').fadeIn(1000));
});



// $('#l').click(function() {
//     $('#content-l').fadeToggle()
// });
