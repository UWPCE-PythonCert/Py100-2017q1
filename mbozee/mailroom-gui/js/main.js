
// MENU: KEYBOARD ACTIVATED
// if ($('#main-panel').has('#n-content')) { // not correct
//     $(document).bind("keyup",function(e) {
//         var value = String.fromCharCode(e.keyCode).toLowerCase();
//         // make associated menu item active
//         $('#' + value).focus().addClass('active');
//         $('#' + value).siblings().removeClass('active');
//         $('#' + value + '-content').siblings().hide();
//         // make associated content item visible
//         $('#main-panel').prepend($('#' + value + '-content').fadeIn(1000));

//         // cursor focus to new entry input
//         if ($('#' + value + '-content').is('#n-content')) {
//             $('input#entry-name').focus();
//             // menu keyboard icons fade, since keyboard nav disabled
//             $('ul#menu li').addClass('kb-disabled');
//         } else {
//             $('ul#menu li').removeClass('kb-disabled');
//         }
//     });
// }



// MENU: MOUSE ACTIVATED
$('ul#menu li').click(function() {
    var value = $(this).attr('id');
    $('#' + value).focus().addClass('active');
    $('#' + value).siblings().removeClass('active');
    $('#' + value + '-content').siblings().hide();
    $('#main-panel').prepend($('#' + value + '-content').fadeIn(1000));

    // cursor focus to new entry input
    if ($('#' + value + '-content').is('#n-content')) {
        $('input#entry-name').focus();
        // menu keyboard icons fade out, since keyboard nav disabled
        // $('ul#menu li').addClass('kb-disabled');
    } // else {
    //     // menu keyboard icons fade in, since keyboard nav enabled
    //     $('ul#menu li').removeClass('kb-disabled');
    // }
});



// REPORT: "STAR" DONOR ROW
$('table#report-data tr').click(function() {

    // if thead row, toggle all rows
    if ($(this).is('#report-head')) {
        $('table#report-data').toggleClass('active');

        // check all table checkboxes
        if ($('table#report-data').hasClass('active')) {
            $('table#report-data tr').addClass('active');
            $('table#report-data input[type="checkbox"').prop('checked', true);

        // otherwise... uncheck all table checkboxes
        } else {
            $('table#report-data tr').removeClass('active');
            $('table#report-data input[type="checkbox"').prop('checked', false);
        }

    // otherwise... if not thead row, just toggle itself
    } else {
        $(this).toggleClass('active');

        // if active, check its checkbox
        if ($(this).hasClass('active')) {
            $(this).children().children('input[type="checkbox"').prop('checked', true);

        // otherwise... uncheck its checkbox
        } else {
            $(this).children().children('input[type="checkbox"').prop('checked', false);
        }
    }

});


