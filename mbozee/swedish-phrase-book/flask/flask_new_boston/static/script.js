/**
 * Created by vagrant on 2/5/17.
 */

// Input turns aqua if answer is correct
$('.vocab-list input').keyup(function () {
    if($(this).val()==$(this).attr('placeholder')) {
        $(this).css({'background-color': 'aqua', 'color': '#fff'});
    }
});
