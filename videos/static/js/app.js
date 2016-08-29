$( document ).ready(function() {
    $(".individual_video").each(function(i){
      $(this).delay(500 * i).fadeIn(500);
    })

    $(".individual_video").hover(function(){
      $(".individual_video").css("background", "rgb(255, 255, 255)")
      $(this).css("background", "rgb(68, 68, 68)")
      $(this).find("h1").css("text-decoration", "underline")
      description_text = $(this).find(".description").html();
      $(".moreinfo-sidebar").html("No description.")
      $(".moreinfo-sidebar").html(description_text)
    })

    $(".individual_video").mouseleave(function(){
      $(".individual_video").css("background", "rgb(255, 255, 255)")
      $(".moreinfo-sidebar").html("Hover over any video for more information!")
      $("h1").css("text-decoration", "none")
    })

    // Testing
    var windw = this;

    $.fn.followTo = function ( pos ) {
        var $this = this,
            $window = $(windw);

        $window.scroll(function(e){
            if ($window.scrollTop() > pos) {
              if ($this.css("top") == "260px") {
                $this.removeClass("fixed_sidebar");
                $this.animate({
                  top: "50px"
                })
              }

            } else {
              if ($this.css("top") == "50px") {
                $this.animate({
                  top: "260px"
                })
              }


            }
        });
    };

    $('.moreinfo-sidebar').followTo(190);

    function change_class_on_resize(){
      var window_width = $( window ).width();
      // console.log(window_width)
      if (window_width < 1350) {
        $(".individual_video").addClass("clear_class")
      } else {
        $(".individual_video").removeClass("clear_class")
      }
    }

    change_class_on_resize();

    $( window ).resize(function() {
      change_class_on_resize();
    });



});
