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
var time = 60;
function timer() {
    $('#timer-button').prop('disabled', true);
    $('#timer').html(time);
    time--;
    if (time < 0) {
        alert('You lose!');
        $('#timer-button').prop('disabled', false);
        time = 60;
    }
    else {
        setTimeout(timer, 1000);
    }
}



// Top bar sticky
function sticky_relocate() {
    var window_top = $(window).scrollTop();
    var div_top = $('#fixed-anchor').offset().top;
    if (window_top > div_top) {
        $('#stats-bar').addClass('fixed');
        $('#fixed-anchor').height($('#stats-bar').outerHeight());
    } else {
        $('#stats-bar').removeClass('fixed');
        $('#fixed-anchor').height(0);
    }
}

$(function() {
    $(window).scroll(sticky_relocate);
    sticky_relocate();
});

var dir = 1;
var MIN_TOP = 200;
var MAX_TOP = 350;

function autoscroll() {
    var window_top = $(window).scrollTop() + dir;
    if (window_top >= MAX_TOP) {
        window_top = MAX_TOP;
        dir = -1;
    } else if (window_top <= MIN_TOP) {
        window_top = MIN_TOP;
        dir = 1;
    }
    $(window).scrollTop(window_top);
    window.setTimeout(autoscroll, 100);
}



// Enable enter key for input transversing
// $('.vocab-list input').on('keydown', 'input', function (event) {
//     if (event.which == 13) {
//         event.preventDefault();
//     }
// });


