$(function () {
    $("#l_sidebar_closer").on("click",function() {
            $("#l_sidebar").prop("checked",false);
    });
});

$(function () {
    $("#edit_menu_closer").on("click",function() {
        $(".comment_edit_menu_button").prop("value",false);
        //$(".v_c_edit_tab").prop("checked",false);
    });
});
