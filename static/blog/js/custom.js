// code
console.log("Yes it works");
$(document).ready(function (e) {
    $(".delete-btn-open").click(function (e) {
        e.preventDefault();
        var title = $(this).attr("data-title");
        var id = $(this).attr("data-id");
        $(".delete-btn").click();
        $(".modal-title").text(title);
        $(".article_id").val(id);
    });
});