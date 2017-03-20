/**
 * Created by DavidALaw on 20/03/2017.
 */

    $(Document).ready(function() {

        $('#likes').click(function() {
            var imageid;
            imageid = $(this).attr("data-imageid");
            $.get('/pictaroo/image_like/', {image_id: imageid}, function(data) {
                $('#image_like_count').html(data);

            });
        });

         $('#likes_comments').click(function() {
            var commentid;
            commentid = $(this).attr("data-commentid");
            $.get('/pictaroo/comment_like/', {comment_id: commentid}, function(data) {
                $('#comment_like_count').html(data);
                $('#likes_comments').hide();

            });
        });
    });
