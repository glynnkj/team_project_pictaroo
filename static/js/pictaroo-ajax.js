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
    });
