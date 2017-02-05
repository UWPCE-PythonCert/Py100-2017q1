/**
 * Created by vagrant on 2/5/17.
 */

// Input turns aqua if answer is correct
var score = 0;
$('.vocab-list input').keyup(function () {
    if($(this).val()==$(this).attr('placeholder')) {
        $(this).css({'background-color': 'aqua', 'color': '#fff'});
        score++;
        $('#score span').html(score);
    }
});
