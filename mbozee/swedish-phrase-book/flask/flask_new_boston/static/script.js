/**
 * Created by vagrant on 2/5/17.
 */

// Input turns green if answer is correct
var score = 0;
$('.vocab-list input').change(function () {
    if($(this).val()==$(this).attr('placeholder')) {
        $(this).css({'background-color': '#00d187', 'color': '#fff'});
        $(this).prop('disabled', true);
        $(this).parent('li').addClass('correct');
        score++;
        $('#score span').html(score);
    }
    else {
        $(this).css({'background-color': '#FF5300', 'color': '#fff'});
        $(this).prop('disabled', true);
        $(this).parent('li').addClass('incorrect');
    }
});



// Countdown timer
function timer() {
    var time = 5;
    $('#timer').html(time);
    time--;
    if (time < 0) {
        alert('You lose!');
    }
    else {
        setTimeout(timer, 1000);
    }
}



// Enable enter key for input transversing
// $('.vocab-list input').on('keydown', 'input', function (event) {
//     if (event.which == 13) {
//         event.preventDefault();
//     }
// });
