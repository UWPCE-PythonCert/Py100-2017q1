/**
 * Created by vagrant on 2/5/17.
 */

// Input turns green if answer is correct
var score = 0;
$('.vocab-list input').keyup(function () {
    if($(this).val()==$(this).attr('placeholder')) {
        $(this).css({'background-color': '#00d187', 'color': '#fff'});
        $(this).parent('li').addClass('correct');
        score++;
        $('#score span').html(score);
    }
});



// Enable enter key for input transversing
// $('.vocab-list input').on('keydown', 'input', function (event) {
//     if (event.which == 13) {
//         event.preventDefault();
//     }
// });
